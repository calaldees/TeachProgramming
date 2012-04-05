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

def make_ver(source, target_versions, lang=None, hidden_line_replacement=None):
    """
    Doc required
    
    source - string filename or file object
    lang   - language to process (optional - will try to aquire from filename automatically)
    
    """
    try: # Can take an integer arg for target versions, under this case, make the sequential set
        target_versions = range(1,int(target_versions)+1)
    except:
        pass
    if isinstance(target_versions, basestring):
        target_versions = [ver.strip() for ver in target_version.split()]
    target_versions = set(target_versions)
    
    # Open source file if string - otherwise assume source is a file object
    if isinstance(source, basestring):
        source = open(source, 'r')
    # Setup comment_token for correct language
    if not lang:
        try:
            lang = get_fileext(source.name)
        except:
            pass
    if lang not in comment_tokens:
        raise Exception('lang %s is not supported' % lang)
    comment_token = comment_tokens[lang]

    # Regex compile
    extract_code          = re.compile(r'^(?P<line>(?P<indent>\s*)(?P<code>.*?))(%s|$)(?P<comment>.*)' % comment_token) 
    extract_ver           = re.compile(r'VER:\s*(?P<ver>.*?)(\s+|$)', flags=re.IGNORECASE)
    extract_hide          = re.compile(r'HIDE|HIDDEN'               , flags=re.IGNORECASE)
    extract_blank_comment = re.compile('\s*%s\s*$' % comment_token)
    
    #remmed_line = re.compile(r'^\s*%s' % comment_token)
    
    output = []
    # Process source file
    for line in source:
        # Extract meta data from line
        code_match = extract_code.match(line)
        
        # Get versions set
        try   : line_versions = set([ver.strip() for ver in extract_ver.search(code_match.group('comment')).group('ver').split(',')])
        except: line_versions = set(['1'])
        # Like with the input for target_versions - if a single integer is provided, make the version set based on a sequential range
        if len(line_versions)==1 and list(line_versions)[0].isdigit():
            line_versions = set(range(int(line_versions.pop()),10))
        
        # If is the version requested is a union with the current line
        if target_versions & line_versions:
            # Removed matched metadata
            line = extract_ver          .sub('', line)
            line = extract_hide         .sub('', line)
            line = extract_blank_comment.sub('', line)
            
            # If the line starts with a comment then remove that first comment
            # This is for lines that are not present and executed in the raw run of the file, but are interim steps
            #if remmed_line.match(line):
            #    line = re.sub(comment_token, '', line, count=1)
            
            try:
                if hidden_line_replacement and extract_hide.search(code_match.group('comment')):
                    line = code_match.group('indent') + comment_token + hidden_line_replacement
                    if hidden_line_replacement in output[-1]: # If the previous line was hidden then there is no need to repeat the '...'
                        line = None
            except:
                pass
            
            if line:
                output.append(line.rstrip())
    
    source.close()
    return output #"\n".join(output)


def get_diff(source, target_versions, prev_versions, lang=None, n=3, hidden_line_replacement=None):
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


get_diff_seq_prev_version = []
def get_diff_seq_clear():
    global get_diff_seq_prev_version
    get_diff_seq_prev_version = []
def get_diff_seq(source, target_versions, lang=None, n=3, hidden_line_replacement=None):
    """
    Rather than having to specity the target and previous versions every time,
    this method stores the previously generated version that was called and uses that as the previous version
    """
    global get_diff_seq_prev_version
    prev_version   = get_diff_seq_prev_version
    target_version = make_ver(source, target_versions, lang=lang, hidden_line_replacement=hidden_line_replacement)
    get_diff_seq_prev_version = target_version
    
    diff = []
    for line in difflib.unified_diff(prev_version, target_version, n=n):
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
    parser.add_argument('-v','--target_version', type=int                   , help='the target version', default=version_max) #default=argparse.SUPPRESS,
    return parser.parse_args()
    
if __name__ == "__main__":
    args = get_args()
    output = make_ver(args.source, args.target_version)
    if args.output:
        args.output.write(output)
        args.output.close()
    else:
        print(output)