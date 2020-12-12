import math
import io
import struct

import pygame

from pygame_test import GameBase

def sine(x):
    """
    >>> def _sine(x):
    ...    return round(sine(x), 4)
    >>> _sine(0)
    0.0
    >>> _sine(0.25)
    1.0
    >>> _sine(0.5)
    0.0
    >>> _sine(0.75)
    -1.0
    >>> _sine(1)
    -0.0
    """
    return math.sin(x * math.pi * 2)
def triangle(x):
    """
    >>> triangle(0)
    -0.0
    >>> triangle(0.25)
    1.0
    >>> triangle(0.5)
    -0.0
    >>> triangle(0.75)
    -1.0
    >>> triangle(1)
    -0.0
    """
    return -(abs((((x+0.25)%1)*4) - 2) - 1)
def sawtooth(x):
    """
    >>> sawtooth(0)
    0.0
    >>> sawtooth(0.25)
    0.5
    >>> sawtooth(0.5)
    -1.0
    >>> sawtooth(0.75)
    -0.5
    >>> sawtooth(1)
    0.0
    """
    return (((x+0.5) * 2) % 2) - 1
def square(x):
    """
    https://en.wikipedia.org/wiki/Square_wave
    >>> square(0)
    1.0
    >>> square(0.25)
    1.0
    >>> square(0.5)
    -1.0
    >>> square(0.75)
    -1.0
    >>> square(1)
    -1.0
    """
    return 1.0 if x < 0.5 else -1.0
OSCILLATOR_TYPES = {
    "sine": sine,
    "square": square,
    "sawtooth": sawtooth,
    "triangle": triangle,
    "custom": lambda p: p,
}
class Oscillator():
    # consider cloning https://developer.mozilla.org/en-US/docs/Web/API/OscillatorNode
    def __init__(self, frequency, _type="sine"):
        self.frequency = frequency
        self.f = OSCILLATOR_TYPES[_type]
        self.o = io.BytesIO()
    @property
    def samples(self):
        return self.o.getbuffer().nbytes / 2 # 2 bytes ber sample as 16bit
    def add_full_oscillation(self, note=440):
        oscillation_samples = int(self.frequency / note * 2)
        for s in (int(self.f(s/oscillation_samples)*(pow(2, 16)-2)/2) for s in range(oscillation_samples)):
            self.o.write(struct.pack('h', s))

class Game(GameBase):
    def __init__(self):
        self.s = None
        self.c = None
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
        super().__init__()
        self.channel = pygame.mixer.Channel(0)
        self.frequency, sample_bits, channels = pygame.mixer.get_init()
        self.frame_samples = int(self.frequency / self.fps)
    def loop(self, screen, frame):
        if frame == 10:
            #ff = ((frame//60) % 7) + 1
            #ff = 24
            #tt = tuple(int((math.sin(i/ff)*128)+127) for i in range(self.frame_samples*60))
            #self.channel.play(pygame.mixer.Sound(buffer=bytes(tt)))
            o = Oscillator(self.frequency, _type="square")
            #while (o.samples < self.frame_samples):
            for i in range(1000):
                o.add_full_oscillation(note=220)
            self.channel.queue(pygame.mixer.Sound(buffer=o.o.getbuffer()))
            #self.channel.play(pygame.mixer.Sound(buffer=bytes(tt)))


if __name__ == '__main__':
    Game().run()
