# Inspired by
# https://docs.pytest.org/en/stable/example/nonpython.html#yaml-plugin

import json
from pathlib import Path

import pytest


def pytest_collect_file(parent: pytest.Dir, file_path: Path):
    if file_path.suffix == ".json":
        return ProjectFile.from_parent(parent, path=file_path)


class ProjectFile(pytest.File):
    def collect(self):
        project = json.load(self.path.open(encoding="utf-8"))
        #for name, spec in sorted(raw.items()):
        #    yield YamlItem.from_parent(self, name=name, spec=spec)
