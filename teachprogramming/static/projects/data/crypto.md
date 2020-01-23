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

Task
----


This document is a markdown [doctest](https://docs.python.org/3.9/library/doctest.html#simple-usage-checking-examples-in-a-text-file)
The tests can be run with
```bash
    python -m doctest -v crypto.md
```

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
    'wmkko q vah z ddo shpb rai nm p kng'
    >>> decode('pizza', 'wmkko q vah z ddo shpb rai nm p kng')
    'hello i was a dog that sat on a log'

Secret bonus
------------

    >>> encode('b', 'abcABC123+-*!')
    'bcdbcd123+-*!'

    >>> import random
    >>> LETTERS = tuple(chr(i) for i in range(64, 127))
    >>> key = 'abc'
    >>> message = ''.join(random.choice(LETTERS) for i in range(1000))
    >>> message_encoded = encode(key, message)
    >>> message_decoded = decode(key, message_encoded)
    >>> assert message == message_decoded, f'{message} \n\n!=\n\n {message_decoded}'

