
def in_a_row(data):
    """
    >>> in_a_row('')
    0
    >>> in_a_row('a')
    1
    >>> in_a_row('b')
    1
    >>> in_a_row('ab')
    1
    >>> in_a_row('aa')
    2
    >>> in_a_row('aab')
    2
    >>> in_a_row('abb')
    2
    >>> in_a_row('aabbcc')
    2
    >>> in_a_row('aabbbcc')
    3
    """
    max_count = 0
    for i in data:
        count = 0
        for j in data:
            if i == j:
                count += 1
        if count > max_count:
            max_count = count
    return max_count

def in_a_row2(data):
    """
    >>> in_a_row2('')
    (0, None)
    >>> in_a_row2('a')
    (1, 'a')
    >>> in_a_row2('b')
    (1, 'b')
    >>> in_a_row2('ab')
    (1, 'a')
    >>> in_a_row2('aa')
    (2, 'a')
    >>> in_a_row2('aab')
    (2, 'a')
    >>> in_a_row2('abb')
    (2, 'b')
    >>> in_a_row2('aabbcc')
    (2, 'a')
    >>> in_a_row2('aabbbcc')
    (3, 'b')
    """
    max_count = 0
    max_i = None
    for i in data:
        count = 0
        for j in data:
            if i == j:
                count += 1
        if count > max_count:
            max_count = count
            max_i = i
    return max_count, max_i


def in_a_row3(data):
    """
    >>> in_a_row3('')
    0
    >>> in_a_row3('a')
    1
    >>> in_a_row3('b')
    1
    >>> in_a_row3('ab')
    1
    >>> in_a_row3('aa')
    2
    >>> in_a_row3('aab')
    2
    >>> in_a_row3('abb')
    2
    >>> in_a_row3('aabbcc')
    2
    >>> in_a_row3('aabbbcc')
    3
    """
    if not data: return 0
    return max(
        sum(1 for j in data if i == j)  #, i)
        for i in set(data)
    )

from itertools import groupby
def in_a_row4(data):
    """
    >>> in_a_row4('')
    (0, '')
    >>> in_a_row4('a')
    (1, 'a')
    >>> in_a_row4('b')
    (1, 'b')
    >>> in_a_row4('ab')
    (1, 'b')
    >>> in_a_row4('aa')
    (2, 'a')
    >>> in_a_row4('aab')
    (2, 'a')
    >>> in_a_row4('abb')
    (2, 'b')
    >>> in_a_row4('aabbcc')
    (2, 'c')
    >>> in_a_row4('aabbbcc')
    (3, 'b')
    """
    if not data: return (0, '')
    return max(
        (sum(1 for _ in iterator), key)
        for key, iterator in groupby(data)
    )
