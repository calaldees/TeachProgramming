"""
DNS Server and Request Tools

This is a learning tool to understand DNS.
Professional developers would not implement this themselves.


https://datatracker.ietf.org/doc/html/rfc1035
https://routley.io/posts/hand-writing-dns-messages/
https://wiki.python.org/moin/UdpCommunication
"""

import socket
import struct
import random
import inspect

from pprint import pprint
import logging
from typing import NamedTuple
import typing

DEFAULT_PORT = 5353

log = logging.getLogger(__name__)


# Utils -----------------

class Header(NamedTuple):
    ID: int
    query: int
    QDCOUNT: int # Number of questions
    ANCOUNT: int # Number of answers
    NSCOUNT: int # Number of authority records
    ARCOUNT: int # Number of additional records

    _STRUCT = '>HHHHHH'

    @classmethod
    def new(cls, ID=None, QDCOUNT=1, ANCOUNT=0, NSCOUNT=0, ARCOUNT=0, **kwargs):
        """
        from https://routley.io/posts/hand-writing-dns-messages/
        >>> Header.new(ID=0xaaab).bytes.hex('-')
        'aa-ab-01-00-00-01-00-00-00-00-00-00'
        """
        return cls(ID or random.randint(0,pow(2,16)), cls._encode_query(**kwargs), QDCOUNT, ANCOUNT, NSCOUNT, ARCOUNT)

    @property
    def bytes(self):
        return struct.pack(self._STRUCT, *self)

    @classmethod
    def from_bytes(cls, data):
        """
        >>> header = Header.from_bytes(bytes.fromhex('aa-ab-01-00-00-01-00-00-00-00-00-00'.replace('-','')))
        >>> header
        Header(ID=43691, query=256, QDCOUNT=1, ANCOUNT=0, NSCOUNT=0, ARCOUNT=0)
        >>> header.QR
        0
        >>> header.Opcode
        0
        >>> header.TC
        0
        >>> header.RD
        1
        """
        return cls._make(struct.unpack(cls._STRUCT, data))

    @property
    def QR(self):
        # TODO: unsure if this works
        return (self.query & 0b1000000000000000) >> 15
    @property
    def Opcode(self):
        # TODO: unsure if this works
        return (self.query & 0b0111100000000000) >> 11
    @property
    def TC(self):
        # TODO: unsure if this works
        return (self.query & 0b0000001000000000) >> 9
    @property
    def RD(self):
        return (self.query & 0b0000000100000000) >> 8

    @staticmethod
    def _encode_query(QR=0, Opcode=0, TC=0, RD=1, AA=0, RA=0, Z=0, RCODE=0):
        """
        Old lookups
        _lookups = {
            'QR': {  # query_or_response
                'query': 0,
                'response': 1,
            }[QR],
            'Opcode': {
                'query': 0,
                'inverse_query': 1,
                'server_status': 2,
            }[Opcode],
            'TC': {  # truncated
                False: 0,
                True: 1,
            }[TC],
            'RD': {  # recursive
                False: 0,
                True: 1,
            }[RD],
        }
        """
        q = 0
        q += QR
        q <<= 4 ; q += Opcode
        q <<= 1 ; q += AA
        q <<= 1 ; q += TC
        q <<= 1 ; q += RD
        q <<= 1 ; q += RA
        q <<= 3 ; q += Z
        q <<= 4 ; q += RCODE
        return q


_QTYPE = typing.Literal['A',]
_QCLASS = typing.Literal['IN',]

class Question(NamedTuple):
    QNAME: str
    QTYPE: _QTYPE
    QCLASS: _QCLASS

    @classmethod
    def new(cls, QNAME, QTYPE='A', QCLASS='IN'):
        """
        from https://routley.io/posts/hand-writing-dns-messages/
        >>> Question.new('example.com').bytes.hex('-')
        '07-65-78-61-6d-70-6c-65-03-63-6f-6d-00-00-01-00-01'
        """
        return Question(QNAME, QTYPE, QCLASS)

    @property
    def bytes(self):
        data = b''
        for qname_segment in self.QNAME.encode('utf-8').split(b'.'):
            data += bytes([len(qname_segment)]) + qname_segment
        return data + bytes([0x00]) + struct.pack('>HH', self._QTYPE, self._QCLASS)

    @classmethod
    def from_bytes(cls, data):
        raise NotImplemented()
        return Question()

    @property
    def _QTYPE(self):
        return {
            'A': 1,
        }[self.QTYPE]

    @property
    def _QCLASS(self):
        return {
            'IN': 1,
        }[self.QCLASS]


# ------------------------------------------------------------------------------

def dns_request(data):
    """
    """
    pass


# Server -----------------------------------------------------------------------
def server(host_proxy, lookup_file, port, **kwargs):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", port))
    while True:
        data, addr = sock.recvfrom(4098)
        log.debug("received message: %s" % data)

        header = Header.from_bytes(data[0:12])
        for question in range(header.QDCOUNT):
            log.info('todo decode question')
            


# Request ----------------------------------------------------------------------

def request(name, host, **kwargs):
    host, port = host.split(':')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(Header.new().bytes + Question.new(name).bytes, (host, int(port)))


# Commandlin Args --------------------------------------------------------------

def get_args():
    import argparse

    parser = argparse.ArgumentParser(
        prog=__name__,
        description='''
            DNS Tools
        ''',
    )
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_server = subparsers.add_parser('server', help='launch a dns server')
    parser_server.set_defaults(parser='server')
    parser_server.add_argument('--host_proxy', action='store', default='', help='googles dns = 8.8.8.8:53')
    parser_server.add_argument('--lookup_file', action='store', default='', help='')
    parser_server.add_argument('--port', action='store', default=DEFAULT_PORT, type=int, help='')

    parser_request = subparsers.add_parser('request', help='make a dns request')
    parser_request.set_defaults(parser='request')
    parser_request.add_argument('name', action='store', default='example.com', help='')
    parser_request.add_argument('--host', action='store', default=f'127.0.0.1:{DEFAULT_PORT}', help='')

    parser.add_argument('--log_level', action='store', type=int, help='loglevel of output to stdout', default=logging.INFO)

    kwargs = vars(parser.parse_args())
    return kwargs



if __name__ == "__main__":
    kwargs = get_args()
    logging.basicConfig(level=kwargs['log_level'])

    #pprint(kwargs)
    {
        'server': server,
        'request': request,
    }[kwargs['parser']](**kwargs)
