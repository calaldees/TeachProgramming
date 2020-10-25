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
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def depth_of_nodes(self):
        """
        >>> t = Tree(left='C', right=Tree(left=Tree(left='D', right='A'), right='B'))
        >>> tuple(t.depth_of_nodes())
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
        q.put(WeightTreeItem(a.weight + b.weight, Tree(a.item, b.item)))
    return q.get()

def _normalise_tree_depths(tree):
    """
    #>>> t = Tree(left=3, right=Tree(left=Tree(left=4, right=1), right=2))
    >>> t = _build_tree(bytes(range(256)))
    >>> _normalise_tree_depths(t)
    """
    i_depth = sorted((i, depth) for depth, i in sorted(tree.depth_of_nodes()))
    def pop_if_match(i):
        if i_depth:
            _i, _depth = i_depth[0]
            if i == _i:
                i_depth.pop(0)
                return _depth
        return 0
    return tuple(pop_if_match(i) for i in range(256))


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
