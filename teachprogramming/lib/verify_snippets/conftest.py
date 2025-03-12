# Inspired by
# https://docs.pytest.org/en/stable/example/nonpython.html#yaml-plugin

import re
import json
from pathlib import Path
from typing import NamedTuple, Callable
from types import MappingProxyType
import subprocess
import logging
import shutil

import pytest


log = logging.getLogger(__name__)

PATH_PROJECTS = Path("projects").absolute()
PATH_LANGUAGES = Path('languages').absolute()
LANGUAGE_TO_FOLDER_MAPPING = MappingProxyType({
    'py': 'python',
    'cs': 'csharp',
})

# `tempdir` creates 'secure' temp folders.
# These are not available to other users.
# docker on mac runs as a different user.
# None of the temp folders from env work because again - owned by the user
#   environ.get('TMPDIR') or environ.get('TEMP') or environ.get('TMP') or
tempdir = Path('.').joinpath('_language_runner')
tempdir.mkdir(exist_ok=True)
def clear(path: Path):
    # https://docs.python.org/3/library/pathlib.html#pathlib.Path.walk
    for root, dirs, files in path.walk(top_down=False):
        for name in files:
            (root / name).unlink()
        for name in dirs:
            (root / name).rmdir()


# Docker -----------------------------------------------------------------------

def get_built_docker_language_runners() -> set[str]:
    result = subprocess.run(
        ("docker", "images", "language_runner", "--format", "json"),
        capture_output=True,
        timeout=5,
        text=True,
        check=True,
    )
    return {container['Tag'] for container in map(json.loads, filter(None, result.stdout.split('\n')))}

BUILT_LANGUAGES_RUNNERS = get_built_docker_language_runners()

def get_docker_folder_for_language(language: str) -> Path:
    return PATH_LANGUAGES.joinpath(LANGUAGE_TO_FOLDER_MAPPING.get(language, language))

def build_docker_language_runner(language) -> subprocess.CompletedProcess:
    return subprocess.run(
        ("docker", "build", get_docker_folder_for_language(language), "--tag", f"language_runner:{language}"),
        capture_output=True,
        timeout=120,
        text=True,
        check=True,
    )


# Project Compile --------------------------------------------------------------

class ProjectItemSpec(NamedTuple):
    name: str
    language: str
    version: str
    code: str

    def exec_language(self, language_args: tuple[str]=()):
        workdir = f"/{self.language}"
        docker_args = (
            "docker", "run", "--rm",
            "--workdir", workdir,
            "--volume", f"{tempdir.absolute()}:{workdir}:rw",
            f"language_runner:{self.language}",  # should match image name built from `build_docker_language_runner`
        )
        result = subprocess.run(
            docker_args + language_args,
            capture_output=True,
            timeout=30,
            text=True,
            #check=True,
        )
        if result.returncode != 0:
            raise ProjectCompileException(self, result)


class ProjectCompileException(Exception):
    def __init__(self, spec: ProjectItemSpec, result: subprocess.CompletedProcess):
        super().__init__()
        self.spec = spec
        self.result = result


def compile_test_python(spec: ProjectItemSpec):
    path_code_file = tempdir.joinpath(spec.name)
    path_code_file.write_text(spec.code)
    spec.exec_language(("python3", "-m", "py_compile", path_code_file.name))


def get_java_main_classname(code: str) -> str:
    # utter mess - using regex to get this is poor form
    if match := re.search(r'class (\w+?) .*public static void main', code, re.DOTALL):
        return match.group(1)
    raise Exception('unable to find top level classname for filename', code)
def compile_test_java(spec: ProjectItemSpec):
    path_code_file = tempdir.joinpath(get_java_main_classname(spec.code) + ".java")
    path_code_file.write_text(spec.code)
    spec.exec_language(("javac", path_code_file.name))


def copy_cs_file_to_workdir(filename: str):
    shutil.copyfile(get_docker_folder_for_language('cs').joinpath(filename), tempdir.joinpath(filename))
