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
version        = '0.0'
version_max    = 100
version_min    =   1
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

def make_ver(source, target_version=version_max, lang=None):
    """
    Doc required
    
    source - string filename or file object
    lang   - language to process (optional - will try to aquire from filename automatically)
    
    """
    #if not target_version:
    #    target_version = 
    target_version = int(target_version)
    
    
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
    extract_ver = re.compile(r'(?P<code>.*)%s(.*?)Ver:\s*(?P<ver>\d\d?)(?:\s*to\s*(?P<ver_limit>\d\d?))?' % comment_token)
    remmed_line = re.compile(r'^\s*%s' % comment_token)
    
    output = []
    # Process source file
    for line in source:
        # Extract version numbers from line
        ver_match = extract_ver.match(line)
        try   : line_version       = int(ver_match.group('ver')      )
        except: line_version       = version_min
        try   : line_version_limit = int(ver_match.group('ver_limit'))
        except: line_version_limit = version_max
        
        # If lines version number in range or target version to be generated, print code
        if line_version <= target_version and target_version <= line_version_limit:
            try:
                line = ver_match.group('code')
                if remmed_line.match(line):
                    line = re.sub(comment_token, '', line, count=1)
            except: 
                pass
            #print(line.rstrip())
            output.append(line.rstrip())
    
    source.close()
    return output #"\n".join(output)


def get_diff(source, version, version_from=None, lang=None, n=2):
    """
    n = number of lines of context
    """
    diff = []
    if not version_from:
        version_from = version - 1
    for line in difflib.unified_diff(
        make_ver(source, version_from, lang=lang),
        make_ver(source, version     , lang=lang),
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