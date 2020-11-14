"""
https://en.wikipedia.org/wiki/Huffman_coding
https://en.wikipedia.org/wiki/Canonical_Huffman_code
https://www.geeksforgeeks.org/canonical-huffman-coding/

docker run -it --name python3.9 --volume $PWD:/code/:ro python:alpine /bin/sh
"""

import io
import typing
from functools import reduce, total_ordering
from itertools import zip_longest, tee, groupby
from collections import defaultdict
from queue import PriorityQueue


def pairwise(iterable, fillvalue=None):
    """
    https://stackoverflow.com/a/5434936/3356840
    s -> (s0,s1), (s1,s2), (s2, s3), ...

    >>> tuple(pairwise((1,2,3)))
    ((1, 2), (2, 3), (3, None))
    """
    a, b = tee(iterable)
    next(b, None)
    return zip_longest(a, b, fillvalue=fillvalue)
def is_last(iterable):
    """
    >>> tuple(is_last('123'))
    (('1', False), ('2', False), ('3', True))
    """
    return ((a, True if b is None else False) for a, b in pairwise(iterable))


def bytes_iterator(source, chunksize=8192):
    """
    https://stackoverflow.com/a/1035456
    
    >>> tuple(bytes_iterator(b"abc"))
    (97, 98, 99)
    >>> tuple(bytes_iterator(io.BytesIO(b"abc")))
    (97, 98, 99)
    """
    if isinstance(source, bytes):
        for b in source:
            yield b
        return
    while data := source.read(chunksize):
        for b in data:
            yield b
def bit_iterator(byte):
    """
    >>> tuple(bit_iterator(15))
    (0, 0, 0, 0, 1, 1, 1, 1)
    >>> tuple(bit_iterator(129))
    (1, 0, 0, 0, 0, 0, 0, 1)
    """
    for i in range(7, -1, -1):
        yield 1 if byte & pow(2, i) else 0
def bit_iter_to_byte(data):
    """
    >>> bit_iter_to_byte((0,0,0,0,0,0,0,0))
    0
    >>> bit_iter_to_byte((0,0,0,0,0,0,0,1))
    1
    >>> bit_iter_to_byte((1,0,0,0,0,0,0,0))
    128
    >>> bit_iter_to_byte((1,1,1,1,1,1,1,1))
    255
    >>> bit_iter_to_byte((0,0,0,0,1,1,1,1))
    15
    >>> bit_iter_to_byte((1,0,0,0,0,0,0,1))
    129
    """
    data = tuple(data)
    l = len(data)
    assert l == 8
    byte = 0
    for i in range(l):
        byte |= pow(2, 7 - i) if data[i] else 0
    return byte


@total_ordering
class Tree():
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __str__(self):
        return f'({str(self.left)},{str(self.right)})'

    def __cmp__(self, other):
        return False
    def __eq__(self, other):
        return self is other
    def __lt__(self, other):
        return False

    @property
    def depth_of_nodes(self):
        """
        >>> t = Tree(left='C', right=Tree(left=Tree(left='D', right='A'), right='B'))
        >>> tuple(t.depth_of_nodes)
        ((1, 'C'), (2, 'B'), (3, 'D'), (3, 'A'))
        """
        stack = [(1, self)]
        while stack:
            depth, i = stack.pop()
            if isinstance(i.left, self.__class__):
                stack.append((depth+1, i.left))
            else:
                yield (depth, i.left)
            if isinstance(i.right, self.__class__):
                stack.append((depth+1, i.right))
            else:
                yield (depth, i.right)

    @property
    def dict(self):
        """
        >>> t = Tree(left='C', right=Tree(left=Tree(left='D', right='A'), right='B'))
        >>> t.dict
        {'C': (0,), 'D': (1, 0, 0), 'A': (1, 0, 1), 'B': (1, 1)}
        """
        d = {}
        stack = [("", self)]
        while stack:
            path, i = stack.pop()
            if isinstance(i, self.__class__):
                stack.append((path+"1", i.right))
                stack.append((path+"0", i.left))
            else:
                d[i] = tuple(0 if c=="0" else 1 for c in path)
        return d



def _frequency_analysis(data: bytes) -> dict[str, int]:
    """
    >>> import random
    >>> fa = _frequency_analysis(b'ABCD' + b'A'*9 + b'C'*14 + b'D'*6)
    >>> {chr(k): v for k, v in fa.items()}
    {'A': 10, 'B': 1, 'C': 15, 'D': 7}
    """
    def _(acc, char):
        acc[char] += 1
        return acc
    return reduce(_, data, defaultdict(int))

class WeightTreeItem(typing.NamedTuple):
    weight: int
    item: typing.Union[int, Tree]
def _convert_to_PriorityQueue(fa) -> PriorityQueue:
    """
    >>> q = _convert_to_PriorityQueue({'A': 10, 'B': 1, 'C': 15, 'D': 7})
    >>> q.get()
    WeightTreeItem(weight=1, item='B')
    >>> q.get()
    WeightTreeItem(weight=7, item='D')
    >>> q.get()
    WeightTreeItem(weight=10, item='A')
    >>> q.get()
    WeightTreeItem(weight=15, item='C')
    """
    def _(q, item):
        key, weight = item
        q.put(WeightTreeItem(weight, key))
        return q
    return reduce(_, fa.items(), PriorityQueue())

# ------------------------------------------------------------------------------

