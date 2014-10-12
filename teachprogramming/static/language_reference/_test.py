#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import subprocess
from collections import defaultdict

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

DEFAULT_SCRIPT_HEADER_IDENTIFYER = '-(.*)-'
DEFAULT_SCRIPT_HEADER_IDENTIFYER_REGEX = re.compile(DEFAULT_SCRIPT_HEADER_IDENTIFYER)
DEFAULT_EXPECTED_OUTPUT_FILENAME = '_expected_output.txt'

#-------------------------------------------------------------------------------
# Variables
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Generate
#-------------------------------------------------------------------------------

def parse_langauge_output(text, header_identifyer=DEFAULT_SCRIPT_HEADER_IDENTIFYER_REGEX, **kwargs):
    """
    Take the full console output of a language run
    Iterate through each line looking for a heading identifyer (to use as the dict key)
    Index the output snippets under the correct heading/dict key

    Any lines read before the first heading is identifyed are placed under the 'None'
    key and are ignored in comparisons yet still avalable for debugging
    """
    data = defaultdict(list)
    current_heading = None
    for line in text.split('\n'):
        match = header_identifyer.match(line)
        if match and match.group(1):
            current_heading = match.group(1)
        else:
            data[current_heading].append(line)
    return {k: '\n'.join(v) for k, v in data.items()}


def get_expected_output_dict(expected_output_filename=DEFAULT_EXPECTED_OUTPUT_FILENAME, **kwargs):
    with open(expected_output_filename, 'r') as f:
        return parse_langauge_output(f.read())


def test_language(language, expected_output_dict, **kwargs):
    """
    Given a language string
    Run the corresponding Makefile target and capture the output
    Parse the output into a dict
    Compare the parsed grouped output with the expected output and log differences
    """
    test_log = {}

    # Run the language script and capture output
    output = subprocess.Popen(
        CMD_RUN_LANGUAGE_SCRIPT.format(language=language),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ).stdout.read()

    # Parse the captured output into a dict
    language_output = parse_langauge_output(output, **kwargs)

    # Compare expected output with parsed captured output
    # Raise assertions on differences
    for function_name, expected_output_text in expected_output_dict.items():
        language_output_text = language_output.get(function_name)
        single_line = lambda text: '^'.join((text or '').split('\n'))
        try:
            assert expected_output_text == language_output_text, '{0}:{1}: {2} != {3}'.format(language, function_name, single_line(expected_output_text), single_line(language_output_text))
            log.info('{0}:{1}: ok'.format(language, function_name))
        except AssertionError as ae:
            log.warn(ae)
            test_log[function_name] = ae

    return test_log


def test_langauges(languages=LANGAUGES, **kwargs):
    """
    Given a list of languages to test for correct operation
    Load and parse the expected_output
    Iterate through the languages
    """
    expected_output_dict = get_expected_output_dict(**kwargs)
    test_log = {}
    for language in languages:
        test_log[language] = test_language(language, expected_output_dict, **kwargs)
    return test_log


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
    parser.add_argument('--header_identifyer', action='store', help='regex to identify sections titles', default=DEFAULT_SCRIPT_HEADER_IDENTIFYER)
    parser.add_argument('--expected_output_filename', action='store', help='filename of expected output', default=DEFAULT_EXPECTED_OUTPUT_FILENAME)
    parser.add_argument('--log_level', default=logging.INFO, type=int)
    parser.add_argument('--version', action='version', version=VERSION)

    args = parser.parse_args()

    if 'all' in args.languages:
        args.languages = LANGAUGES
    args.header_identifyer = re.compile(args.header_identifyer)

    return args


if __name__ == "__main__":
    args = get_args()

    logging.basicConfig(level=args.log_level)

    log.info('Testing langauge output {0}'.format(args.languages))
    test_langauges(**vars(args))

