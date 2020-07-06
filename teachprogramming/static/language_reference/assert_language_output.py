#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re
import subprocess
from functools import reduce

#import shutil
#shutil.get_terminal_size((80, 20))  # pass fallback
#os.terminal_size(columns=87, lines=23)  # returns a named-tuple

import logging
log = logging.getLogger(__name__)


#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------

VERSION = "0.0"
LANGUAGES = set(os.listdir('languages'))


#-------------------------------------------------------------------------------
# Generate
#-------------------------------------------------------------------------------

def parse_langauge_output(text):
    r"""
    >>> text = '''
    ... - heading1 -------------------
    ... 1
    ... 2
    ...
    ... --heading2--
    ... a
    ...     b
    ...          c
    ...
    ... '''
    >>> parse_langauge_output(text)
    {'heading1': ('1', '2'), 'heading2': ('a', 'b', 'c')}
    """
    def reducer(data, match):
        function, output = match.groups()
        data[function] = tuple(line.strip() for line in output.split('\n'))
        return data
    return reduce(
        reducer,
        re.finditer(r'^-+\s*(?P<function>\w+)\s*-+\n(?P<output>.+?)\n\n', text, flags=re.MULTILINE + re.DOTALL),
        {},
    )


def run_language_and_capture_output(language):
    """
    >>> run_language_and_capture_output('__fake_assert_target')
    '# unittest\\n'
    """
    return subprocess.Popen(
        f"""make {language}""",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ).stdout.read().decode('utf8')


def assert_language(language, expected_output_dict, **kwargs):
    """
    Given a language string
    Run the corresponding Makefile target and capture the output
    Parse the output into a dict
    Compare the parsed grouped output with the expected output and log differences
    """
    log.info(f'Running {language}')
    test_log = {}

    output = run_language_and_capture_output(language)

    # Parse the captured output into a dict
    language_output = parse_langauge_output(output)

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


def assert_langauges(expected_output_dict, languages=LANGUAGES, **kwargs):
    """
    Given a list of languages to test for correct operation
    Load and parse the expected_output
    Iterate through the languages
    """
    log.info(f'{languages=}')
    for language in languages:
        assert_language(language, expected_output_dict, **kwargs)
    sys.exit(1)  # TODO: exit code should reflect if any languages fail


#-------------------------------------------------------------------------------
# Command Line
#-------------------------------------------------------------------------------

def get_args():
    import argparse
    # Command line argument handling
    parser = argparse.ArgumentParser(
        description="""???""",
        epilog=""""""
    )
    parser.add_argument('-l', '--language', nargs='*', help='list of languages to generate', choices=LANGUAGES|{'all',}, default='all')
    parser.add_argument('--expected_output_filename', action='store', help='filename of expected output', default='_expected_output.txt')
    parser.add_argument('--log_level', default=logging.INFO, type=int)
    parser.add_argument('--version', action='version', version=VERSION)

    args = parser.parse_args()

    if 'all' in args.language:
        args.language = LANGUAGES

    return vars(args)


if __name__ == "__main__":
    kwargs = get_args()
    logging.basicConfig(level=kwargs['log_level'])

    filename = kwargs['expected_output_filename']
    with open(filename, 'rt', encoding='utf8') as f:
        expected_output_dict = parse_langauge_output(f.read())
    log.info(f'expecting each language output to have the following headings {expected_output_dict.keys()}')

    test_langauges(expected_output_dict, **kwargs)
