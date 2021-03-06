import sys


def mergelists(aa, bb):
    """
    >>> mergelists([2], [1])
    [1, 2]
    >>> mergelists([2], [1,3])
    [1, 2, 3]
    >>> mergelists([1,2,3], [4,5,6])
    [1, 2, 3, 4, 5, 6]
    >>> mergelists([2,4,6], [1,3,5])
    [1, 2, 3, 4, 5, 6]
    >>> mergelists([1, 4], [1, 3, 5, 6])
    [1, 1, 3, 4, 5, 6]
    """
    oo = []
    while aa or bb:
        va = aa[0] if aa else sys.maxsize
        vb = bb[0] if bb else sys.maxsize
        if va < vb:
            oo.append(aa.pop(0))
            continue
        oo.append(bb.pop(0))
    return oo

def mergesort(aa):
    """
    >>> mergesort([1,2,3])
    [1, 2, 3]
    >>> mergesort([5,6,1,3,5,3,9,4,9,6,2,5,4,1])
    [1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 9, 9]
    """
    lists = [[item] for item in aa]
    while len(lists) > 1:
        lists.append(mergelists(lists.pop(0), lists.pop(0)))
    return lists.pop()

if __name__ == "__main__":
    pass
    #mergesort([5,6,1,3,5,3,9,4,9,6,2,5,4,1])
    #mergelists([1, 4], [1, 3, 5, 6])