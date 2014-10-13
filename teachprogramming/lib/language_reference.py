#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from make_ver import make_ver


from pprint import pprint
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

def get_function_name_list(function_list_filename=DEFAULT_FUNCTION_LIST_FILENAME):
    function_name_list = []
    with open(os.path.join(DEFAULT_PATH, function_list_filename), 'r') as f:
        for line in f:
            function_name_list.append(line)
    return function_name_list


def generate_language(language_filename, function_name_list):
    return {
        function_name: make_ver(os.path.join(DEFAULT_PATH, language_filename), function_name, process_additional_metafiles=False)
        for function_name in function_name_list
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
    parser.add_argument('--function_list_filename', action='store', help='filename functions', default=DEFAULT_FUNCTION_LIST_FILENAME)
    parser.add_argument('--log_level', default=logging.INFO, type=int)
    parser.add_argument('--version', action='version', version=VERSION)

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = get_args()
    logging.basicConfig(level=args.log_level)

    args.languages = ('python.py', 'javascript.js')

    log.info('Generating langauge sheet {0}'.format(args.languages))

    function_name_list = get_function_name_list()
    languages = {}
    for language_filename in args.languages:
        languages[language_filename] = generate_language(language_filename, function_name_list)

    pprint(languages)
