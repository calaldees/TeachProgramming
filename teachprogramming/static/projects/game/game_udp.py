# uv run --with pygame game_udp.py
from collections.abc import Set
from typing import Tuple, NamedTuple
import socket
import threading
import multiprocessing
import logging
import queue

import pygame

from animation_base_pygame import PygameBase


log = logging.getLogger(__name__)

DEFAULT_IMAGE = pygame.image.load("images/ship.gif")

class Pos(NamedTuple):
    x: int
    y: int

class Ship():
    def __init__(self, image:pygame.image=DEFAULT_IMAGE, x:float=0, y:float=0):
        self.image = image
        self.x:float = x
        self.y:float = y
        self.x_vel:float = 0.0
        self.y_vel:float = 0.0

    @property
    def pos(self) -> Pos:
        return Pos(int(self.x), int(self.y))

    def inc(self, inputs: Set = frozenset()) -> None:
        if 'up'    in inputs: self.y_vel += -0.1
        if 'down'  in inputs: self.y_vel +=  0.1
        if 'left'  in inputs: self.x_vel += -0.1
        if 'right' in inputs: self.x_vel +=  0.1
        self.x_vel *= 0.99
        self.y_vel *= 0.99
        self.y_vel += float(0.025)
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel


class NetworkUDP():
    class Addr(NamedTuple):
        host: str
        port: int
    class UDPMessage(NamedTuple):
        data: bytes = b''
        addr_from: Tuple[str, int] = ('', 0)  # meant to be Addr, but cant
        def __bool__(self) -> bool: return bool(self.data)
    def __init__(self, addr_to='127.0.0.1', port=5005):
        self.recv_queue: multiprocessing.Queue[NetworkUDP.UDPMessage] = multiprocessing.Queue()
        self.addr_to = self.Addr(addr_to, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.sock.bind(('0.0.0.0', port))
        except OSError:
            log.warning('cant bind socket - is another client is already running on this port?')
        thread = threading.Thread(target=self._recv_thread)
        thread.daemon=True
        thread.start()
    def _recv_thread(self) -> None:
        while True:
            self.recv_queue.put_nowait(self.UDPMessage(*self.sock.recvfrom(1024)))
    def send(self, data: bytes, addr_to: Addr | None = None) -> None:
        self.sock.sendto(data, addr_to or self.addr_to)
    def get(self) -> UDPMessage:
        try               : return self.recv_queue.get_nowait()
        except queue.Empty: return self.UDPMessage()


class UDPDemo(PygameBase):
    def __init__(self, network: NetworkUDP):
        self.network = network
        self.ship = Ship()
        super().__init__(resolution=(640,360))

    def loop(self, s, frame):
        while msg := self.network.get():
            self.ship.x, self.ship.y = map(float, msg.data.decode('utf8').split(','))
            #s.blit(DEFAULT_IMAGE, (_x, _y))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        #s.blit(DEFAULT_IMAGE, (mouse_x, mouse_y))
        if frame%3 == 0:
            self.network.send(f'{mouse_x},{mouse_y}'.encode('utf8'))

        s.blit(self.ship.image, self.ship.pos)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    import sys
    UDPDemo(NetworkUDP(*sys.argv[1:])).run()
