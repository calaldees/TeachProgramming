# Inspired by
# https://docs.pytest.org/en/stable/example/nonpython.html#yaml-plugin

import json
from pathlib import Path

import pytest

PATH_PROJECTS = Path("projects").absolute()


LANGUAGES_SUPPORTED = frozenset({'py'})

def pytest_collect_file(parent: pytest.Dir, file_path: Path):
    try:
        # exclude detection of files outside project path - is there a better way of this?
        file_path.relative_to(PATH_PROJECTS.absolute())
    except ValueError:
        return
    if file_path.suffix == ".json":
        file_path.name.endswith(".ver.json")
        return ProjectFile.from_parent(parent, path=file_path)


class ProjectFile(pytest.File):
    def collect(self):
        project_name = self.path.stem
        project = json.load(self.path.open(encoding="utf-8"))
        for language, versions in project["languages"].items():
            for version, code in versions.items():
                name = ".".join((project_name, version or 'base', language))
                yield ProjectItem.from_parent(self, name=name, language=language, version=version, code=code)


class ProjectItem(pytest.Item):
    def __init__(self, *, language, version, code, **kwargs):
        super().__init__(**kwargs)
        self.language = language
        self.version = version
        self.code = code

    def runtest(self):
        #print(self.name)
        #breakpoint()
        if self.language not in LANGUAGES_SUPPORTED:
            raise pytest.skip.Exception()
        if False:
            raise ProjectCompileException(self, self.name, self.code)

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
        return self.path, 0, f"usecase: {self.name}"


class ProjectCompileException(Exception):
    """Custom exception for error reporting."""
