
def overlap(a: tuple, b: tuple):
    """
    Inspired by 
        https://news.ycombinator.com/item?id=33901287
        https://adventofcode.com/2022/day/4

    >>> assert overlap((0,1),(0,1))
    >>> assert overlap((1,10),(5,15))
    >>> assert overlap((1,2),(2,3))
    >>> assert overlap((2,3),(1,2))
    >>> assert overlap((2,1),(3,2))

    >>> assert not overlap((1,2),(3,4))
    >>> assert not overlap((-10,0),(1,10))

    >>> assert overlap((0,100),(20,30))
    >>> assert overlap((20,30),(0,100))
    >>> assert not overlap((0,100),(120,130))
    >>> assert not overlap((0,1),(100,101))
    """
    return (max(a) > max(b) and min(a) < min(b)) or (max(a) >= min(b) and min(a) <= max(b))

    # a set based approach - very wasteful
    _range = lambda a, b: range(a,b+1)  # make range inclusive
    return frozenset(_range(*sorted(a))) & frozenset(_range(*sorted(b)))
