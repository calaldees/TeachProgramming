def tower(n):
    r"""
    >>> tower(1)
    '#'
    >>> tower(2)
    ' #\n###'
    >>> tower(3)
    '  #\n ###\n#####'
    >>> tower(4)
    '   #\n  ###\n #####\n#######'
    """
    return '\n'.join(
        ' '*(n-1-i) + '#'*(i*2+1)
        for i in range(n)
    )
