
def overlap(a: tuple, b: tuple):
    """
    Inspired by 
        https://news.ycombinator.com/item?id=33901287
        https://adventofcode.com/2022/day/4

    >>> assert not overlap((1,2),(3,4))
    >>> assert overlap((1,10),(5,15))
    >>> assert overlap((1,2),(2,3))
    >>> assert overlap((2,1),(3,2))
    >>> assert not overlap((-10,0),(1,10))
    """
    # Unfinished!!
    return max(a) < min(b) or min(a) > max(b)
    return frozenset(range(*sorted(a))) & frozenset(range(*sorted(b)))