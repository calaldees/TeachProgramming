import re
from itertools import chain
from functools import cached_property, reduce, lru_cache, partial
from collections import defaultdict
from pathlib import Path
from types import MappingProxyType
from contextlib import contextmanager
import io
from textwrap import dedent
from typing import NamedTuple, Iterable, Set, TypedDict, Sequence
import json


from make_ver import make_ver


class Version(str):
    # TODO: this may need to support multiple sets
    # AND OR EXCLUDE HIDE
    pass
type VersionPath = frozenset[Version]

### KILL THESE!!!

def parse_legacy_version_data(data) -> MappingProxyType[Version, VersionPath]:
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

def load_version_data(source: io.IOBase):
    data = json.load(source)

### END KILL


class VersionDescription(TypedDict):
    name: Version
    parent: Version
    mutations: None | Iterable[re.Pattern]  # TODO: Incomplete (previously replacements)
class _Versions(TypedDict):
    versions: MappingProxyType[Version, VersionDescription]

class Versions():
    """
    >>> data = {"versions": {
    ...     "base": {"parents": []},
    ...     "background": {"parents": ["base"]},
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
    ['background', 'base', 'collision_multi', 'collision_single', 'copter', 'full', 'level', 'parallax', 'physics']
    >>> sorted(versions.resolve_versions(Version('collision_single')))
    ['background', 'base', 'collision_single', 'copter']

    >>> sorted(versions.version_paths['copter'])
    ['background', 'base', 'copter']
    """
    def __init__(self, versions: _Versions):
        self.versions = versions['versions']

    def resolve_versions(self, *versions: Iterable[Version]) -> VersionPath:
        versions_to_resolve = set(versions)
        versions_resolved = set()
        while versions_to_resolve and (version := versions_to_resolve.pop()):
            target_version_description = self.versions.get(version)
            versions_resolved.add(version)
            if target_version_description:
                versions_to_resolve |= set(target_version_description['parents'])
                versions_to_resolve -= versions_resolved
        return frozenset(versions_resolved)

    @cached_property
    def version_paths(self) -> MappingProxyType[Version, VersionPath]:
        return MappingProxyType({
            version: self.resolve_versions(version)
            for version in self.versions.keys()
        })

class LanguageFileExtension(str):
    pass

class Comment(NamedTuple):
    start: str
    end: str = ''

COMMENTS_STYLE_C = (Comment(r'//'), Comment(r'/*',r'*/'))
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
        # txt  =   '#',
    ))
    for language_ext in language.ext
})


class VersionEvaluator():
    """
    TODO: HIDE (replace with '???') NOT?
    'block_move,mines' AND, OR

    if variables.player2_x_pos<=0                  : variables.player2_x_pos = screen.get_width() -1 # VER: player2,wrap

    var g = variables.grid;                                               // VER: block_move,mines   OR?
            //if (block_name!=undefined) {                                // VER: blocks not images,mines

    //v.background_image = new Image();                   // VER: background NOT level,parallax

    //collisions_context.drawImage(v.background_image, -v.view_x_pos, 0);  // VER: collision_single NOT parallax
    collisions_context.drawImage(v.background_images[0], -v.view_x_pos, 0);  // VER: collision_single,parallax    AND?

    if self.keys[pygame.K_LEFT ]: self.copter_x_vel += -0.1 # VER: physics HIDE
    if self.keys[pygame.K_RIGHT]: self.copter_x_vel +=  0.1 # VER: physics HIDE
    """
    def __init__(self, version_str: str = ''):
        # TODO: could be property of version from evaluator
        self.versions: VersionPath = frozenset((Version(v.strip()) for v in version_str.split(',')))

    def __call__(self, version_path: VersionPath) -> bool:
        return any(version in self.versions for version in version_path)

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

    @classmethod
    def _parse_line(cls, language: Language, line: str) -> Line:
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
    write_file('test.json', dedent('''
        {"versions": {
            "base": {"parents": []}
        }}
    '''))
    #write_file('test.ver', dedent('''
    #    VERNAME: base           base
    #'''))
    yield files
    td.cleanup()

class ProjectVersions():
    r"""
    TODO: REFACTOR FOR make_ver2 -> deprecate make_ver

    Read in a project and have all permutations of that project in an object

    >>> with _testfiles() as files:
    ...     p = ProjectVersions(files)

    >>> p.versions['base']
    frozenset({'base'})

    #>>> p.data['py']['base']
    #"\nprint('Hello World')"
    """
    def __init__(self, files):
        self.files_by_ext = MappingProxyType({
            LanguageFileExtension(f.suffix.strip('.')): f.open(encoding='utf8').read()
            for f in files
        })
        self.data  # generate cache on object creation

    @property
    def languages(self) -> frozenset[LanguageFileExtension]:
        return frozenset(self.files_by_ext.keys()) - frozenset(('ver', 'json', 'yaml', 'yml'))

    @cached_property
    def versions(self) -> MappingProxyType[Version, VersionPath]:
        """
        Parse versions from .ver or .yaml file
        """
        file_exts = frozenset(self.files_by_ext.keys())
        if {'yaml', 'yml'} & file_exts:
            raise NotImplementedError('yaml version file format not implemented')
        if {'ver',} & file_exts:
            return parse_legacy_version_data(self.files_by_ext['ver'])
        if {'json',} & file_exts:
            return Versions(_Versions(json.loads(self.files_by_ext['json']))).version_paths
        raise Exception('no version information')

    #@lru_cache?
    def language(self, language: LanguageFileExtension) -> MappingProxyType[Version, str]:
        return MappingProxyType({
            ver_name: '\n'.join(
                make_ver(
                    io.StringIO(self.files_by_ext[language]),
                    ver_path=ver_path,
                    lang=language,
                    process_additional_metafiles=False,
                )
            )
            for ver_name, ver_path in self.versions.items()
        })

    @cached_property
    def data(self) -> MappingProxyType[LanguageFileExtension, MappingProxyType[Version, str]]:
        return MappingProxyType({l: self.language(l) for l in self.languages})



class LanguageVersions():
    r"""

    >>> with _testfiles() as files:
    ...     l = LanguageVersions(files)

    `hello_world` is in the VERSION_ORDER and so will come first, then the rest are then ordered
    >>> l.all_versions
    ('hello_world', 'test1', 'test2', 'test4')
    >>> l.languages['py']['test4']
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
            acc[path.suffix.strip('.')].append(path.read_text('utf-8'))
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
