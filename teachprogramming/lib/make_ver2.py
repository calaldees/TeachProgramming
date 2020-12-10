import re
from functools import cached_property
from pathlib import Path
from types import MappingProxyType

import io
try:  # pytest has it one one, running from the cmdline another ?? wha?
    from make_ver import make_ver  # TODO: deprecate and reimplement
except ImportError:
    from .make_ver import make_ver  # TODO: deprecate and reimplement


def parse_legacy_version_data(data):
    r"""
    >>> ver = parse_legacy_version_data('''
    ... VERNAME: base            base
    ... VERNAME: background      base,background
    ... VERNAME: copter          base,background,copter
    ... VERNAME: paralax         base,background,paralax
    ... VERNAME: colision_single base,background,copter,colision_single
    ... VERNAME: colision_multi  base,background,copter,colision_single,colision_multi
    ... VERNAME: level           base,background,copter,colision_single,level
    ... VERNAME: physics         base,background,copter,colision_single,physics
    ... VERNAME: full            base,background,copter,physics,colision_single,colision_multi,paralax,level
    ... VERNAME: fish_full       base,background,copter,colision_single,fish_background
    ... REPLACE: CopterLevel WITH FishLevel FOR fish_full
    ... REPLACE: ship.gif WITH fish.gif FOR fish_full
    ... ''')
    >>> ver.keys()
    dict_keys(['base', 'background', 'copter', 'paralax', 'colision_single', 'colision_multi', 'level', 'physics', 'full', 'fish_full'])
    >>> ver['copter']
    ('base', 'background', 'copter')
    """
    RE_VERNAME = re.compile(r'VERNAME:\s*(?P<vername>.*?)\s+(?P<versions>.*?)(\s+|$)', flags=re.IGNORECASE)
    # TODO: implement REPLACE
    #RE_REPLACE = re.compile(r'REPLACE:\s*(?P<replace>.*?)\s*WITH\s*(?P<replacement>.*?)\s*FOR\s*(?P<ver_names>.*?)(\s+|$)', flags=re.IGNORECASE)
    return MappingProxyType({
        match.group('vername'): tuple(v.strip() for v in match.group('versions').split(','))
        for match in RE_VERNAME.finditer(data)
    })



class ProjectVersions():
    r"""
    make_ver2

    read in a project and have all permutations of that project in an object
    We can lazily evaluate each version

    >>> from contextlib import contextmanager
    >>> @contextmanager
    ... def testfiles():
    ...     import os
    ...     import tempfile
    ...     td = tempfile.TemporaryDirectory()
    ...     filenames = set()
    ...     def write_file(filename, data):
    ...         filename = os.path.join(td.name, filename)
    ...         with open(filename, 'wt') as filehandle:
    ...            _ = filehandle.write(data)
    ...         filenames.add(filename)
    ...     write_file('test.py', '''
    ... print('Hello World')
    ... ''')
    ...     write_file('test.js', '''
    ... console.log("Hello World")
    ... ''')
    ...     write_file('Test.java', '''
    ... public class Test {
    ...     public Test() {
    ...         System.out.println("Hello World");
    ...     }
    ...     public static void main(String[] args) {new Test();}
    ... }
    ... ''')
    ...     write_file('test.ver', '''
    ... VERNAME: base           base
    ... ''')
    ...     yield filenames
    ...     td.cleanup()

    >>> with testfiles() as filenames:
    ...     p = ProjectVersions(filenames)

    >>> p.versions['base']
    ('base',)
    >>> p.data['py']['base']

    """
    def __init__(self, filenames):
        self.files = MappingProxyType({
            f.suffix.strip('.'): f.open(encoding='utf8').read()
            for f in map(Path, filenames)
        })
        self.data  # generate cache on object creation

    @cached_property
    def langauges(self):
        return frozenset(self.files.keys()) - frozenset({'ver', 'yaml', 'yml', 'txt', 'md'})

    @cached_property
    def versions(self):
        """
        Parse versions from .ver or .yaml file
        """
        file_exts = set(self.files.keys())
        if {'yaml', 'yml'} & file_exts:
            raise NotImplementedError('yaml version file format not implemented')
        if {'ver',} & file_exts:
            return parse_legacy_version_data(self.files['ver'])
        raise Exception()

    #@lru_cache?
    def langauge(self, language):
        return MappingProxyType({
            ver_name: '\n'.join(make_ver(io.StringIO(self.files[language]), ver_path=ver_path, lang=language, process_additional_metafiles=False))
            for ver_name, ver_path in self.versions.items()
        })

    @cached_property
    def data(self):
        return MappingProxyType({l: self.langauge(l) for l in self.langauges})
