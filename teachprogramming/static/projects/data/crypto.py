"""
placeholder for 'passphrase' cypher exercise
https://en.wikipedia.org/wiki/Frequency_analysis

Given a passphrase can a message be encrypted/decrypted

This is an exercise for string manipulation and ascii
"""

def cypher_ceaser_ascii(text, offset=1):
    """
    >>> cypher_ceaser('abc', 1)
    'bcd'
    >>> cypher_ceaser_ascii('hello', 1)
    'ifmmp'
    >>> cypher_ceaser('xyz', 1)
    'yza'
    """
    return ''.join(chr(((ord(letter)+offset-97)%26)+97) for letter in text)


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

def cypher_vigenere(key, text, letter_shift_operator=add):
    """
    >>> cypher_vigenere('a', 'abc')
    'abc'
    >>> cypher_vigenere('b', 'abc')
    'bcd'
    >>> cypher_vigenere('bb', 'abc')
    'bcd'
    >>> cypher_vigenere('abc', 'abc')
    'ace'
    >>> cypher_vigenere('b', 'bcd', sub)
    'abc'
    >>> cypher_vigenere('pizza', 'hello i was a dog that sat on a log')
    'wmkko q vah z ddo shpb rai nm p kng'
    >>> cypher_vigenere('pizza', 'wmkko q vah z ddo shpb rai nm p kng', sub)
    'hello i was a dog that sat on a log'
    """
    text = text.lower()
    def _offset_letter(letter_tuple):
        letter, keyword_letter = letter_tuple
        if letter not in LETTERS:
            return letter
        return LETTERS[
            letter_shift_operator(
                LETTERS.index(letter),
                keyword_letter if isinstance(keyword_letter, int) else LETTERS.index(keyword_letter),
            ) % len(LETTERS)
        ]
    key_sequence = key if isinstance(key, (str, list, tuple)) else (key, )
    return ''.join(
        map(_offset_letter, zip(text, cycle(key_sequence)))
    )

# Quick hack to make `cypher.md` doctests example work
from functools import partial
encode = partial(cypher_vigenere, letter_shift_operator=add)
decode = partial(cypher_vigenere, letter_shift_operator=sub)