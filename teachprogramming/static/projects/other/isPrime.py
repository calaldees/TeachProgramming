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
