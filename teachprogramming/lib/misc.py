import random
import datetime

# Normalize Python 3 vocab
# http://www.rfk.id.au/blog/entry/preparing-pyenchant-for-python-3/
try:
    unicode = unicode
except NameError:
    # 'unicode' is undefined, must be Python 3
    str = str
    unicode = str
    bytes = bytes
    basestring = (str,bytes)
else:
    # 'unicode' exists, must be Python 2
    str = str
    unicode = unicode
    bytes = str
    basestring = basestring

import inspect
#print "My name is: %s" % inspect.stack()[0][3]
def funcname(level=1):
    return inspect.stack()[level][3]


def random_string(length=8):
    """
    Generate a random string of a-z A-Z 0-9
    (Without vowels to stop bad words from being generated!)

    >>> len(random_string())
    8
    >>> len(random_string(10))
    10

    If random, it should compress pretty badly:

    >>> import zlib
    >>> len(zlib.compress(random_string(100))) > 50
    True
    """
    random_symbols = '1234567890bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    r = ''
    for i in range(length):
        r += random_symbols[random.randint(0,len(random_symbols)-1)]
    return r


_normalize_datetime_lookup = {
    'minute': lambda d: d.replace(microsecond=0, second=0),
    'hour'  : lambda d: d.replace(microsecond=0, second=0, minute=0),
    'day'   : lambda d: d.replace(microsecond=0, second=0, minute=0, hour=0),
    'week'  : lambda d: d.replace(microsecond=0, second=0, minute=0, hour=0) - datetime.timedelta(days=d.weekday()),
}
def normalize_datetime(d=None, accuracy='hour'):
    """
    Normalizez datetime down to hour or day
    Dates are immutable (thank god)
    """
    if not d:
        d = datetime.datetime.now()
    return _normalize_datetime_lookup[accuracy](d)
