
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
    >>> in_a_row('aabbbccb')
    3
    >>> in_a_row('aabbbcacbaa')
    3
    >>> in_a_row((1,2,2,3,3,3,2,2))
    3

    """
    max_count = 0
    for i in data:
        count = 0
        for j in data:
            if i == j:
                count += 1
            else:
                count = 0
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
    >>> in_a_row2('aabbccdd')
    (2, 'a')
    >>> in_a_row2('aabbbcc')
    (3, 'b')
    >>> in_a_row2('aabbbccb')
    (3, 'b')
    >>> in_a_row2('aabbbcacbaa')
    (3, 'b')
    >>> in_a_row2((1,2,2,3,3,3,2,2))
    (3, 3)
    """
    max_count, max_i = 0, None
    for i in sorted(set(data)):
        count = 0
        for j in data:
            count = count + 1 if i == j else 0
            if count > max_count:
                max_count, max_i = count, i
    return max_count, max_i


import re
def in_a_row3(data):
    """
    String only with regex

    >>> in_a_row3('')
    (0, '')
    >>> in_a_row3('aabbbccb')
    (3, 'b')
    >>> in_a_row3('aabbbcacbaa')
    (3, 'b')
    """
    if not data: return (0, '')
    return max(
        (max(map(len, re.split(f'[^{i}]', data))), i)
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
    >>> in_a_row4('aabbbccb')
    (3, 'b')
    >>> in_a_row4('aabbbcacbaa')
    (3, 'b')
    >>> in_a_row4((1,2,2,3,3,3,2,2))
    (3, 3)
    """
    if not data: return (0, '')
    return max(
        (sum(1 for _ in iterator), key)
        for key, iterator in groupby(data)
    )


# ---- stuff that did not work

    #return max(
        #reduce(lambda acc, j: acc+1 if i==j else 0, data, 0)
        #sum(1 for j in data if i == j)  #, i)
    #    for i in set(data)
    #)
