# Inspired by
# https://gist.github.com/itsbilal/b4af303f70659a7f7d38
# https://www.educative.io/edpresso/what-is-the-rsa-algorithm  (this feels wrong - the e=17 does not track with the other example)

from typing import NamedTuple
from functools import partial



def gcd(p, q):
    """
    Create the Greatest_common_divisor of two positive integers.

    >>> gcd(10, 15)
    5
    """
    while q != 0:
        p, q = (q, p%q)
    return p
#from math import gcd

def phi(a, b):
    """
    >>> phi(61, 53)
    3120
    """
    return (a-1)*(b-1)

def is_coprime(a, b):
    """
    >>> is_coprime(17, 13)
    True
    >>> is_coprime(17, 21)
    True
    >>> is_coprime(15, 21)
    False
    >>> is_coprime(25, 45)
    False
    """
    return gcd(a, b) == 1
def coprime(n):
    """
    Find largest coprime to n and return it
    TODO: does this have to be the largest coprime? or any coprime?

    >>> coprime(9)
    7
    >>> coprime(17)
    15
    >>> coprime(3120)
    3113
    """
    return max(filter(partial(is_coprime, n), range(n-1)))

def isprime(n):
    """
    Check first 100 digets
    >>> PRIMES = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
    >>> for i in range(2,100):
    ...     assert (i in PRIMES) == isprime(i), f"{i} is in list of primes {PRIMES}"

    Test a mini prime number
    >>> isprime(6700417)
    True
    """
    assert isinstance(n, int) and n >= 0 # make sure n is a positive integer
    if n < 2:  # 0 and 1 are not primes
        return False
    if n == 2:   # 2 is the only even prime number
        return True
    if not n & 1:  # all other even numbers are not primes
        return False
    # range starts with 3 and only needs to go up the squareroot of n for all odd numbers
    for x in range(3, int(pow(n,0.5))+1, 2):
        if n % x == 0:
            return False
    return True


class Key(NamedTuple):
    e: int
    n: int
    def crypt(self, p):
        return pow(p, self.e, self.n)
    def crack(self):
        """
        First, find all prime numbers that multiply to give n
        For each p,q possibility, check if phi(p,q) and e are coprime

        >>> Key(3113, 3233).crack()
        (53, 61)
        >>> Key(1337, 3233).crack()
        (53, 61)
        """
        for p in range(2, self.n-1):
            if isprime(p) and (self.n % p) == 0:
                q = self.n // p
                if isprime(q) and is_coprime(self.e, phi(p, q)):
                    return (p, q)

def keygen(p, q):
    """
    >>> keygen(61, 53)
    (Key(e=3113, n=3233), Key(e=1337, n=3233))
    """
    assert isprime(p)
    assert isprime(q)
    n = p * q
    _phi = phi(p, q)
    e = coprime(_phi)
    d = next(filter(lambda d: (d * e) % _phi == 1, range(3, _phi)))
    return (Key(e,n), Key(d,n))  # the first key is public, the second is private


def _test():
    """
    >>> pub, pri = keygen(61, 53)

    >>> pri.crypt(pub.crypt(123))
    123

    >>> pub.crypt(pri.crypt(123))
    123
    """
    pass


if __name__ == "__main__":
    print("see doctests - python3 -m doctest -v rsa.py")
