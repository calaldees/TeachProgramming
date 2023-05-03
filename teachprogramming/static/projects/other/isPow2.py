

def isPowerOfTwo(x):
    """
    https://stackoverflow.com/a/600306/3356840
    bool IsPowerOfTwo(ulong x) {return (x & (x - 1)) == 0;}
    Amendem explanation - https://stackoverflow.com/a/32385656/3356840


    >>> isPowerOfTwo(1)
    True
    >>> isPowerOfTwo(2)
    True
    >>> isPowerOfTwo(3)
    False
    >>> isPowerOfTwo(4)
    True
    >>> isPowerOfTwo(5)
    False

    >>> import random
    >>> all(isPowerOfTwo(pow(2,x)) for x in range(1,100))
    True
    >>> any(isPowerOfTwo(pow(2,x)+1) for x in range(1,100))
    False
    """
    return (x & (x - 1)) == 0

