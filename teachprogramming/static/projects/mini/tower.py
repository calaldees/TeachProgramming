def tower(n):
    r"""
    >>> print(tower(1))
    #
    >>> print(tower(2))
     #
    ###
    >>> print(tower(3))
      #
     ###
    #####
    >>> print(tower(4))
       #
      ###
     #####
    #######

    """
    return '\n'.join(' '*(n-1-i) + '#'*(i*2+1) for i in range(n))

import doctest ; doctest.testmod()