def _build_tree_from_data(data):
    """
    # WeightTreeItem(weight=33, item=)
    >>> t = _build_tree_from_data(b'ABCD' + b'A'*9 + b'C'*14 + b'D'*6)
    >>> t
    <huffman.Tree object at 0x...>
    >>> chr(t.left)
    'C'
    >>> t.right
    <huffman.Tree object at 0x...>
    """
    q = _convert_to_PriorityQueue(_frequency_analysis(data))
    while q.qsize() > 1:
        a, b = q.get(), q.get()
        q.put(WeightTreeItem(a.weight + b.weight, Tree(a.item, b.item)))
    return q.get().item

def _normalise_depths_from_tree(tree: Tree) -> tuple[int]:
    """
    A dataset of every possible 0-255 byte is uniform. Each key length in the tree will be 8-bits
    >>> t = _build_tree_from_data(bytes(range(256)))
    >>> assert _normalise_depths_from_tree(t) == (8,)*256

    #>>> t = Tree(left=3, right=Tree(left=Tree(left=4, right=1), right=2))
    # +bytes(range(128)
    #>>> from itertools import groupby
    #>>> tuple((i, sum(1 for x in ll)) for i, ll in groupby(sorted(_normalise_depths_from_tree(t))))
    """
    i_depth = sorted((i, depth) for depth, i in sorted(tree.depth_of_nodes))
    def pop_if_match(i):
        if i_depth:
            _i, _depth = i_depth[0]
            if i == _i:
                i_depth.pop(0)
                return _depth
        return 0
    return tuple(pop_if_match(i) for i in range(256))

def _tree_from_normalised_depths(normalised_depths: tuple[int]) -> Tree:
    """
    #>>> t = _tree_from_normalised_depths((1, 2, 3))
    >>> normalised_depths = (8,)*256
    >>> t = _tree_from_normalised_depths(normalised_depths)
    >>> t
    <huffman.Tree object at 0x...>
    >>> import re
    >>> frozenset(map(str,range(256))) == frozenset(re.findall('\d+', str(t)))
    True
    >>> _normalise_depths_from_tree(t) == normalised_depths
    True
    """
    # Take a list of 'bitlengths' in order for 0-255 and make a sorted bitdepth->character list
    assert len(normalised_depths) == 256, 'must have a depth for each character 0-255'

    normalised_character_to_huffman_binary_code = []
    huffman_code = ''
    for depth, character in sorted(zip(
        normalised_depths,
        range(256),
    )):
        huffman_code_length = len(huffman_code) or depth
        huffman_code = ("{0:b}".format(int(huffman_code, base=2)+1) if huffman_code else '').zfill(huffman_code_length)
        if depth > len(huffman_code):
            huffman_code += '0'*(depth-len(huffman_code))
        normalised_character_to_huffman_binary_code.append((character, huffman_code))

    len(frozenset(b for a,b in normalised_character_to_huffman_binary_code)) == len(normalised_character_to_huffman_binary_code), 'we have conflicting binary representations of huffman_codes'

    # Build Tree
    root = Tree()
    for character, huffman_code in normalised_character_to_huffman_binary_code:
        t = root
        for binary_digit, _is_last in is_last(huffman_code):
            if binary_digit == '0':
                t.left = t.left or (character if _is_last else Tree())
                t = t.left
            if binary_digit == '1':
                t.right = t.right or (character if _is_last else Tree())
                t = t.right

    return root

def _normalise_depths_to_bytes(normalised_depths: tuple[int]) -> bytes:
    r"""
    >>> _normalise_depths_to_bytes(range(16))
    b'\x01#Eg\x89\xab\xcd\xef'

    I'm encoding each bit depth into 4 bits (16 values) - this may not be enough - need to investigate!
    """
    #assert len(normalised_depths) == 256
    return bytes.fromhex(''.join('{:x}'.format(i) for i in normalised_depths))
def _bytes_to_normalise_depths(data: bytes) -> tuple[int]:
    r"""
    >>> _bytes_to_normalise_depths(b'\x01#Eg\x89\xab\xcd\xef')
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    """
    #assert len(data) == 128
    return tuple(int(c, base=16) for c in data.hex())


def _encode(source) -> bytes:
    """
    >>> tuple(bytes_iterator(io.BytesIO(b"abc")))
    (97, 98, 99)
    >>> tuple(_encode(b'abc'))
    b''
    """
    normalised_depths = _normalise_depths_from_tree(_build_tree_from_data(bytes_iterator(source)))
    yield from iter(_normalise_depths_to_bytes(normalised_depths))
    lookup = _tree_from_normalised_depths(normalised_depths).dict

    if hasattr(source, 'seek'):
        length = source.tell()
        source.seek(0)
    else:
        length = len(source)
    #yield length  # as 16bit usinged int? use struct?

    def _bit_stream(source):
        # reading bytes from the source, lookup the huffman tuple (0,1)'s (should be less than 8 bits)
        # this is a continuious stream of these lookups
        for byte in bytes_iterator(source):
            yield from lookup[byte]
    it = _bit_stream(source)
    b = 'NonNull'
    while any(b):
        # Convert batches of 8 bits at a time back to bytes
        b = tuple(next(it) for b in range(8))
        yield bit_iter_to_byte(b)




# def _decode(data: bytes) -> bytes:
#     """
#     >>> _decode(b'')
#     b'AAAAACGTTATGCCTA'
#     """
#     return b''
#     t = root
#     for byte in bytes_iterator(source):
#         for bit in bit_iterator(byte):
#             if bit:
#                 t = t.left
#             else:
#                 t = t.right
#             if isinstance(t, Tree):
#                 continue
#             else:
#                 yield t
#                 t = root

