import math
import random
from functools import partial
import re

#Something to consider https://sfxr.me/ online js sound effect generator



class Note():
    """
    https://en.wikipedia.org/wiki/Scientific_pitch_notation
    """
    LOOKUP_NOTE_STR = {0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}
    LOOKUP_STR_NOTE = {text: note for note, text in LOOKUP_NOTE_STR.items()}
    MIDI_C0 = 12
    REGEX_NOTE = re.compile(r'([ABCDEFG]#?)(-?\d{1,2})')
    def __init__(self, note):
        """
        >>> Note(60).midi
        60
        >>> Note('60').midi
        60
        >>> Note('C-1').midi
        0
        >>> Note('C0').midi
        12
        >>> Note('C4').midi
        60
        >>> Note('C#4').midi
        61
        >>> Note('A4').midi
        69
        >>> Note('G9').midi
        127
        >>> Note([])
        Traceback (most recent call last):
        TypeError
        """
        if isinstance(note, int) or isinstance(note, str) and note.isdigit():
            self.midi = int(note)
        elif isinstance(note, str):
            note_str, octave = self.REGEX_NOTE.match(note.upper()).groups()
            self.midi = self.MIDI_C0 + (int(octave)*12) + self.LOOKUP_STR_NOTE[note_str]
        else:
            raise TypeError()
    def __str__(self):
        """
        >>> str(Note(0))
        'C-1'
        >>> str(Note(12))
        'C0'
        >>> str(Note(60))
        'C4'
        >>> str(Note(61))
        'C#4'
        >>> str(Note(69))
        'A4'
        >>> str(Note(127))
        'G9'
        """
        return f"{self.LOOKUP_NOTE_STR[self.midi%12]}{(self.midi-self.MIDI_C0)//12}"
    @property
    def hz(self):
        """
        >>> Note(69).hz
        440.0
        >>> Note(70).hz
        466.1637615180899
        >>> Note(0).hz
        8.175798915643707
        """
        return 440*2**((self.midi-69)/12)

SAMPLE_FREQUENCY_HZ = 22050

def num_samples_for_full_oscillation(note_frequency_hz, sample_frequency_hz=SAMPLE_FREQUENCY_HZ):
    # Annoyingly a full oscillation (one up + one down) is actually 2. So this makes a 220 wave when the input is 440
    return int(sample_frequency_hz / note_frequency_hz * 2)


class Sample():
    def __init__(self, name='', data=None, func=None, note_frequency_hz=440, loop=None):
        assert bool(data) ^ bool(func)
        if data:
            self.data = data
        if func:
            self.data = self.oscillator_generator_8bit_unsigned(func, note_frequency_hz)
        self.note_frequency_hz = note_frequency_hz
    @staticmethod
    def oscillator_generator_8bit_unsigned(func, note_frequency_hz:float=440):
        s = num_samples_for_full_oscillation(note_frequency_hz)
        return bytes(int((func(i/s)+1)*127) for i in range(s))
    def _get_value_at(self, index:float):
        """
        >>> s = Sample(data=bytes((4,3,2,1,6)))
        >>> s._get_value_at(1)
        3
        >>> s._get_value_at(1.5)
        2.5
        >>> s._get_value_at(3.5)
        3.5
        """
        s = self.data
        i = int(index)
        a = s[(i  )%len(s)]
        b = s[(i+1)%len(s)]
        mix = index % 1
        return (a*(1-mix))+(b*(mix))
    def get_frame(self, i1:float, i2:float):
        """
        >>> s = Sample(data=bytes((4,3,2,1,6)))
        >>> s.get_frame(1.0,2.0)
        1.5
        >>> s.get_frame(1.0,3.0)
        2.5

        >> s.get_frame(1,2)
        1
        """
        return sum((
            self._get_value_at(i1),
            sum(self.data[i] for i in range(int(i1)+1, int(i2))),
            self._get_value_at(i2),
        ))/i2-i1
    def resample(self, note_frequency_hz, size=None, start_frame=0):
        data = 0
        return Sample(self.name, data, note_frequency_hz=note_frequency_hz)


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
def noise(x):
    return random.random()*2-1


OSCILLATOR_SAMPLES = {
    name: Sample(func=func)
    # functions that take 0.0 to 1.0 input of progress though osculation and return -1.0 to +1.0 of wave
    for name, func in {
        "sine": sine,
        "square": square,
        "sawtooth": sawtooth,
        "triangle": triangle,
        "noise": noise,
    }.items()
}




# get_frame, get_sample_bytes and resample are not the correct approach.
# I need to get functional with zero state
# each frame should be a float size/width and should increment and be processed each frame


def get_sample_bytes(sample_index, size, sample):
    return bytes(map(partial(get_frame, sample), range(sample_index, sample_index+size)))

def resample(data, size):
    if size > len(data):
        # upscale - linear interpolation
        return bytes(int(get_frame(data, (i/size)*len(data))) for i in range(size))
    elif size < len(data):
        # downscale
        raise NotImplementedError()
    return data
#breakpoint()

import pyaudio
class Audio():
    def __init__(self):
        self.pyaudio = pyaudio.PyAudio()
        self.audio_frame = 0
        self.audio_stream = self.pyaudio.open(format=pyaudio.paUInt8, channels=1, rate=SAMPLE_FREQUENCY_HZ, output=True, stream_callback=self.pyaudio_stream_callback)
    def pyaudio_stream_callback(self, in_data, frame_count, time_info, status):
        audio_bytes = get_sample_bytes(self.audio_frame, frame_count, OSCILLATOR_SAMPLES['sine'])
        self.audio_frame += frame_count
        return (audio_bytes, pyaudio.paContinue)
    def quit(self):
        self.audio_stream.close()
        self.pyaudio.terminate()


from animation_base_pygame import PygameBase
class Game(PygameBase):
    def __init__(self):
        super().__init__()
        self.pyaudio = pyaudio.PyAudio()
        self.audio_frame = 0
        self.audio_stream = self.pyaudio.open(format=pyaudio.paUInt8, channels=1, rate=22050, output=True, stream_callback=self.pyaudio_stream_callback)
    def pyaudio_stream_callback(self, in_data, frame_count, time_info, status):
        audio_bytes = get_sample_bytes(self.audio_frame, frame_count, OSCILLATOR_SAMPLES['sine'])
        self.audio_frame += frame_count
        return (audio_bytes, pyaudio.paContinue)
    def quit(self):
        self.audio_stream.close()
        self.pyaudio.terminate()
    def loop(self, screen, frame):
        print(f"video_frame={frame} audio_frame={self.audio_frame}")


if __name__ == '__main__':
    #Game().run()

    aa = Audio()
    
    #import signal
    #def handler(signum, frame):
    #    aa.quit()
    #signal.signal(signal.SIGINT, handler)

    import time
    while aa.audio_stream.is_active():
        time.sleep(0.1)
