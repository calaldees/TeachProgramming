def isPrime(p):
    """
    https://brilliant.org/wiki/prime-numbers/
    https://en.wikipedia.org/wiki/Largest_known_prime_number
    https://en.wikipedia.org/wiki/Primality_test

    Check first 100 digets
    >>> PRIMES = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
    >>> for i in range(2,100):
    ...     assert (i in PRIMES) == isPrime(i), f"{i} is in list of primes {i in primes}"

    Test a mini prime number
    >>> isPrime(6700417)
    True
    >>> isPrime(6700418)
    False

    
    >>> import timeit, random, sys
    >>> timeit.timeit(lambda: isPrime(2147483647), number=1)

    >>> timeit.timeit(lambda: isPrime(random.randint(2, sys.maxsize)), number=100)
    """
    # The most inefficient prime number checker ever
    for i in range(2,p):
        if p % i == 0:
            return False
    return True

# Task optimise?



def isPrime2(n):
    """
    Check first 100 digets
    >>> PRIMES = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
    >>> for i in range(2,100):
    ...     assert (i in PRIMES) == isprime(i), f"{i} is in list of primes {PRIMES}"

    Test a mini prime number
    >>> isPrime2(6700417)
    True
    >>> isPrime2(6700418)
    False

    >>> import timeit, random, sys
    >>> timeit.timeit(lambda: isPrime2(2147483647), number=1)

    >>> timeit.timeit(lambda: isPrime2(random.randint(2, sys.maxsize)), number=100)

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
