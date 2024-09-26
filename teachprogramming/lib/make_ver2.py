import re
from itertools import chain
from functools import cached_property, reduce
from collections import defaultdict
from pathlib import Path
from types import MappingProxyType
from contextlib import contextmanager
import io
from textwrap import dedent

# Using the old `make_ver` under the hood as a transition. It needs re-writing
try:  # pytest has it one one, running from the cmdline another ?? wha?
    from make_ver import make_ver  # TODO: deprecate and reimplement
except ImportError:
    from .make_ver import make_ver  # TODO: deprecate and reimplement


# Deprecated: Remove
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
#@_deprecated(remove='To be replaced with VersionModel')
def extract_versions_from_data(data):
    r"""
    >>> sorted(extract_versions_from_data('''
    ... # Some code
    ... const TT = `ABC`;  // VER:test3      Gotta be a thing I'm sure
    ... function abc(x,y,z) {  // VER: test1
    ...     return x + y + z;  //    VER:          test2
    ... }  // VER: test1
    ... VER: test1,test4
    ... '''))
    ['test1', 'test2', 'test3', 'test4']
    """
    return set(filter(bool, (
        s.strip() for s in chain.from_iterable(
            match.group('ver').split(',') for match in RE_VER.finditer(data)
        )
    )))




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
    write_file('test.py', dedent('''
        print('Hello World')
        print('Hello Test')  # VER: test4
    '''))
    write_file('test.js', dedent('''
        console.log("Hello World")    // VER: hello_world
    '''))
    write_file('Test.java', dedent('''
        public class Test {                          // VER: test1
            public Test() {                          // VER: test2
                System.out.println("Hello World");   // VER: hello_world
            }                                        // VER: test2
            public static void main(String[] args) {new Test();}  // VER: test2
        }  // VER: test1
    '''))
    write_file('test.ver', dedent('''
        VERNAME: base           base
    '''))
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
    def languages(self):
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
    def language(self, language):
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
        return MappingProxyType({l: self.language(l) for l in self.languages})



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
        """
        Concept:
            `/java/main_stuff.java`
            `/java/graphics_stuff.java`
            `/java/network_stuff.java`
        are amalgamated/concatenated into `self.files['java']`
        This means that we can have
            `hello_world`
            `draw_sqaure`
            `get_http`
        defined in different files but still available as a version
        """
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
    def languages(self):
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
        return MappingProxyType({l: self.langauge(l) for l in self.languages})


from typing import NamedTuple, Iterable, Self

class Comment(NamedTuple):
    comment_start: str
    comment_end: str = ''
    #@cached_property
    @property
    def regex_ver(self):
        """
        >>> test_py1 = '''print('helloworld') # VER: 1|2|3 # More comments'''
        >>> test_py2 = '''print('helloworld') # VER: 1|2|3#More comments'''
        >>> test_py3 = '''print('helloworld') #VER:1|2|3'''
        >>> Comment(r'#').regex_ver.search(test_py1)['ver']
        '1|2|3'
        >>> Comment(r'#').regex_ver.search(test_py2)['ver']
        '1|2|3'
        >>> Comment(r'#').regex_ver.search(test_py3)['ver']
        '1|2|3'

        >>> test_js1 = '''console.log('helloworld') // VER: 1|2|3 // More comments'''
        >>> test_js2 = '''console.log('helloworld') // VER: 1|2|3//More comments'''
        >>> test_js3 = '''console.log('helloworld') //VER:1|2|3'''
        >>> Comment(r'//').regex_ver.search(test_js1)['ver']
        '1|2|3'
        >>> Comment(r'//').regex_ver.search(test_js2)['ver']
        '1|2|3'
        >>> Comment(r'//').regex_ver.search(test_js3)['ver']
        '1|2|3'
        
        >>> test_html1 = '''<a href=""> <!-- VER: 1|2|3 --><!-- more comments -->'''
        >>> test_html2 = '''<a href=""><!-- VER: 1|2|3--><!--more comments-->'''
        >>> test_html3 = '''<a href=""><!--VER:1|2|3-->'''
        >>> Comment(r'<!--',r'-->').regex_ver.search(test_html1)['ver']
        '1|2|3'
        >>> Comment(r'<!--',r'-->').regex_ver.search(test_html2)['ver']
        '1|2|3'
        >>> Comment(r'<!--',r'-->').regex_ver.search(test_html3)['ver']
        '1|2|3'

        >>> test_css1 = '''   border-radius: 4px; /* VER:1|2|3 */  '''
        >>> Comment(r'/*','*/').regex_ver.search(test_css1)['ver']
        '1|2|3'

        """
        return re.compile(r'''(?P<ver_remove>{comment_start}\s*VER:\s*(?P<ver>.+?)\s*)($|{comment_end})'''.format(comment_start=re.escape(self.comment_start), comment_end=re.escape(self.comment_end or self.comment_start)), flags=re.IGNORECASE)

