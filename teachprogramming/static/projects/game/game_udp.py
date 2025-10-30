# uv run --with pygame game_udp.py
from collections.abc import Set, Mapping
from typing import Tuple, NamedTuple
import logging
import queue
import json

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
        self.inputs: Set[str] = frozenset()

    @property
    def pos(self) -> Pos:
        return Pos(int(self.x), int(self.y))

    def inc(self) -> None:
        if 'up'    in self.inputs: self.y_vel += -0.1
        if 'down'  in self.inputs: self.y_vel +=  0.1
        if 'left'  in self.inputs: self.x_vel += -0.1
        if 'right' in self.inputs: self.x_vel +=  0.1
        self.x_vel *= 0.99
        self.y_vel *= 0.99
        self.y_vel += float(0.025)
        self.x += self.x_vel
        self.y += self.y_vel

    def get_bytes(self) -> bytes:
        """
        >>> s = Ship()
        >>> breakpoint()
        >>> s.get_bytes()
        b''
        """
        return json.dumps(vars(self)).encode('utf8')
    def set_bytes(self, data: bytes):
        for k,v in json.loads(data).items():
            setattr(self, k, v)

class NetworkThreadQueueUDP():
    class Addr(NamedTuple):
        host: str
        port: int
    class Message(NamedTuple):
        data: bytes = b''
        addr_from: Tuple[str, int] = ('', 0)  # meant to be Addr, but cant
        def __bool__(self) -> bool: return bool(self.data)
    def __init__(self, port:int=5005, default_addr_to:str='127.0.0.1'):
        import socket
        import threading
        import multiprocessing
        self.recv_queue: multiprocessing.Queue[NetworkThreadQueueUDP.Message] = multiprocessing.Queue()
        self.default_addr_to = self.Addr(default_addr_to, port)
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
            self.recv_queue.put_nowait(self.Message(*self.sock.recvfrom(1024)))
    def send(self, data: bytes, addr_to: Addr | None = None) -> None:
        self.sock.sendto(data, addr_to or self.default_addr_to)
    def get(self) -> Message:
        try               : return self.recv_queue.get_nowait()
        except queue.Empty: return self.Message()


class UDPDemo(PygameBase):
    def __init__(self, network: NetworkThreadQueueUDP):
        self.network = network
        self.ship = Ship()
        super().__init__(resolution=(640,360))

    def translate_input(self, mapping: Mapping[int, str]) -> Set[str]:
        return {mapping[key] for key in mapping.keys() if self.keys[key]}

    def loop(self, s, frame):
        while msg := self.network.get():
            pass
            #self.ship.x, self.ship.y = map(float, msg.data.decode('utf8').split(','))
            #s.blit(DEFAULT_IMAGE, (_x, _y))

        self.ship.inputs = self.translate_input({
            pygame.K_UP: 'up',
            pygame.K_DOWN: 'down',
            pygame.K_LEFT: 'left',
            pygame.K_RIGHT: 'right',
        })
        self.ship.inc()
        s.blit(self.ship.image, self.ship.pos)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        #s.blit(DEFAULT_IMAGE, (mouse_x, mouse_y))
        if frame%3 == 0:
            self.network.send(f'{mouse_x},{mouse_y}'.encode('utf8'))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    import sys
    network = NetworkThreadQueueUDP(*sys.argv[1:])
    UDPDemo(network).run()
