import re
import difflib

# Normalize Python 3 vocab
# http://www.rfk.id.au/blog/entry/preparing-pyenchant-for-python-3/
try:
    unicode = unicode
except NameError:
    # 'unicode' is undefined, must be Python 3
    str = str
    unicode = str
    bytes = bytes
    basestring = (str,bytes)
else:
    # 'unicode' exists, must be Python 2
    str = str
    unicode = unicode
    bytes = str
    basestring = basestring



# Constants
version        = '0.1'
version_max    = 20
comment_tokens = dict(
    js   = r'//',
    html = r'//',
    py   =   '#',
    java = r'//',
    vb   =  '\'',
    php  =   '#',
)

def get_fileext(filename):
    return re.search(r'\.([^\.]+)$', filename).group(1).lower()
    
def get_ver_set(versions):
    if not versions:
        return set()
    # Can take an integer arg for target versions, under this case, make the sequential set
    try   : versions = [str(i) for i in range(1,int(versions)+1)]
    except: pass
    if isinstance(versions, basestring):
        versions = [ver.strip() for ver in versions.split(',')]
    return set(versions)

def make_ver(source, target_versions, lang=None, hidden_line_replacement=None, close_file_on_exit=False):
    """
    Doc required
    
    source - string filename or file object
    lang   - language to process (optional - will try to aquire from filename automatically)
    hidden_line_replacement - when line is removed with HIDE - it can be replaced with a placeholder
    close_file_on_exit - optional - not needed in any normal operation
    
    returns a list of strings - each line is an element
    
    cCc VER: item1,item2 NOT item3,item4
    HIDE - anywhere in line - removes whole line
    
    """
    output = []
    if not target_versions:
        return output
    target_versions = get_ver_set(target_versions)
    
    # Open source file if string - otherwise assume source is a file object
    if isinstance(source, basestring):
        source = open(source, 'r')
        close_file_on_exit = True
    # Setup comment_token for correct language
    if not lang:
        try:
            lang = get_fileext(source.name)
        except:
            pass
    if lang not in comment_tokens:
        raise Exception('lang %s is not supported' % lang)
    comment_token = comment_tokens[lang]
    
    # Regex compile - for this language based on comment_token
    extract_code          = re.compile(r'^(?P<line>(?P<indent>\s*)(?P<code>.*?))({0}|$)(?P<comment>.*)'.format(comment_token))
    extract_ver           = re.compile(r'VER:\s*(?P<ver>.*?)(\s+|$)(not\s*(?P<ver_exclude>.*?(\s+|$)))?', flags=re.IGNORECASE)
    extract_vername       = re.compile(r'VERNAME:\s*(?P<vername>.*?)(\s+|$)')
    extract_hide          = re.compile(r'HIDE')
    extract_blank_comment = re.compile('\s*{0}\s*$'.format(comment_token))
    remmed_line           = re.compile(r'^\s*{0}'.format(comment_token))
    

    # if source is a file object - double check we are ready for reading
    #  (this is handy when processing a single file multiple times)

    
    # preprocess vernames in file?
    # attempt vername extraction from .ver file companion?
    try   : source.seek(0)
    except: pass
    for line in source:
        vername_match = extract_vername.search(line)
        if vername_match:
            vername_match.group('vername')
            # todo - split by ',' and index under name

    try   : source.seek(0)
    except: pass    
    # Process source file
    for line in source:
        
        # Always remove all VERNAME lines
        vername_match = extract_vername.search(line)
        if vername_match:
            break # no need to process the line any further
        
        # Extract meta data from line
        code_match = extract_code.match(line)
        
        # Get current line versions set
        line_versions    = get_ver_set(1)
        exclude_versions = set()
        ver_match = extract_ver.search(code_match.group('comment'))
        if ver_match:
            line_versions    = get_ver_set(ver_match.group('ver'        ))
            exclude_versions = get_ver_set(ver_match.group('ver_exclude'))
        
        # If is the version requested is a union with the current line
        if line_versions & target_versions and not exclude_versions & target_versions:
            
            # Removed matched metadata
            line = extract_ver          .sub('' , line)
            line = extract_hide         .sub('' , line) # bug?: this is over zelus, HIDE anywhere in the line is removed, improve it chump!
            line = extract_blank_comment.sub(' ', line) # blank comments still need to represent a line (the \n gets rstiped later but at least it triggers an append)
            
            # If the line starts with a comment then remove that first comment
            # This is for lines that are not present and executed in the raw run of the file, but are interim steps in the overall progression
            if remmed_line.match(line):
                line = re.sub(comment_token, '', line, count=1)
            
            try:
                if hidden_line_replacement and extract_hide.search(code_match.group('comment')):
                    line = code_match.group('indent') + comment_token + hidden_line_replacement
                    if hidden_line_replacement in output[-1]: # If the previous line was hidden then there is no need to repeat the '...'
                        line = None
            except:
                pass
            
            if line:
                output.append(line.rstrip())
    
    # Tidy up - either close or reset file
    if close_file_on_exit:
        source.close()
    
    return output #"\n".join(output)


def get_diff(source, prev_versions, target_versions, lang=None, n=3, hidden_line_replacement=None):
    """
    n = number of lines of context
    """
    diff = []
    for line in difflib.unified_diff(
        make_ver(source, prev_versions  , lang=lang, hidden_line_replacement=hidden_line_replacement),
        make_ver(source, target_versions, lang=lang, hidden_line_replacement=hidden_line_replacement),
        n=n, ):
        diff.append(line)
    return diff
    

def get_args():
    import argparse
    # Command line argument handling
    parser = argparse.ArgumentParser(
        description="""
Takes code file returns version based on following syntax
stuff
    """,
        epilog="""
And that is how you version up!
    """
    )
    parser.add_argument('--version', action='version', version=version)
    parser.add_argument('source'               , type=argparse.FileType('r'), help='file to read')
    parser.add_argument('-o','--output'        , type=argparse.FileType('w'), help='File to output version too, if absent will output to STDIO') #default=argparse.SUPPRESS,
    parser.add_argument('-v','--target_version',                              help='the target version', default='1') #default=argparse.SUPPRESS,
    parser.add_argument('-d','--diff_version'  ,                              help='the target version diff only', default='1') #default=argparse.SUPPRESS,
    return parser.parse_args()
    
if __name__ == "__main__":
    args = get_args()
    if args.target_version:
        output = make_ver(args.source, args.target_version)
    if args.diff_version:
        target_versions = [ver.strip() for ver in args.diff_version.split(',')]
        prev_versions   = target_versions[:-1]
        output = get_diff(args.source, prev_versions, target_versions, n=2)
    if args.output:
        args.output.write(output)
        args.output.close()
    else:
        print('\n'.join(output))