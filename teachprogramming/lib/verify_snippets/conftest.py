# Inspired by
# https://docs.pytest.org/en/stable/example/nonpython.html#yaml-plugin

import json
import tempfile
from pathlib import Path
from typing import TypedDict, Unpack

import pytest

PATH_PROJECTS = Path("projects").absolute()


LANGUAGES_SUPPORTED = frozenset({"py"})


def pytest_ignore_collect(collection_path: Path, path, config: pytest.Config):
    try:
        collection_path.relative_to(PATH_PROJECTS.absolute())
        return False
    except ValueError:
        return True


def pytest_collect_file(parent: pytest.Dir, file_path: Path):
    if file_path.suffix == ".json":
        file_path.name.endswith(".ver.json")
        return ProjectFile.from_parent(parent, path=file_path)


class ProjectItemSpec(TypedDict):
    name: str
    language: str
    version: str
    code: str


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
                    spec=ProjectItemSpec(name=name, language=language, version=version, code=code),
                )


class ProjectItem(pytest.Item):
    def __init__(self, *, spec: ProjectItemSpec, **kwargs):
        super().__init__(**kwargs)
        self.spec = spec

    def runtest(self):
        if self.spec['language'] not in LANGUAGES_SUPPORTED:
            raise pytest.skip.Exception(f"Unsupported language {self.spec['language']}")

        # https://stackoverflow.com/questions/66037780/how-do-i-require-fixtures-in-a-pytest-plugin
        # No fixtures in plugins?

        with tempfile.TemporaryDirectory() as tempdir:
            dispatch_compile_test(tempdir, **self.spec)

    def repr_failure(self, excinfo):
        """Called when self.runtest() raises an exception."""
        if isinstance(excinfo.value, ProjectCompileException):
            return "\n".join(
                [
                    "usecase execution failed",
                    "   spec failed: {1!r}: {2!r}".format(*excinfo.value.args),
                    "   no further details known at this point.",
                ]
            )
        return super().repr_failure(excinfo)

    def reportinfo(self):
        return (self.path, 0, f"usecase: {self.name}")


class ProjectCompileException(Exception):
    """Custom exception for error reporting."""


def dispatch_compile_test(tempdir, name, language, version, code):
    breakpoint()
    # raise ProjectCompileException(self, self.name, self.code)
