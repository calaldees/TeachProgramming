"""
placeholder for 'passphrase' cypher exercise
https://en.wikipedia.org/wiki/Frequency_analysis

Given a passphrase can a message be encrypted/decrypted

This is an exercise for string manipulation and ascii
"""

def cypher_ceaser_ascii(text, offset=1):
    """
    >>> cypher_ceaser_ascii('abc', 1)
    'bcd'
    >>> cypher_ceaser_ascii('hello', 1)
    'ifmmp'
    >>> cypher_ceaser_ascii('xyz', 1)
    'yza'
    """
    return ''.join(chr(((ord(letter)+offset-97)%26)+97) for letter in text)


LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def cypher_ceaser_0(text, offset=1):
    """
    >>> cypher_ceaser_0('abc', 1)
    'bcd'
    >>> cypher_ceaser_0('hello', 1)
    'ifmmp'
    >>> cypher_ceaser_0('xyz', 1)
    'yza'
    >>> cypher_ceaser_0('a b c', -1)
    'z a b'
    """
    def getIndexFromLetter(letter):
        for i in range(len(LETTERS)):
            if LETTERS[i] == letter:
                return i
        return -1

    def getLetterFromIndex(index):
        return LETTERS[index]

    output = ''
    for letter in text:
        letter_index = getIndexFromLetter(letter)
        if letter_index < 0:
            new_letter = ' '
        else:
            letter_index = (letter_index + offset) % len(LETTERS)
            new_letter = getLetterFromIndex(letter_index)
        output = output + new_letter
    return output



def cypher_ceaser_1(text, offset=1):
    """
    >>> cypher_ceaser_1('abc', 1)
    'bcd'
    >>> cypher_ceaser_1('hello', 1)
    'ifmmp'
    >>> cypher_ceaser_1('xyz', 1)
    'yza'
    >>> cypher_ceaser_1('a b c', -1)
    'z a b'
    """
    output = ''
    for letter in text:
        if letter in LETTERS:
            letter_index = LETTERS.index(letter)
            letter_index = (letter_index + offset) % len(LETTERS)
            letter = LETTERS[letter_index]
        output = output + letter
    return output

def cypher_ceaser_2(text, offset=1):
    """
    >>> cypher_ceaser_2('abc', 1)
    'bcd'
    >>> cypher_ceaser_2('hello', 1)
    'ifmmp'
    >>> cypher_ceaser_2('xyz', 1)
    'yza'
    >>> cypher_ceaser_2('a b c', -1)
    'z a b'
    """
    output = ''
    for letter in text:
        if letter in LETTERS:
            letter = LETTERS[(LETTERS.index(letter) + offset) % len(LETTERS)]
        output += letter
    return output

def cypher_ceaser_3(text, offset=1):
    """
    >>> cypher_ceaser_3('abc', 1)
    'bcd'
    >>> cypher_ceaser_3('hello', 1)
    'ifmmp'
    >>> cypher_ceaser_3('xyz', 1)
    'yza'
    >>> cypher_ceaser_3('a b c', -1)
    'z a b'
    """
    def _offset_letter(letter):
        if letter not in LETTERS:
            return letter
        return LETTERS[(LETTERS.index(letter) + offset) % len(LETTERS)]
    return ''.join(map(_offset_letter, text.lower()))


import io
def cypher_ceaser(src, des, offset=1, _buffer=65535):
    r"""
    >>> src = io.BytesIO(b"abc")
    >>> des = io.BytesIO()
    >>> cypher_ceaser(src, des, offset=1)
    >>> des.getvalue()
    b'bcd'

    >>> src.seek(0)
    0
    >>> des.seek(0)
    0
    >>> cypher_ceaser(des, src, offset=-1)
    >>> src.getvalue()
    b'abc'

    >>> src = io.BytesIO(b"\xfe\xff\x00\x01")
    >>> des = io.BytesIO()
    >>> cypher_ceaser(src, des, offset=1)
    >>> des.getvalue()
    b'\xff\x00\x01\x02'
    """
    while data := src.read(_buffer):
        des.write(bytes((d + offset) % 256 for d in data))


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
    >>> cypher_vigenere('abc', 'z a b', sub)
    'z y a'
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