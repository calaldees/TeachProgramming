#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from functools import lru_cache

from .make_ver import make_ver

LANGUAGES = {
    'python.py',
    'javascript.js',
}

#from pprint import pprint
#data = make_ver('../static/language_reference/python.py', 'file_read', process_additional_metafiles=False)


import logging
log = logging.getLogger(__name__)

#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------

VERSION = "0.0"
DEFAULT_FUNCTION_LIST_FILENAME = '_function_order.txt'
DEFAULT_PATH = '../static/language_reference/'


#-------------------------------------------------------------------------------
# Generate
#-------------------------------------------------------------------------------

@lru_cache(maxsize=32)
def get_function_name_list(function_list_filename=DEFAULT_FUNCTION_LIST_FILENAME, default_path=DEFAULT_PATH, **kwargs):
    function_name_list = []
    function_list_filename_path = os.path.join(default_path, function_list_filename)
    log.info('Getting function_list: {0}'.format(function_list_filename_path))
    with open(function_list_filename_path, 'r') as f:
        for line in f:
            function_name_list.append(line)
    return function_name_list


def generate_language(language_filename, function_name_list, default_path=DEFAULT_PATH, **kwargs):
    log.info('Extracting version snippets for {0}'.format(language_filename))
    return {
        function_name: make_ver(os.path.join(default_path, language_filename), function_name, process_additional_metafiles=False)
        for function_name in function_name_list
    }


def generate_languages(languages=LANGUAGES, **kwargs):
    return {
        language_filename: generate_language(language_filename, get_function_name_list(**kwargs), **kwargs)
        for language_filename in languages
    }


#-------------------------------------------------------------------------------
# Command Line
#-------------------------------------------------------------------------------

def get_args():
    import argparse
    # Command line argument handling
    parser = argparse.ArgumentParser(
        description="""Generate Language Sheet""",
        epilog=""""""
    )
    parser.add_argument('-l', '--languages', nargs='*', help='list of languages to generate', choices=LANGUAGES|set(('all',)), default='all')
    parser.add_argument('-p', '--default_path', action='store', help='path', default=DEFAULT_PATH)
    parser.add_argument('--function_list_filename', action='store', help='filename functions', default=DEFAULT_FUNCTION_LIST_FILENAME)
    parser.add_argument('--log_level', default=logging.INFO, type=int)
    parser.add_argument('--version', action='version', version=VERSION)

    args = parser.parse_args()

    if 'all' in args.languages:
        args.languages = LANGUAGES

    return args


if __name__ == "__main__":
    args = get_args()
    logging.basicConfig(level=args.log_level)

    #args.languages = ('python.py', 'javascript.js')

    #log.info('Generating langauge sheet {0}'.format(args.languages))


    #pprint(languages)
