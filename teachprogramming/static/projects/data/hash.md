Hash
====

https://brilliant.org/wiki/secure-hashing-algorithms/
sha is HARD!

https://www.quora.com/What-is-the-simplest-example-of-a-hash-function

FNV-1 hash
----------
https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
```
uint64 FNV_offset_basis = 14695981039346656037 
uint64 FNV_prime = 1099511628211 

algorithm fnv-1 is
    hash := FNV_offset_basis

    for each byte_of_data to be hashed do
        hash := hash * FNV_prime
        hash := hash XOR byte_of_data

    return hash 
```

```python
FNV_offset_basis = 14695981039346656037 
FNV_prime = 1099511628211 
uint64_max = pow(2,64)

def fnv1(data):
    """
    >>> fnv1(b'')
    14695981039346656037
    >>> fnv1(b'x\00')
    590622495169253573
    >>> fnv1(b'abc')
    15626587013303479755
    """
    hash = FNV_offset_basis
    for b in data:
        hash *= FNV_prime
        hash %= uint64_max  # python does not support uint64, so we simulate it with mod operator
        hash ^= b
    return hash
```

