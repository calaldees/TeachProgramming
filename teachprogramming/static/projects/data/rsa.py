# Inspired by
# https://gist.github.com/itsbilal/b4af303f70659a7f7d38
# https://www.educative.io/edpresso/what-is-the-rsa-algorithm  (this feels wrong - the e=17 does not track with the other example)
# The above also state that e=public key and d=private - the private key is derived from the public key? I think this is the wrong way round. The public key can be derived from the private key
# TODO
# [Idempotent Factorizations: A New Addition to the Cryptography Classroom](https://dl.acm.org/doi/10.1145/3304221.3325557)

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
    return next(filter(partial(is_coprime, n), range(n-2,0,-1)))

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
    return (Key(e,n), Key(d,n))  # the first key is private, the second is public key  # swapped from original


def _test():
    """
    >>> pri, pub = keygen(61, 53)

    >>> pri.crypt(pub.crypt(123))
    123

    >>> pub.crypt(pri.crypt(123))
    123
    """
    pass

def _test2():
    r"""
    >>> from functools import partial
    >>> from calaldees.iterator import IteratorCombine
    >>> def _enc_func(f):
    ...     return IteratorCombine().map(f).map(partial(int.to_bytes, length=2, byteorder='big')).flatten().func(bytes).process
    >>> def _dec_func(f):
    ...     return IteratorCombine().group(2).map(partial(int.from_bytes, byteorder='big')).map(f).func(bytes).process

    >>> pri, pub = keygen(61, 53)

    >>> pub_encrypt_to_bytes = _enc_func(pub.crypt)
    >>> pri_decrypt_from_bytes = _dec_func(pri.crypt)
    >>> pub_encrypt_to_bytes(b'abc')
    b'\x03\n\x08\x9c\x0c\x0f'
    >>> pri_decrypt_from_bytes(b'\x03\n\x08\x9c\x0c\x0f')
    b'abc'

    >>> pri_encrypt_to_bytes = _enc_func(pri.crypt)
    >>> pub_decrypt_from_bytes = _dec_func(pub.crypt)
    >>> pri_encrypt_to_bytes(b'abc')
    b'\x0b8\tq\x03\xaf'
    >>> pub_decrypt_from_bytes(b'\x0b8\tq\x03\xaf')
    b'abc'
    """
    pass


def random_prime():
    import random
    i = random.randint(0, 255)
    while not isprime(i):
        i += 1
    return i


class KeyCrack(Key):
    def crack(self):
        """
        First, find all prime numbers that multiply to give n
        For each p,q possibility, check if phi(p,q) and e are coprime

        >>> KeyCrack(3113, 3233).crack()
        (53, 61)
        >>> KeyCrack(1337, 3233).crack()
        (53, 61)
        """
        for p in range(2, self.n-1):
            if isprime(p) and (self.n % p) == 0:
                q = self.n // p
                if isprime(q) and is_coprime(self.e, phi(p, q)):
                    return (p, q)


if __name__ == "__main__":
    # any two prime numbers - there are A LOT - http://www.primos.mat.br/2T_en.html
    print("see doctests")
    print("python3 -m doctest -v rsa.py")
    print("or")
    print("pytest --doctest-modules rsa.py")
