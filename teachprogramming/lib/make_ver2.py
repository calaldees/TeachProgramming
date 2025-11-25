from types import MappingProxyType
from typing import NamedTuple, Iterable, Set, TypedDict, Sequence
from textwrap import dedent
from contextlib import contextmanager
from itertools import chain
from functools import cached_property, reduce, lru_cache, partial
from collections import defaultdict
from pathlib import Path
from difflib import unified_diff
import io
import re
import json
import operator
import inspect



def _json_dumps(obj):
    if isinstance(obj, (dict, MappingProxyType)):
        return dict(obj)
    if isinstance(obj, (set,frozenset)):
        return tuple(obj)
    return obj


@contextmanager
def _testfiles():
    import tempfile
    td = tempfile.TemporaryDirectory()
    files: Set[Path] = set()
    def write_file(filename, data):
        path = Path(td.name).joinpath(filename)
        with path.open('wt', encoding='utf8') as filehandle:
           _ = filehandle.write(data)
        files.add(path)
    write_file('test.py', dedent('''
        print('Hello Test')
        print('Hello World')  # VER: hello_world
    '''))
    write_file('test.js', dedent('''
        console.log("Hello World")    // VER: hello_world
        //console.log("Hello Test")    // VER: test4
    '''))
    write_file('Test.java', dedent('''
        public class Test {                          // VER: test1
            public Test() {                          // VER: test2
                System.out.println("Hello World");   // VER: hello_world
            }                                        // VER: test2
            public static void main(String[] args) {new Test();}  // VER: test2
        }  // VER: test1
    '''))
    write_file('test.ver.json', dedent('''
        {"versions": {
            "": {"parents": []},
            "test1": {"parents": [""]},
            "test2": {"parents": ["test1"]},
            "hello_world": {"parents": ["test2"]},
            "test4": {"parents": []}
        }}
    '''))
    #write_file('test.ver', dedent('''
    #    VERNAME: base           base
    #'''))
    yield files
    td.cleanup()



class Version(str):
    # TODO: this may need to support multiple sets
    # AND OR EXCLUDE HIDE
    pass
type VersionPath = frozenset[Version]


class VersionDescription(TypedDict):
    name: Version
    parent: Version
    mutations: None | Iterable[re.Pattern]  # TODO: Incomplete (previously replacements)
class _Versions(TypedDict):
    versions: MappingProxyType[Version, VersionDescription]

class Versions():
    """
    >>> data = {"versions": {
    ...     "": {"parents": []},
    ...     "background": {"parents": [""]},
    ...     "copter": {"parents": ["background"]},
    ...     "collision_single": {"parents": ["copter"]},
    ...     "collision_multi": {"parents": ["collision_single"]},
    ...     "level": {"parents": ["collision_single"]},
    ...     "physics": {"parents": ["collision_single"]},
    ...     "parallax": {"parents": ["level"]},
    ...     "full": {"parents": ["parallax", "physics", "collision_multi"]},
    ...     "fish": {
    ...         "parents": ["fish_background", "collision_single"],
    ...         "mutations": [
    ...             {"type": "replace", "match":"CopterLevel", "replacement":"FishLevel"},
    ...             {"type": "replace", "match":"ship.gif", "replacement":"fish.gif"}
    ...         ]
    ...     }
    ... }}
    >>> versions = Versions(data)
    >>> sorted(versions.resolve_versions(Version('full')))
    ['', 'background', 'collision_multi', 'collision_single', 'copter', 'full', 'level', 'parallax', 'physics']
    >>> sorted(versions.resolve_versions(Version('collision_single')))
    ['', 'background', 'collision_single', 'copter']

    >>> sorted(versions.paths['copter'])
    ['', 'background', 'copter']

    >>> versions.parents
    mappingproxy({'': None, 'background': '', 'copter': 'background', 'collision_single': 'copter', 'collision_multi': 'collision_single', 'level': 'collision_single', 'physics': 'collision_single', 'parallax': 'level', 'full': None, 'fish': None})

    >>> json_data = json.dumps(versions.paths, default=_json_dumps)
    """
    def __init__(self, versions: _Versions):
        self.versions = versions['versions']

    def resolve_versions(self, *versions: Iterable[Version]) -> VersionPath:
        versions_to_resolve = set(versions)
        versions_resolved = set()
        while versions_to_resolve and ((version := versions_to_resolve.pop()) is not None):
            target_version_description = self.versions.get(version)
            versions_resolved.add(version)
            if target_version_description:
                versions_to_resolve |= set(target_version_description['parents'])
                versions_to_resolve -= versions_resolved
        return frozenset(versions_resolved)

    @cached_property
    def paths(self) -> MappingProxyType[Version, VersionPath]:
        return MappingProxyType({
            version: self.resolve_versions(version)
            for version in self.versions.keys()
        })

    @cached_property
    def parents(self) -> MappingProxyType[Version, Version]:
        return MappingProxyType({
            version: version_data['parents'][0] if len(version_data.get('parents', tuple())) == 1 else None
            for version, version_data in self.versions.items()
        })

