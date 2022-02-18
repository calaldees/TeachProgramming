from functools import cached_property
import struct
from datetime import datetime
import typing

from hash import fnv1 as HASH_FUNC


class Block(typing.NamedTuple):
    previous_block: Block
    hash: int
    length: int
    datetime: datetime
    pos: int
    _filehandle: typing.BinaryIO

    BLOCK_HEADER_FORMAT = 'QQdQ'
    @classmethod
    def from_filehandle(Class, previous_block, filehandle):
        header_binary = filehandle.read(struct.calcsize(Class.BLOCK_INDEX_FORMAT))
        if not header_binary:
            return
        _hash, _length, _timestamp, _pos = struct.unpack(Class.BLOCK_INDEX_FORMAT, header_binary)
        assert _pos == filehandle.tell(), "validation of read block failed, file position does not match"
        filehandle.seek(_pos + _length)
        return Class(previous_block, _hash, _length, datetime.fromtimestamp(_timestamp), _pos, filehandle)

    @property
    def data(self):
        self._filehandle.seek(self.pos)
        return self._filehandle(self.length)

    @cached_property
    def isvalid(self):
        return self.hash == self.hash_calculated

    @cached_property
    def previous_header_bytes(self):
        return struct.pack(self.BLOCK_HEADER_FORMAT, (
            (self.previous_block and self.previous_block.hash) or 0, self.length, self.datetime.timestamp(), self.pos,
        ))

    @cached_property
    def hash_calculated(self):
        return HASH_FUNC(self.data + self.previous_header_bytes)


class BlockChain():
    def __init__(self, filehandle):
        block = None
        while block := Block.from_filehandle(block, filehandle):
            self.last_block = block
    def blocks(self):
        block = self.last_block
        yield block
        while block := block.previous_block:
            yield block
    def isvalid(self):
        return all(block.isvalid for block in self.blocks)
    def add_block(self, data):
        raise NotImplementedError()
