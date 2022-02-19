from itertools import chain
from functools import cached_property
import struct
from datetime import datetime
import typing
try:
    from typing_extensions import Self
except ImportError as ex:
    Self = None

from hash import fnv1 as HASH_FUNC


class Block(typing.NamedTuple):
    previous_block: Self
    hash: int
    length: int
    datetime: datetime
    pos: int
    filehandle: typing.BinaryIO

    BLOCK_HEADER_FORMAT = 'QQdQ'
    @classmethod
    def from_filehandle(Class, previous_block: Self, filehandle: typing.BinaryIO) -> Self:
        header_binary = filehandle.read(struct.calcsize(Class.BLOCK_HEADER_FORMAT))
        if not header_binary:
            return
        _hash, _length, _timestamp, _pos = struct.unpack(Class.BLOCK_HEADER_FORMAT, header_binary)
        assert _pos == filehandle.tell()
        filehandle.seek(_pos + _length)
        return Class(previous_block, _hash, _length, datetime.fromtimestamp(_timestamp), _pos, filehandle)

    @classmethod
    def add_block(Class, previous_block: Self, filehandle: typing.BinaryIO, data: bytes):
        if previous_block:
            assert previous_block.isvalid
            previous_block_hash = previous_block.hash
            filehandle.seek(previous_block.pos + previous_block.length)
        else:
            previous_block_hash = 0
            assert filehandle.tell() == 0
        start_pos = filehandle.tell()
        # calc new block fields
        _length = len(data)
        _datetime = datetime.now().timestamp()
        _pos = start_pos + struct.calcsize(Class.BLOCK_HEADER_FORMAT)
        _hash_bytes = struct.pack(Class.BLOCK_HEADER_FORMAT, previous_block_hash, _length, _datetime, _pos)
        _hash = HASH_FUNC(chain(_hash_bytes, data))
        # write new block to file
        filehandle.seek(start_pos)
        filehandle.write(struct.pack(Class.BLOCK_HEADER_FORMAT, _hash, _length, _datetime, _pos))
        filehandle.write(data)
        filehandle.seek(start_pos)
        # read written block from file as return
        return Class.from_filehandle(previous_block, filehandle)

    @property
    def data(self) -> bytes:
        self.filehandle.seek(self.pos)
        return self.filehandle.read(self.length)

    @property
    def hash_calculated(self) -> int:  # TODO: some duplication with `add_block`. Consider removing duplication?
        previous_block_hash = (self.previous_block and self.previous_block.hash) or 0
        _hash_bytes = struct.pack(self.BLOCK_HEADER_FORMAT, previous_block_hash, self.length, self.datetime.timestamp(), self.pos)
        return HASH_FUNC(chain(_hash_bytes, self.data))

    @property
    def isvalid(self) -> bool:
        return self.hash == self.hash_calculated


class BlockChain():
    def __init__(self, filehandle: typing.BinaryIO):
        self.filehandle = filehandle
        self.last_block = None
        block = None
        while block := Block.from_filehandle(block, self.filehandle):
            self.last_block = block
    @property
    def blocks(self) -> typing.Iterable[Block]:
        if not self.last_block: return
        block = self.last_block
        yield block
        while block := block.previous_block: 
            yield block
    @property
    def isvalid(self) -> bool:
        return all(block.isvalid for block in self.blocks)
    def add_block(self, data: bytes):
        self.last_block = Block.add_block(self.last_block, self.filehandle, data)


def _test_blockchain():
    """
    >>> import io

    Create a new blockchain
    >>> bb = BlockChain(io.BytesIO())
    >>> bb.add_block(b'abc')
    >>> bb.add_block(b'def')
    >>> [b.data for b in bb.blocks]
    [b'def', b'abc']
    >>> [b.isvalid for b in bb.blocks]
    [True, True]
    >>> bb.isvalid
    True

    Test loading from filehandle
    >>> bb.filehandle.seek(0)
    0
    >>> cc = BlockChain(bb.filehandle)
    >>> [b.data for b in cc.blocks]
    [b'def', b'abc']

    Test corrupting data
    >>> bb.filehandle.seek(next(bb.blocks).pos+1)
    68
    >>> bb.filehandle.write(b'x')
    1
    >>> [b.data for b in bb.blocks]
    [b'dxf', b'abc']
    >>> [b.isvalid for b in bb.blocks]
    [False, True]
    >>> bb.isvalid
    False
    """
    pass