def compile_test_csharp(spec: ProjectItemSpec):
    copy_cs_file_to_workdir('main.csproj')
    copy_cs_file_to_workdir('packages.log.json')
    path_code_file = tempdir.joinpath(spec.name)
    path_code_file.write_text(spec.code)
    # TODO: edit `main.csproj` to point to top level cs class
    # TODO: probably need to cleanup the other cs files or this might be contaminated from previous runs
    spec.exec_language(('dotnet', 'build'))


LANGUAGES: MappingProxyType[str, Callable] = MappingProxyType(
    {
        "py": compile_test_python,
        "java": compile_test_java,
        "cs": compile_test_csharp,
        #"php": ???
        #"vb": ???
    }
)


# PyTest -----------------------------------------------------------------------

def pytest_ignore_collect(collection_path: Path, config: pytest.Config):
    try:
        collection_path.relative_to(PATH_PROJECTS.absolute())
        return False
    except ValueError:
        return True


def pytest_collect_file(parent: pytest.Dir, file_path: Path):
    if file_path.suffix == ".json":
        return ProjectFile.from_parent(parent, path=file_path)


def pytest_collection_modifyitems(session: pytest.Session, config: pytest.Config, items: list[pytest.Item]):
    languages_selected = set(config.option.language or ()) or LANGUAGES.keys()
    items_deselected = tuple(
        item for item in items
        if isinstance(item, ProjectItem) and item.spec.language not in languages_selected
    )
    config.hook.pytest_deselected(items=items_deselected)
    items[:] = tuple(
        item for item in items
        if isinstance(item, ProjectItem) and item.spec.language in languages_selected
    )


def pytest_addoption(parser: pytest.Parser, pluginmanager: pytest.PytestPluginManager):
    parser.addoption("--language", default=None, help="Project languages to test", choices=LANGUAGES.keys(), action="extend", nargs="+", type=str)


def pytest_collection_finish(session: pytest.Session):
    # Build required language_runner containers
    languages_in_items = {
        item.spec.language
        for item in session.items
        if hasattr(item, 'spec')
    }
    language_runners_to_build = (languages_in_items - BUILT_LANGUAGES_RUNNERS) & LANGUAGES.keys()
    for language in language_runners_to_build:
        print(f"docker build --tag language_runner:{language}")  #log.info
        build_docker_language_runner(language)
        BUILT_LANGUAGES_RUNNERS.add(language)


def pytest_sessionfinish(session: pytest.Session, exitstatus: int):
    clear(tempdir)


class ProjectFile(pytest.File):
    def collect(self):
        project_name = self.path.stem
        project = json.load(self.path.open(encoding="utf-8"))
        for language, versions in project["languages"].items():
            for version, code in versions.items():
                name = ".".join((project_name, version or "base", language))
                yield ProjectItem.from_parent(
                    self,
                    name=name,
                    spec=ProjectItemSpec(
                        name=name, language=language, version=version, code=code
                    ),
                )


class ProjectItem(pytest.Item):
    def __init__(self, *, spec: ProjectItemSpec, **kwargs):
        super().__init__(**kwargs)
        self.spec = spec

    def runtest(self):
        if self.spec.language not in LANGUAGES.keys():
            raise pytest.skip.Exception(f"Unsupported language {self.spec.language}")

        # If we clear the folder, there is some race hazard with mounting this in docker and the folder is not writeable
        # A delay of 0.5 seconds solves most of this - but I don't want to slow the tests down
        #clear(tempdir)
        #sleep(0.5)
        LANGUAGES[self.spec.language](self.spec)

        # https://stackoverflow.com/questions/66037780/how-do-i-require-fixtures-in-a-pytest-plugin
        # No fixtures in plugins?

    def repr_failure(self, exinfo: pytest.ExceptionInfo):
        """Called when self.runtest() raises an exception."""
        if isinstance(exinfo.value, subprocess.CalledProcessError):
            return exinfo.value.stderr
        if isinstance(exinfo.value, ProjectCompileException):
            return exinfo.value.result.stdout + exinfo.value.result.stderr + exinfo.value.spec.code
        return super().repr_failure(exinfo)

    def reportinfo(self):
        return (self.path, 0, f"usecase: {self.name}")
