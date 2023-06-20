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
    1.0
    >>> square(0.75)
    -1.0
    >>> square(1)
    -1.0
    """
    return 1.0 if x <= 0.5 else -1.0
    return float(-((round(x)*2)-1))  # branchless? which is faster? the float cast could be expensive

OSCILLATOR_TYPES = {
    "sine": sine,
    "square": square,
    "sawtooth": sawtooth,
    "triangle": triangle,
    #"custom": lambda p: p,
}

class Oscillator():
    """
    Consider
        Realtime Output
            https://python-sounddevice.readthedocs.io/en/0.4.3/examples.html
        Copying JS ossilator methods
            https://developer.mozilla.org/en-US/docs/Web/API/OscillatorNode
    WAV 16bit+ are signed integers
    WAV 8bit are unsigned (nice consistency?)
    """
    def __init__(self, oscillator_function=sine, sample_rate=44100, bit_depth=16):
        self.oscillator_function = oscillator_function
        self.sample_rate = sample_rate
        self.bit_depth = bit_depth
        self.MAX_POSITIVE_INT = (pow(2, self.bit_depth) - 2) // 2 # `//2` because two's complement
        self.o = io.BytesIO()
    @property
    def num_bytes(self):
        return self.o.getbuffer().nbytes
    @property
    def samples(self):
        return self.o.getbuffer().nbytes // self.bit_depth // 8
    @property
    def bytes(self):
        data = self.o.getvalue()
        self.o.seek(0)
        self.o.truncate(0)
        return data
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

    def header(self, Subchunk2Size):
        r"""
        http://soundfile.sapp.org/doc/WaveFormat/
        http://www.topherlee.com/software/pcm-tut-wavformat.html

        >>> WAVHeader(channels=1, sample_rate=44100, bits_per_sample=16).header(128)
        b'RIFF\xa4\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00D\xac\x00\x00\x88X\x01\x00\x02\x00\x10\x00data\x80\x00\x00\x00'
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


def play_pyaudio(o):
    # See more at 
    #    https://python.plainenglish.io/build-your-own-python-synthesizer-part-3-162796b7d351
    # pip install pyaudio
    try:
        import pyaudio
    except ImportError:
        return

    p = pyaudio.PyAudio()

    # blocking
    #stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True)
    #stream.write(o.o.getvalue())

    # stream
    buffer = bytearray()
    def _callback(in_data, frame_count, time_info, status):
        nonlocal buffer
        target_bytes = frame_count * 2  #16bits
        while (len(buffer) + o.num_bytes) < target_bytes:
            o.add_full_oscillation()
        buffer += o.bytes
        (out, buffer[:]) = (bytes(buffer[:target_bytes]), buffer[target_bytes:])
        return (out, pyaudio.paContinue)
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, stream_callback=_callback)

    import time
    while stream.is_active():
        time.sleep(0.1)

    stream.close()
    p.terminate()


def play_simpleaudio(o):
    try:
        import simpleaudio as sa
    except ImportError as ex:
        print("simpleaudio not installed")
        return
    # https://simpleaudio.readthedocs.io/en/latest/tutorial.html#playing-audio-directly
    play_obj = sa.play_buffer(o.o.getbuffer(), 1, 2, 44100)
    play_obj = play_obj.play()
    play_obj.wait_done()

    # Could not install this on windows - what a pain
    # choco install microsoft-visual-cpp-build-tools
    # pip install simpleaudio
    # https://stackoverflow.com/questions/67312738/error-command-errored-out-with-exit-status-1-python-when-installing-simple
    # https://www.lfd.uci.edu/~gohlke/pythonlibs/#simpleaudio
    # pip install https://download.lfd.uci.edu/pythonlibs/archived/simpleaudio-1.0.4-cp310-cp310-win_amd64.whl



if __name__ == "__main__":
    wh = WAVHeader(channels=1, sample_rate=44100, bits_per_sample=16)

    o = Oscillator(sine)
    for i in range(200):
        o.add_full_oscillation()

    with open('test2.wav', 'wb') as f:
        f.write(wh.header(o.num_bytes))
        f.write(o.o.getbuffer())

    play_pyaudio(o)


# Consider
# js synth
# https://dev.to/ndesmic/building-a-digital-synthesizer-part-2-octaves-power-and-chords-991
# * [A Young Person's Guide to the Principles of Music Synthesis](http://beausievers.com/synth/synthbasics/)
# Realtime python audio output
# https://python-sounddevice.readthedocs.io/en/0.4.3/examples.html#creating-an-asyncio-generator-for-audio-blocks