COMMENTS_STYLE_C = (Comment(r'//'), Comment(r'/*',r'*/'))
COMMENTS_STYLE_PYTHON = (Comment(r'#'),)

class Language(NamedTuple):
    name: str
    ext: Iterable[str]
    comments: Iterable[Comment]
LANGUAGES: MappingProxyType[str, Language] = MappingProxyType({
    language_ext: language 
    for language in map(lambda l: Language(*l), (
        ('python',('py',),COMMENTS_STYLE_PYTHON),
        ('javascript',('js',),COMMENTS_STYLE_C),
        ('html5/javascript',('html',),(Comment(r'<!--',r'-->'),)+COMMENTS_STYLE_C),
        ('java',('java',),COMMENTS_STYLE_C),
        ('visual basic',('vb',),(Comment(r"'"),)),
        ('php',('php'),COMMENTS_STYLE_PYTHON),
        ('c',('c',),COMMENTS_STYLE_C),
        ('c++',('cpp',),COMMENTS_STYLE_C),
        ('ruby',('rb',),COMMENTS_STYLE_PYTHON),
        ('csharp',('cs',),COMMENTS_STYLE_C),
        ('lua',('lua',),(Comment(r'--'),)),
        ('golang',('go',),COMMENTS_STYLE_C),
        # txt  =   '#',
    ))
    for language_ext in language.ext
})

class Version(str):
    pass

class VersionModel():
    r"""
    >>> java = io.StringIO(dedent('''
    ...     import java.util.stream.Collectors;             // VER: list_comprehension,dict_comprehension
    ...     import static java.util.Map.entry;              // VER: dict_comprehension
    ...     public class Java {
    ...         public static void main(String[] args) {new Java();}
    ...         public Java() {
    ...             hello_world();
    ...             arithmetic();
    ...         }
    ...         void hello_world() {
    ...             // // Must be in file named `HelloWorld.java`                    // VER: hello_world
    ...             //public class HelloWorld {                                      // VER: hello_world
    ...                 //public static void main(String[] args) {new HelloWorld();} // VER: hello_world
    ...                 //public HelloWorld() {                                      // VER: hello_world
    ...                     System.out.println("Hello World");                       // VER: hello_world
    ...                 //}                                                          // VER: hello_world
    ...             //}                                                              // VER: hello_world
    ...         }
    ...         void list_comprehension() {
    ...             List<Integer> data1 = new ArrayList<>(Arrays.asList(new Integer[]{1,2,3,4,5,6})); // VER: list_comprehension
    ...         }
    ...         void dict_comprehension() {
    ...             Map<String,Integer> data3 = Map.ofEntries(  //  VER: dict_comprehension
    ...                 entry("a", 1),                          //  VER: dict_comprehension
    ...                 entry("b", 2)                           //  VER: dict_comprehension
    ...             );                                          //  VER: dict_comprehension
    ...         }
    ...     }
    ... '''))
    >>> vm = VersionModel(java, LANGUAGES['java'])

    >>> vm.version.keys()
    {'list_comprehension', 'dict_comprehension', 'hello_world'}

    >>> vm.version['hello_world']
    '''// Must be in file named `HelloWorld.java`
    public class HelloWorld {
        public static void main(String[] args) {new HelloWorld();}
        public HelloWorld() {
            System.out.println("Hello World");
        }
    }

    >>> vm.version['list_comprehension']
    '''
    import java.util.stream.Collectors;
        List<Integer> data1 = new ArrayList<>(Arrays.asList(new Integer[]{1,2,3,4,5,6}));
    '''

    >>> vm.version['dict_comprehension']
    '''
    import java.util.stream.Collectors;
        Map<String,Integer> data3 = Map.ofEntries(
            entry("a", 1),
            entry("b", 2)
        );
    '''

    """

    @classmethod
    def from_path(cls: Self, path: str|Path) -> Self:
        path = Path(path)
        language = LANGUAGES.get(path.suffix.strip('.'))
        assert language, f'Language unknown: {path.suffix}. Valid languages are {LANGUAGES.keys()}'
        with path.open() as source:
            return cls(source, language)

    def __init__(self, source: io.IOBase, language: Language):
        self.language = language
        def parse_line(line: str) -> str:
            return line
        self.lines = tuple(map(parse_line, source))

    @cached_property
    def version(self) -> dict[str, str]:
        return MappingProxyType({})