class LanguageFileExtension(str):
    pass

class Comment(NamedTuple):
    start: str
    end: str = ''

COMMENTS_STYLE_C = (Comment(r'/*',r'*/'), Comment(r'//'))
COMMENTS_STYLE_PYTHON = (Comment(r'#'),)

class Language(NamedTuple):
    name: str
    ext: Iterable[LanguageFileExtension]
    comments: Iterable[Comment]
LANGUAGES: MappingProxyType[LanguageFileExtension, Language] = MappingProxyType({
    language_ext: language
    for language in map(lambda l: Language(*l), (
        ('python',('py',),COMMENTS_STYLE_PYTHON),
        ('javascript',('js',),COMMENTS_STYLE_C),
        ('html5/javascript',('html',),(Comment(r'<!--',r'-->'),)+COMMENTS_STYLE_C),
        ('java',('java',),COMMENTS_STYLE_C),
        ('visual basic',('vb',),(Comment(r"'"),)),
        ('php',('php',),COMMENTS_STYLE_PYTHON),
        ('c',('c',),COMMENTS_STYLE_C),
        ('c++',('cpp',),COMMENTS_STYLE_C),
        ('ruby',('rb',),COMMENTS_STYLE_PYTHON),
        ('csharp',('cs',),COMMENTS_STYLE_C),
        ('lua',('lua',),(Comment(r'--'),)),
        ('golang',('go',),COMMENTS_STYLE_C),
        ('rust',('rs',),COMMENTS_STYLE_C),
        # txt  =   '#',
    ))
    for language_ext in language.ext
})


class VersionEvaluator():
    """
    TODO: HIDE (replace with '???') NOT?

    >>> VersionEvaluator('collision_single')(frozenset(('base','collision_single','parallax')))
    True
    >>> VersionEvaluator('collision_single parallax NOT_ AND_')(frozenset(('base','collision_single')))
    True
    >>> VersionEvaluator('collision_single parallax NOT_ AND_')(frozenset(('base','collision_single','parallax')))
    False

    >>> VersionEvaluator('block_move mines OR_')(frozenset(('base',)))
    False
    >>> VersionEvaluator('block_move mines OR_')(frozenset(('base','block_move')))
    True
    >>> VersionEvaluator('block_move mines OR_')(frozenset(('base','mines')))
    True
    """
    def __init__(self, version_str: str = ''):
        version_str = version_str.replace(',',' ')
        self.tokens = tuple(filter(None, map(lambda v: v.strip(), version_str.split(' ')))) or ('',)
        # !!! WIP TEMP HACKs: to allow migration from old `make_ver` !!! REMOVE THIS SHIT!
        self.tokens = tuple(t for t in self.tokens if t.lower()!='hide')
        if len(self.tokens) == 3 and self.tokens[1].lower() == 'not':
            self.tokens = (self.tokens[0], self.tokens[2], 'NOT_', 'AND_')
        if len(self.tokens) == 4 and self.tokens[1].lower() == 'not':
            self.tokens = (self.tokens[0], self.tokens[2], 'NOT_', self.tokens[3], 'NOT_', 'OR_', 'AND_')  # probably a ballzup
        if len(self.tokens) == 2 and 'list_comprehension' not in self.tokens and 'AND_' not in self.tokens and 'NOT_' not in self.tokens and 'OR_' not in self.tokens:
                self.tokens = self.tokens + ('AND_',)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tokens=})"

    def __call__(self, version_path: VersionPath) -> bool:
        if not version_path:
            return False
        stack = []
        for token in self.tokens:
            if _operator := getattr(operator, token.lower(), None):
                param_count = len(inspect.signature(_operator).parameters)
                try:
                    result = _operator(*(stack.pop() for i in range(param_count)))
                except IndexError:
                    raise Exception(f'{self.__class__.__name__} Out of tokens {self.tokens=} {version_path=}')
                stack.append(result)
            else:
                stack.append(token in version_path)
        assert len(stack) == 1, f"After evaluation of version_path, we should have a single value {self.tokens=} {version_path=}"
        return stack.pop()

    @cached_property
    def versions(self) -> VersionPath:
        return frozenset(token for token in self.tokens if not hasattr(operator, token))

