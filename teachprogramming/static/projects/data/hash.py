FNV_offset_basis = 14695981039346656037
FNV_prime = 1099511628211
uint64_max = pow(2,64)

def fnv1(data):
    r"""
    >>> fnv1(b'')
    14695981039346656037
    >>> fnv1(b'\x00')
    12638153115695167455
    >>> fnv1(b'abc')
    15626587013303479755
    """
    hash = FNV_offset_basis
    for b in data:
        hash *= FNV_prime
        hash %= uint64_max  # python does not support uint64, so we simulate it with mod operator
        hash ^= b
    return hash
