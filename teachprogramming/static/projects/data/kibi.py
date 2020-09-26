
BASE_NAME_LOOKUP = ('','K','M','G','T','P')

def humanise(size, base=1000, base_str='B'):
    """
    >>> humanise(0)
    '0.0B'
    >>> humanise(1000)
    '1.0KB'
    >>> humanise(1499)
    '1.5KB'
    >>> humanise(1500)
    '1.5KB'
    >>> humanise(10000)
    '10.0KB'
    >>> humanise(100000)
    '100.0KB'
    >>> humanise(999900)
    '999.9KB'
    >>> humanise(1000000)
    '1.0MB'
    >>> humanise(1490000)
    '1.5MB'
    >>> humanise(1530000000)
    '1.5GB'
    >>> humanise(15300000000)
    '15.3GB'

    >>> humanise(1000000, base=1024, base_str='iB')
    '976.6KiB'
    >>> humanise(1048576, base=1024, base_str='iB')
    '1.0MiB'
    
    #>>> humanise(1048575, base=1024, base_str='iB')
    #'1.0MiB'
    """
    def get_threshold(size):
        for i, _ in enumerate(BASE_NAME_LOOKUP):
            threshold = pow(base, i)
            if not (size // threshold):
                return (pow(base, max(0,i-1)), BASE_NAME_LOOKUP[max(0,i-1)])
    threshold, name = get_threshold(size)
    return f'{round(size / threshold, 1)}{name}{base_str}'


# NAME_LOOKUP = (
#     (0, 'B'),
#     (1000, 'KB'),
#     (1000000, 'MB'),
#     (1000000000, 'GB'),
# )
# def humanise_simple(size):
#     """
#     >>> humanise_simple(1)
#     1B
#     >>> humanise_simple(1000)
#     1KB
#     >>> humanise_simple(1500)
#     2KB
#     >>> humanise_simple(900000)
#     900KB
#     >>> humanise_simple(1000000)
#     1.0MB
#     >>> humanise_simple(1005000)
#     1.0MB
#     >>> humanise_simple(1500000)
#     1.5MB
#     >>> humanise_simple(1590000)
#     1.6MB
#     """
#     for threshold, name in NAME_LOOKUP:
#         if size < threshold:
#             continue
#     size / threshold
