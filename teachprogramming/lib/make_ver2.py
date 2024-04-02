import re
from itertools import chain
from functools import cached_property, reduce
from collections import defaultdict
from pathlib import Path
from types import MappingProxyType
from contextlib import contextmanager
import io


# Using the old `make_ver` under the hood as a transition. It needs re-writing
try:  # pytest has it one one, running from the cmdline another ?? wha?
    from make_ver import make_ver  # TODO: deprecate and reimplement
except ImportError:
    from .make_ver import make_ver  # TODO: deprecate and reimplement


EXCLUDED_EXTENSIONS = frozenset({'ver', 'yaml', 'yml', 'txt', 'md', 'json', 'csproj', '', 'Makefile', 'Dockerfile', 
    'editorconfig', 'cache',  # HACK - this is getting out of hand - we do a filescan() and get all files - csharp creates some cancer with bin/obj folders and I need a way to ignore them - for now I just hide rougue files here. Please remove this hack line and try to debug this properly
})


def parse_legacy_version_data(data):
    r"""
    >>> ver = parse_legacy_version_data('''
    ... VERNAME: base            base
    ... VERNAME: background      base,background
    ... VERNAME: copter          base,background,copter
    ... VERNAME: parallax         base,background,parallax
    ... VERNAME: collision_single base,background,copter,collision_single
    ... VERNAME: collision_multi  base,background,copter,collision_single,collision_multi
    ... VERNAME: level           base,background,copter,collision_single,level
    ... VERNAME: physics         base,background,copter,collision_single,physics
    ... VERNAME: full            base,background,copter,physics,collision_single,collision_multi,parallax,level
    ... VERNAME: fish_full       base,background,copter,collision_single,fish_background
    ... REPLACE: CopterLevel WITH FishLevel FOR fish_full
    ... REPLACE: ship.gif WITH fish.gif FOR fish_full
    ... ''')
    >>> ver.keys()
    dict_keys(['base', 'background', 'copter', 'parallax', 'collision_single', 'collision_multi', 'level', 'physics', 'full', 'fish_full'])
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

RE_VER = re.compile(r'VER:\s*(?P<ver>.*?)(\s+|$)(NOT\s*(?P<ver_exclude>.*?(\s+|$)))?', flags=re.IGNORECASE)
def extract_versions_from_data(data):
    r"""
    >>> sorted(extract_versions_from_data('''
    ... # Some code
    ... const TT = `ABC`;  // VER:test3      Gotta be a thing I'm sure
    ... function abc(x,y,z) {  // VER: test1
    ...     return x + y + z;  //    VER:          test2
    ... }  // VER: test1
    ... '''))
    ['test1', 'test2', 'test3']
    """
    return {match.group('ver') for match in RE_VER.finditer(data)}




@contextmanager
def _testfiles():
    import os
    import tempfile
    td = tempfile.TemporaryDirectory()
    filenames = set()
    def write_file(filename, data):
        filename = os.path.join(td.name, filename)
        with open(filename, 'wt', encoding='utf8') as filehandle:
           _ = filehandle.write(data)
        filenames.add(filename)
    write_file('test.py', '''
print('Hello World')
print('Hello Test')  # VER: test4
''')
    write_file('test.js', '''
console.log("Hello World")    // VER: hello_world
''')
    write_file('Test.java', '''
public class Test {                          // VER: test1
    public Test() {                          // VER: test2
        System.out.println("Hello World");   // VER: hello_world
    }                                        // VER: test2
    public static void main(String[] args) {new Test();}  // VER: test2
}  // VER: test1
''')
    write_file('test.ver', '''
VERNAME: base           base
''')
    yield filenames
    td.cleanup()



class ProjectVersions():
    r"""
    make_ver2

    read in a project and have all permutations of that project in an object
    We can lazily evaluate each version

    >>> with _testfiles() as filenames:
    ...     p = ProjectVersions(filenames)

    >>> p.versions['base']
    ('base',)
    >>> p.data['py']['base']
    "\nprint('Hello World')"
    """
    def __init__(self, filenames):
        self.files = MappingProxyType({
            f.suffix.strip('.'): f.open(encoding='utf8').read()
            for f in map(Path, filenames)
        })
        self.data  # generate cache on object creation

    @cached_property
    def langauges(self):
        return frozenset(self.files.keys()) - frozenset({'txt',}) - EXCLUDED_EXTENSIONS

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
        raise Exception('no version information')

    #@lru_cache?
    def langauge(self, language):
        return MappingProxyType({
            ver_name: '\n'.join(
                make_ver(
                    io.StringIO(self.files[language]), 
                    ver_path=ver_path,
                    lang=language,
                    process_additional_metafiles=False,
                )
            )
            for ver_name, ver_path in self.versions.items()
        })

    @cached_property
    def data(self):
        return MappingProxyType({l: self.langauge(l) for l in self.langauges})



class LanguageVersions():
    r"""

    >>> with _testfiles() as filenames:
    ...     l = LanguageVersions(filenames)

    >>> l.versions
    ['hello_world', 'test1', 'test2', 'test4']
    >>> l.data['py']['test4']
    "print('Hello Test')"
    """

    VERSION_ORDER = [  # TODO: these should be moved eventually
        'title',
        'download',
        'help',
        'run',
        'hello_world',
        'read_line_from_console',
        'comment',
        'define_variables',
        'define_constants',
        'arithmetic',
        'if_statement',
        'if_statement_more',
        'while_loop',
        'until_loop',
        'for_loop',
        'for_each_loop',
        'file_write',
        'file_read',
        'string_concatenation',
        'split_strings',
        'convert_string_to_integer_and_back',
        'convert_double_to_string_and_back',
        'function',
        'function_with_return_value',
        'function_with_params_by_reference',
        'function_with_params_by_value',
        'function_with_param_function',
        'define_fixed_array',
        'define_list',
        'define_2d_arrays_with_nested_arrays',
        'define_2d_arrays_with_1d_array_with_lookup_function',
        'define_2d_arrays_with_dictionary',
        'define_map',
        'define_set',
        'error_handling',
        'join_strings',
        'random_number',
        'class',
        'read_csv_into_array_of_classs',
        'sleep',
        'list_comprehension',
        'dict_comprehension',
    ]

    def __init__(self, filenames):
        def _amalgamate_files_with_same_extension(acc, f):
            with f.open(encoding='utf8') as _f:
                acc[f.suffix.strip('.')] += _f.read()
            return acc
        self.files = MappingProxyType(dict(
            reduce(
                _amalgamate_files_with_same_extension,
                map(Path, filenames),
                defaultdict(str)
            )
        ))
        self.data  # generate cache on object creation

    @cached_property
    def langauges(self):
        return frozenset(self.files.keys()) - EXCLUDED_EXTENSIONS

    @cached_property
    def versions(self):
        """
        extract all files for VER markers in all files
        Each vername is a standalone version
        """
        version_order_set = frozenset(self.VERSION_ORDER)
        self_versions_set = frozenset(chain.from_iterable(
            extract_versions_from_data(data)
            for data in self.files.values()
        ))
        return [ver for ver in self.VERSION_ORDER if ver in self_versions_set] + sorted(self_versions_set - version_order_set)

    def langauge(self, language):
        return MappingProxyType({
            ver: '\n'.join(
                make_ver(
                    io.StringIO(self.files[language]), 
                    ver_path=ver,
                    lang=language,
                    process_additional_metafiles=False,
                )
            )
            for ver in self.versions
        })

    @cached_property
    def data(self):
        return MappingProxyType({l: self.langauge(l) for l in self.langauges})
