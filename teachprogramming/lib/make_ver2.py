from functools import cached_property
from pathlib import Path


class ProjectVersions():
    r"""
    make_ver2

    read in a project and have all permutations of that project in an object
    We can lazily evaluate each version

    >>> import os
    >>> import tempfile
    >>> td = tempfile.TemporaryDirectory()
    >>> filenames = set()
    >>> def write_file(filename, data):
    ...     filename = os.path.join(td.name, filename)
    ...     with open(filename, 'wt') as filehandle:
    ...         _ = filehandle.write(data)
    ...     filenames.add(filename)
    >>> write_file('test.py', '''
    ... print('Hello World')
    ... ''')
    >>> write_file('test.js', '''
    ... console.log("Hello World")
    ... ''')
    >>> write_file('Test.java', '''
    ... public class Test {
    ...     public Test() {
    ...         System.out.println("Hello World");
    ...     }
    ...     public static void main(String[] args) {new Test();}   
    ... }
    ... ''')
    >>> write_file('test.ver', '''
    ... VERNAME: base           base
    ... ''')

    >>> p = ProjectVersions(filenames)
    >>> p.data

    >>> td.cleanup()

    """
    def __init__(self, filenames):
        self.files = {
            f.suffix.strip('.'): f.open(encoding='utf8').read()
            for f in map(Path, filenames)
        }
    
    @cached_property
    def versions(self):
        """
        Parse versions from .ver file
        """
        pass

    @cached_property
    def data(self):
        """
        Output as dict structure
        """
        return self.files
