"""
https://en.wikipedia.org/wiki/Huffman_coding
https://en.wikipedia.org/wiki/Canonical_Huffman_code
https://www.geeksforgeeks.org/canonical-huffman-coding/
"""

import typing
from functools import reduce
from collections import defaultdict
from queue import PriorityQueue

class Tree():
    def __init__(self, i, left=None, right=None):
        self.i = i
        self.left = left
        self.right = right


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

def _build_tree(data):
    """
    >>> t = _build_tree(b'ABCD' + b'A'*9 + b'C'*14 + b'D'*6)
    >>> t
    WeightTreeItem(weight=33, item=<huffman.Tree object at 0x...>)
    >>> chr(t.item.left)
    'C'
    >>> t.item.right
    <huffman.Tree object at 0x...>
    """
    q = _convert_to_PriorityQueue(_frequency_analysis(data))
    while q.qsize() > 1:
        a, b = q.get(), q.get()
        q.put(WeightTreeItem(a.weight + b.weight, Tree(None, a.item, b.item)))
    return q.get()


def encode(data: bytes) -> bytes:
    """
    >>> encode(b'AAAAACGTTATGCCTA')
    b''
    """
    return b''

def decode(data: bytes) -> bytes:
    """
    >>> decode(b'')
    b'AAAAACGTTATGCCTA'
    """
    return b''
