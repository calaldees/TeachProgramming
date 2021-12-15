import math
import io
import struct
from typing import NamedTuple


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
    #"custom": lambda p: p,
}

class Oscillator():
    # consider cloning https://developer.mozilla.org/en-US/docs/Web/API/OscillatorNode
    def __init__(self, oscillator_function=sine, sample_rate=44100, bit_depth=16):
        self.sample_rate = sample_rate
        self.bit_depth = bit_depth
        self.MAX_POSITIVE_INT = (pow(2, self.bit_depth) - 2) // 2 # `//2` because two's complement
        self.oscillator_function = oscillator_function
        self.o = io.BytesIO()
    @property
    def num_bytes(self):
        return self.o.getbuffer().nbytes
    @property
    def samples(self):
        return self.o.getbuffer().nbytes // self.bit_depth // 8
    def add_full_oscillation(self, note=440):
        oscillation_samples = self.sample_rate // note * 2
        for s in (
            int(self.oscillator_function(s/oscillation_samples)*self.MAX_POSITIVE_INT) 
            for s in range(oscillation_samples)
        ):
            self.o.write(struct.pack('h', s))


class WAVHeader(NamedTuple):
    channels: int  # 1
    sample_rate: int  # 44100
    bits_per_sample: int  # 16

    @property
    def byte_rate(self):
        return (self.sample_rate * self.bits_per_sample * self.channels) // 8
    @property
    def block_align(self):
        """
        The number of bytes for one sample including all channels. 
        """
        return (self.channels * self.bits_per_sample) // 8

    def data_size(self, num_samples):
        return num_samples * self.block_align

    def encode(self, Subchunk2Size):
        """
        http://soundfile.sapp.org/doc/WaveFormat/
        http://www.topherlee.com/software/pcm-tut-wavformat.html
        """
        return b'RIFF' + struct.pack('<I', 36 + Subchunk2Size) + b'WAVEfmt ' + struct.pack(
            '<IHHIIHH',
            16,                     # Subchunk size 1 = number of bytes below
            1,                      # 2bytes H  `1=pcm format` values other than one indicate some form of compression
            self.channels,          # 2bytes H
            self.sample_rate,       # 4bytes I
            self.byte_rate,         # 4bytes I
            self.block_align,       # 2bytes H
            self.bits_per_sample,   # 2bytes H
        ) + b'data' + struct.pack('<I', Subchunk2Size)


if __name__ == "__main__":
    wh = WAVHeader(channels=1, sample_rate=44100, bits_per_sample=16)

    o = Oscillator(sine)
    for i in range(200):
        o.add_full_oscillation()

    with open('test2.wav', 'wb') as f:
        f.write(wh.encode(o.num_bytes))
        f.write(o.o.getbuffer())
