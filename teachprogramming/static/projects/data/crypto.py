"""
placeholder for 'passphrase' cypher exercise
https://en.wikipedia.org/wiki/Frequency_analysis

Given a passphrase can a message be encrypted/decrypted

This is an exercise for string manipulation and ascii
"""

import re

LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def cypher_ceaser(text, offset=1):
    """
    >>> cypher_ceaser('abc', 1)
    'bcd'
    >>> cypher_ceaser('hello', 1)
    'ifmmp'
    >>> cypher_ceaser('xyz', 1)
    'yza'
    >>> cypher_ceaser('a b c', -1)
    'z a b'
    """
    def _offset_letter(letter):
        if letter not in LETTERS:
            return letter
        return LETTERS[(LETTERS.index(letter) + offset) % len(LETTERS)]
    return ''.join(map(_offset_letter, text.lower()))


from itertools import cycle
from operator import add, sub

def cypher_vigenere(text, keyword, letter_shift_operator=add):
    """
    >>> cypher_vigenere('abc', 'a')
    'abc'
    >>> cypher_vigenere('abc', 'b')
    'bcd'
    >>> cypher_vigenere('abc', 'bb')
    'bcd'
    >>> cypher_vigenere('abc', 'abc')
    'ace'
    >>> cypher_vigenere('bcd', 'b', sub)
    'abc'
    >>> cypher_vigenere('hello! i was a dog that sat on a log', 'pizza')
    'wmkko! h wpa z swf twis spb nn i kov'
    >>> cypher_vigenere('wmkko! h wpa z swf twis spb nn i kov', 'pizza', sub)
    'hello! i was a dog that sat on a log'
    """
    text = text.lower()
    def _offset_letter(letter_tuple):
        letter, keyword_letter = letter_tuple
        if letter not in LETTERS:
            return letter
        return LETTERS[
            letter_shift_operator(
                LETTERS.index(letter),
                LETTERS.index(keyword_letter),
            ) % len(LETTERS)
        ]
    return ''.join(
        map(_offset_letter, zip(text, cycle(keyword)))
    )
