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
    # Can take an integer arg for target versions, under this case, make the sequential set
    try   : versions = [str(i) for i in range(1,int(versions)+1)]
    except: pass
    if isinstance(versions, basestring):
        versions = [ver.strip() for ver in versions.split(',')]
    return set(versions)

def make_ver(source, target_versions, lang=None, hidden_line_replacement=None):
    """
    Doc required
    
    source - string filename or file object
    lang   - language to process (optional - will try to aquire from filename automatically)
    
    """
    output = []
    if not target_versions:
        return output
    target_versions = get_ver_set(target_versions)
    
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

    remmed_line = re.compile(r'^\s*%s' % comment_token)

    #extract_vername       = re.compile(r'VERNAME:\s*(?P<vername>.*?)\s+(?P<verpath>.*?)(\s+|$)', flags=re.IGNORECASE)    
    # Pre process the source file trying to find a target_version path match
    #if len(target_versions)==1:
    #    for line in source:
    #        vername_match = extract_vername.search(line)
    #        if vername_match and vername_match.group('vername') == list(target_versions)[0]:
    #            target_versions = get_ver_set(vername_match.group('verpath'))
    #    if hasattr(source, 'seek'):
    #        source.seek(0)
    
    # Process source file
    for line in source:
        
        # Extract meta data from line
        code_match = extract_code.match(line)
        
        # Get current line versions set
        try   : line_versions = get_ver_set(extract_ver.search(code_match.group('comment')).group('ver'))
        except: line_versions = get_ver_set(1)
        
        #vername_match = extract_vername.search(line)
        #if vername_match:
        #    line = '' # Always remove all VERNAME lines
        
        # If is the version requested is a union with the current line
        if line_versions <= target_versions:
            
            # Removed matched metadata
            line = extract_ver          .sub('' , line)
            line = extract_hide         .sub('' , line)
            line = extract_blank_comment.sub(' ', line) # blank comments still need to represent a line (the \n gets rstiped later but at least it triggers an append)
            
            # If the line starts with a comment then remove that first comment
            # This is for lines that are not present and executed in the raw run of the file, but are interim steps
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