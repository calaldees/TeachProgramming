Cyrpto Project
==============

Objective
---------
The purpose of this project is to exercise the following spec points
* 3.5.1.6 Ordinal numbers
* 3.5.5.1 Character form of a decimal digit
* 3.5.5.2 ASCII and Unicode
* 3.5.6.8 Encryption

Terminology
-----------
key = password
cypher = 
cryptography = 
Caesar cypher =
Vernam cypher = 
clear-text = 
in-the-clear =

http://www.asciitable.com/

Write your solution in a file called `crypto.py` and have a function `def encode(key, message):` and `def decode(key, message):`

    >>> from crypto import encode, decode

    >>> encode('a', 'abc')
    'abc'
    >>> encode('b', 'abc')
    'bcd'
    >>> encode('c', 'abc')
    'cde'

    >>> decode('b', 'bcd')
    'abc'
    >>> decode('c', 'cde')
    'abc'

    >>> encode('abc', 'abc')
    'ace'
    >>> encode('abc', 'abcdef')
    'acedfh'

    >>> encode('b', 'xyz')
    'yza'
    >>> encode('abc', 'xyz')
    'xzb'

    >>> encode('pizza', 'hello i was a dog that sat on a log')
    'wmkko h wpa z swf twis spb nn i kov'
    >>> decode('pizza', 'wmkko h wpa z swf twis spb nn i kov')
    'hello i was a dog that sat on a log'

    >>> encode('b', 'abcABC123+-*!')
    'bcdABC123+-*!'



This document is a markdown doctest that can be run
https://docs.python.org/3.9/library/doctest.html#simple-usage-checking-examples-in-a-text-file

    python -m doctest -v crypto.md
