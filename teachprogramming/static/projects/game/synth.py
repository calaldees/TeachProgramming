import math
import io
import struct

import pygame

from pygame_test import GameBase

class Oscillator():
    def __init__(self, frequency):
        self.frequency = frequency
        self.o = io.BytesIO()
    @property
    def samples(self):
        return self.o.getbuffer().nbytes / 2 # 2 bytes ber sample as 16bit
    def add_full_oscillation(self, note=440):
        oscillation_samples = int(self.frequency / note)
        for s in (int(math.sin((s/oscillation_samples)*math.pi*2)*(pow(2, 16)-2)/2) for s in range(oscillation_samples)):
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
            o = Oscillator(self.frequency)
            #while (o.samples < self.frame_samples):
            for i in range(1000):
                o.add_full_oscillation()
            self.channel.queue(pygame.mixer.Sound(buffer=o.o.getbuffer()))
            #self.channel.play(pygame.mixer.Sound(buffer=bytes(tt)))


if __name__ == '__main__':
    Game().run()
