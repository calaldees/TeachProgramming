#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import subprocess
import copy
from functools import wraps

import logging
log = logging.getLogger(__name__)


#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------

VERSION = "0.0"

CMD_RUN_LANGUAGE_SCRIPT = """make {language}"""

LANGAUGES = {
    'python',
    'javascript',
    'php',
    'ruby',
    'java',
    'vb',
}


#-------------------------------------------------------------------------------
# Variables
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Generate
#-------------------------------------------------------------------------------

def generate_sheet(languages=LANGAUGES):
    data = {}
    for language in languages:
        output = subprocess.Popen(
            CMD_RUN_LANGUAGE_SCRIPT.format(language=language),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        ).stdout.read()
        data[language] = output
    return data


#-------------------------------------------------------------------------------
# Command Line
#-------------------------------------------------------------------------------

def get_args():
    import argparse
    # Command line argument handling
    parser = argparse.ArgumentParser(
        description="""Import media to local Db""",
        epilog=""""""
    )
    parser.add_argument('-l', '--languages', nargs='*', help='list of languages to generate', choices=LANGAUGES|set(('all',)), default='all')
    parser.add_argument('--log_level', default=logging.INFO, type=int)
    parser.add_argument('--version', action='version', version=VERSION)

    args = parser.parse_args()

    if 'all' in args.languages:
        args.languages = LANGAUGES

    return args


if __name__ == "__main__":
    args = get_args()

    logging.basicConfig(level=args.log_level)

    log.info('Creating sheet {0}'.format(args.languages))
    data = generate_sheet(languages=args.languages)

    from pprint import pprint
    pprint(data)
