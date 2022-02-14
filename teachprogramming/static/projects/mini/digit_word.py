
DIGIT_WORDS = {
    1: 'ONE',
    2: 'TWO',
    3: 'THREE',
    4: 'FOUR',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    8: 'EIGHT',
    9: 'NINE',
}
def digit_word(s):
    """
    >>> digit_word('BOUNCE')
    1
    >>> digit_word('ENCODE')
    'NO'
    >>> digit_word('EIGHT')
    8
    >>> digit_word('BLACKJACK')
    'NO'
    >>> digit_word('FABULOUS')
    'NO'
    >>> digit_word('EXERCISE')
    'NO'
    >>> digit_word('DRIFTWOOD')
    2
    >>> digit_word('SERVICEMAN')
    7
    >>> digit_word('INSIGNIFICANCE')
    9
    >>> digit_word('THROWDOWN')
    2
    """
    assert s.isupper()
    for digit_int, digit_str in DIGIT_WORDS.items():
        digit_str = list(digit_str)
        for letter in s:
            if letter == digit_str[0]:
                digit_str.pop(0)
            if not digit_str:
                return digit_int
    return 'NO'
