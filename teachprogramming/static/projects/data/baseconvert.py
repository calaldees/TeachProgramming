"""
Worthy of note
https://docs.python.org/3/reference/lexical_analysis.html#integer-literals
Python has binary, oct and hex representation builtin - integer literals

https://www.programiz.com/python-programming/numbers
https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals

also Fraction and Decimal
"""
t1 = 0xff
t2 = 0b101101
t3 = b'\xff'

''

def baseconvert(number, fromdigits, todigits):
    """
    http://pastebin.com/f54dd69d6
    http://code.activestate.com/recipes/111286/?_ga=1.4032048.1464823167.1442695690
    http://code.activestate.com/recipes/410672-custom-string-representations-of-bases/

    converts a "number" between two bases of arbitrary digits

    The input number is assumed to be a string of digits from the
    fromdigits string (which is in order of smallest to largest
    digit). The return value is a string of elements from todigits
    (ordered in the same way). The input and output bases are
    determined from the lengths of the digit strings. Negative
    signs are passed through.

    This converts the input into an integer and back - this is designed a teaching aid
    It will not work large amounts of data

    decimal to binary
    >>> baseconvert(555, baseconvert.BASE10, baseconvert.BASE2)
    '1000101011'

    binary to decimal
    >>> baseconvert('1000101011', baseconvert.BASE2, baseconvert.BASE10)
    '555'

    integer interpreted as binary and converted to decimal (!)
    >>> baseconvert(1000101011, baseconvert.BASE2, baseconvert.BASE10)
    '555'

    base10 to base4
    >>> baseconvert(99, baseconvert.BASE10, "0123")
    '1203'

    base4 to base5 (with alphabetic digits)
    >>> baseconvert(1203, "0123", "abcde")
    'dee'

    base5, alpha digits back to base 10
    >>> baseconvert('dee', "abcde", baseconvert.BASE10)
    '99'

    decimal to a base that uses A-Z0-9a-z for its digits
    >>> baseconvert(257938572394, baseconvert.BASE10, baseconvert.BASE62)
    'E78Lxik'

    ..convert back
    >>> baseconvert('E78Lxik', baseconvert.BASE62, baseconvert.BASE10)
    '257938572394'

    binary to a base with words for digits (the function cannot convert this back)
    >>> baseconvert('1101', baseconvert.BASE2, ('Zero','One'))
    'OneOneZeroOne'

    base64 is an actual format - THIS ALGORITHM ONLY WORKS FOR SMALL VALUES!
    https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
    >>> baseconvert('A', baseconvert.BASE64, baseconvert.BASE10)
    '0'

    """

    if str(number)[0] == '-':
        number = str(number)[1:]
        neg = 1
    else:
        neg = 0

    # make an integer out of the number
    x = 0
    for digit in str(number):
        x = x * len(fromdigits) + fromdigits.index(digit)

    # create the result in base 'len(todigits)'
    if x == 0:
        res = todigits[0]
    else:
        res = ""
        while x > 0:
            digit = x % len(todigits)
            res = todigits[digit] + res
            x = int(x / len(todigits))
        if neg:
            res = "-"+res

    return res

baseconvert.BASE2 = "01"
baseconvert.BASE10 = "0123456789"
baseconvert.BASE16 = "0123456789ABCDEF"
baseconvert.BASE36 = "0123456789abcdefghijklmnopqrstuvwxyz"
baseconvert.BASE62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
baseconvert.BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