class VersionModel():

    class Line(NamedTuple):
        line: str
        line_without_ver: str
        version_evaluator: VersionEvaluator

    @staticmethod
    @lru_cache
    def regex_ver(comment: Comment) -> re.Pattern:
        """
        >>> regex_ver = VersionModel.regex_ver

        >>> c = Comment(r'#')
        >>> test_py1 = '''print('helloworld') # VER: 1|2|3 # More comments'''
        >>> test_py2 = '''print('helloworld') # VER: 1|2|3#More comments'''
        >>> test_py3 = '''print('helloworld') #VER:1|2|3'''
        >>> regex_ver(c).search(test_py1)['ver']
        '1|2|3'
        >>> regex_ver(c).search(test_py2)['ver']
        '1|2|3'
        >>> regex_ver(c).search(test_py3)['ver']
        '1|2|3'

        >>> c = Comment(r'//')
        >>> test_js1 = '''console.log('helloworld') // VER: 1|2|3 // More comments'''
        >>> test_js2 = '''console.log('helloworld') // VER: 1|2|3//More comments'''
        >>> test_js3 = '''console.log('helloworld') //VER:1|2|3'''
        >>> regex_ver(c).search(test_js1)['ver']
        '1|2|3'
        >>> regex_ver(c).search(test_js2)['ver']
        '1|2|3'
        >>> regex_ver(c).search(test_js3)['ver']
        '1|2|3'

        >>> c = Comment(r'<!--',r'-->')
        >>> test_html1 = '''<a href=""> <!-- VER: 1|2|3 --><!-- more comments -->'''
        >>> test_html2 = '''<a href=""><!-- VER: 1|2|3--><!--more comments-->'''
        >>> test_html3 = '''<a href=""><!--VER:1|2|3-->'''
        >>> regex_ver(c).search(test_html1)['ver']
        '1|2|3'
        >>> regex_ver(c).search(test_html2)['ver']
        '1|2|3'
        >>> regex_ver(c).search(test_html3)['ver']
        '1|2|3'

        >>> c = Comment(r'/*','*/')
        >>> test_css1 = '''   border-radius: 4px; /* VER:1|2|3 */  '''
        >>> regex_ver(c).search(test_css1)['ver']
        '1|2|3'
        """
        return re.compile(
            r'''(?P<ver_remove>{comment_start}\s*VER:\s*(?P<ver>.+?)\s*)($|{comment_end})'''.format(
                comment_start=re.escape(comment.start),
                comment_end=re.escape(comment.end or comment.start)
            ), flags=re.IGNORECASE)

    @staticmethod
    @lru_cache
    def _regex_first_line_comment(comment) -> re.Pattern:
        """
        """
        return re.compile(
            r'''^(\s*){comment_start}\s*(.*)'''.format(
                comment_start=re.escape(comment.start)
            ), flags=re.IGNORECASE)
    @classmethod
    def _remove_first_line_comment(cls, line, comment):
        """
        >>> VersionModel._remove_first_line_comment('    #  x=x+1', Comment('#'))
        '    x=x+1'
        >>> VersionModel._remove_first_line_comment('    ## Real comment # Again', Comment('#'))
        '    # Real comment # Again'
        """
        return cls._regex_first_line_comment(comment).sub(r'\1\2', line, count=1)

    @staticmethod
    def remove_new_lines(line):
        return re.sub('[\n\r]', '', line)

    @classmethod
    def _parse_line(cls, language: Language, line: str) -> Line:
        r"""
        >>> VersionModel._parse_line(LANGUAGES['py'], "    print('Hello World')  #  VER:  test1 test2 AND_\n\r")
        Line(line="    print('Hello World')  #  VER:  test1 test2 AND_", line_without_ver="    print('Hello World')", version_evaluator=VersionEvaluator(self.tokens=('test1', 'test2', 'AND_')))
        """
        #print(f'_parse_line {language.name} {line[:10]}')
        line = cls.remove_new_lines(line)
        for comment in language.comments:
            if match := cls.regex_ver(comment).search(line):
                line_without_ver = line.replace(match['ver_remove'], '').rstrip()
                line_without_ver = cls._remove_first_line_comment(line_without_ver, comment)
                return cls.Line(
                    line=line,
                    line_without_ver=line_without_ver,
                    version_evaluator=VersionEvaluator(match['ver'])
                )
        return cls.Line(
            line=line,
            line_without_ver=line,
            version_evaluator=VersionEvaluator()
        )

    def __init__(self, source: io.IOBase, language: Language):
        self.lines = tuple(map(partial(self._parse_line, language), source))

