# Inspired by
# https://docs.pytest.org/en/stable/example/nonpython.html#yaml-plugin

import json
from pathlib import Path
from typing import NamedTuple, Callable
from types import MappingProxyType
import subprocess
from os import environ

import pytest


PATH_PROJECTS = Path("projects").absolute()
PATH_LANGUAGES = Path('languages').absolute()
LOOKUP_LANGUAGE_FOLDER = MappingProxyType({
    'py': 'python'
})


def get_built_docker_language_runners() -> set[str]:
    result = subprocess.run(
        ("docker", "images",  "--format", "json"), #"language_runner",
        capture_output=True,
        timeout=5,
        text=True,
        check=True,
    )
    return {container['Tag'] for container in map(json.loads, filter(None, result.stdout.split('\n')))}

def build_docker_language_runner(language) -> subprocess.CompletedProcess:
    return subprocess.run(
        ("docker", "build", PATH_LANGUAGES.joinpath(LOOKUP_LANGUAGE_FOLDER.get(language, language)), "--tag", f"language_runner:{language}"),
        capture_output=True,
        timeout=120,
        text=True,
        check=True,
    )

BUILT_LANGUAGES = get_built_docker_language_runners()

# `tempdir` creates 'secure' temp folders.
# These are not available to other users.
# docker on mac runs as a different user.
# None of the temp folders from env work because again - owned by the user
#   environ.get('TMPDIR') or environ.get('TEMP') or environ.get('TMP') or
tempdir = Path('.').joinpath('_language_runner')
tempdir.mkdir(exist_ok=True)


class ProjectItemSpec(NamedTuple):
    name: str
    language: str
    version: str
    code: str

    def exec_language(self, language_args: tuple[str]):
        if self.language not in BUILT_LANGUAGES:
            BUILT_LANGUAGES.add(self.language)
            build_docker_language_runner(self.language)

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


def compile_test_java(spec: ProjectItemSpec):
    # java? rename file?
    pass


def compile_test_csharp(spec: ProjectItemSpec):
    # csharp create manifest?
    pass


LANGUAGES: MappingProxyType[str, Callable] = MappingProxyType(
    {"py": compile_test_python}
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
        file_path.name.endswith(".ver.json")
        return ProjectFile.from_parent(parent, path=file_path)


#def pytest_collected():
#    # TODO: this is not a real name I need the docs to look it up
#    for language in {test.spec.language for test in collected.tests}:
#        build_docker_language_runner(language)


# TODO: correct hook for teardown
#def pytest_teardown():
#    tempdir.cleanup()


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