class ProjectVersions():
    r"""
    Read in a project and have all permutations of that project in an object

    >>> with _testfiles() as files:
    ...     p = ProjectVersions(files)

    >>> sorted(p.versions.paths['hello_world'])
    ['', 'hello_world', 'test1', 'test2']

    >>> print(p.languages['java']['test2'])
    <BLANKLINE>
    public class Test {
        public Test() {
        }
        public static void main(String[] args) {new Test();}
    }

    >>> print(p.diffs['java']['test2'])
    --- test1
    +++ test2
    @@ -1,3 +1,6 @@
    <BLANKLINE>
     public class Test {
    +    public Test() {
    +    }
    +    public static void main(String[] args) {new Test();}
     }
    """
    class StemExt(NamedTuple):
        stem: str
        ext: LanguageFileExtension
        def __str__(self) -> str:
            return f'{self.ext}: {self.stem}'
    def __init__(self, files):
        self.files_by_stem_ext = MappingProxyType({
            self.StemExt(
                f.stem,
                LanguageFileExtension(''.join(f.suffixes).strip('.'))
            ): f.open(encoding='utf8').read()
            for f in files
        })

    @property
    def _titles(self) -> frozenset[StemExt]:
        EXCLUDE_EXTS = frozenset(('ver', 'json', 'yaml', 'yml', 'ver.json'))
        return frozenset(
            stem_ext
            for stem_ext in self.files_by_stem_ext.keys()
            if stem_ext.ext not in EXCLUDE_EXTS
        )

    @property
    def titles_to_language_mapping(self) -> dict[str, str]:
        return {str(s): s.ext for s in self._titles}

    @cached_property
    def versions(self) -> Versions:
        """
        Parse versions from .ver or .yaml file
        """
        file_exts = frozenset(s.ext for s in self.files_by_stem_ext.keys())
        if {'yaml', 'yml'} & file_exts:
            raise NotImplementedError('yaml version file format not implemented')
        if {'ver.json',} & file_exts:
            return Versions(_Versions(json.loads(next(iter(f for s, f in self.files_by_stem_ext.items() if s.ext == 'ver.json')))))
        raise Exception('no version information')

    def full(self, title: StemExt) -> MappingProxyType[Version, str]:
        lines = VersionModel(io.StringIO(self.files_by_stem_ext[title]), LANGUAGES[title.ext]).lines
        return MappingProxyType({
            version_name: '\n'.join(
                line.line_without_ver
                for line in lines
                if line.version_evaluator(version_path)
            )
            for version_name, version_path in self.versions.paths.items()
        })

    @cached_property
    def full_per_version(self) -> MappingProxyType[str, MappingProxyType[Version, str]]:
        return MappingProxyType({str(l): self.full(l) for l in self._titles})

    def diff(self, title: StemExt) -> MappingProxyType[Version, str]:
        return MappingProxyType({
            version: "\n".join(unified_diff(
                self.full(title)[parent].split("\n"),
                self.full(title)[version].split("\n"),
                fromfile=parent, tofile=version, n=2, lineterm=''))
            for version, parent in self.versions.parents.items()
            if parent is not None
        })

    @cached_property
    def diff_per_version(self) -> MappingProxyType[str, MappingProxyType[Version, str]]:
        return MappingProxyType({str(l): self.diff(l) for l in self._titles})



class LanguageVersions():
    r"""

    >>> with _testfiles() as files:
    ...     l = LanguageVersions(files)

    `hello_world` is in the VERSION_ORDER and so will come first, then the rest are then ordered
    >>> l.all_versions
    ('hello_world', 'test1', 'test2', 'test4')
    >>> l.languages['js']['test4']
    'console.log("Hello Test")'
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

    def __init__(self, files: Iterable[Path]):
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
        def _amalgamate_files_with_same_extension(acc, path):
            acc[''.join(path.suffixes).strip('.')].append(path.read_text('utf-8'))
            return acc
        self.files = MappingProxyType({
            ext: "\n".join(file_content_list)
            for ext, file_content_list in reduce(
                _amalgamate_files_with_same_extension,
                files,
                defaultdict(list),
            ).items()
        })

    @property
    def all_versions(self) -> Sequence[Version]:
        versions = frozenset(chain.from_iterable(version_data.keys() for version_data in self.languages.values()))
        return tuple(v for v in self.VERSION_ORDER if v in versions) + tuple(sorted(v for v in versions if v not in self.VERSION_ORDER))

    @cached_property
    def languages(self) ->  MappingProxyType[str, MappingProxyType[Version, str]]:
        return MappingProxyType({
            language: self._build_versions(io.StringIO(self.files.get(language)), LANGUAGES[language])
            for language in LANGUAGES.keys()
        })

    @classmethod
    def _build_versions(cls, source: io.IOBase, language: Language) -> MappingProxyType[Version, str]:
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
        >>> versions = LanguageVersions._build_versions(java, LANGUAGES['java'])

        >>> sorted(versions.keys())
        ['dict_comprehension', 'hello_world', 'list_comprehension']

        >>> print(versions['hello_world'])
                // Must be in file named `HelloWorld.java`
                public class HelloWorld {
                    public static void main(String[] args) {new HelloWorld();}
                    public HelloWorld() {
                        System.out.println("Hello World");
                    }
                }

        >>> print(versions['list_comprehension'])
        import java.util.stream.Collectors;
                List<Integer> data1 = new ArrayList<>(Arrays.asList(new Integer[]{1,2,3,4,5,6}));

        >>> print(versions['dict_comprehension'])
        import java.util.stream.Collectors;
        import static java.util.Map.entry;
                Map<String,Integer> data3 = Map.ofEntries(
                    entry("a", 1),
                    entry("b", 2)
                );
        """
        lines = VersionModel(source, language).lines
        # We build a dict incrementally with the versions from each line.
        # This is not the way ProjectVersions works.
        # Perhaps we can get a list of all versions and then run the version evaluator for each line to include it?
        # The process below is definitely efficient to build, but I wonder if a single code path for versions would be neater and cleaner
        # For now LanguageVersions feels like it's own case, but it feels weird because `VER:` lines are used for different things in different ways
        def _reducer(acc: defaultdict[Version, list[str]], line: VersionModel.Line) -> defaultdict[Version, list[str]]:
            for version in line.version_evaluator.versions:
                if not version:  # Lines with not explicitly tagged with a version are not considered in LanguageVersions
                    continue
                acc[version].append(line.line_without_ver)
            return acc
        return MappingProxyType({
            version: "\n".join(lines)
            for version, lines in reduce(_reducer, lines, defaultdict(list[str])).items()
        })

    # @classmethod
    # def build_versions_from_path(cls: Self, path: str | Path) -> MappingProxyType[Version, str]:
    #     path = Path(path)
    #     language = LANGUAGES.get(path.suffix.strip('.'))
    #     assert language, f'Language unknown: {path.suffix}. Valid languages are {LANGUAGES.keys()}'
    #     with path.open() as source:
    #         return cls._build_versions(source, language)
