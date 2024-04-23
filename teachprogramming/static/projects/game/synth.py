import math
import random
from functools import partial
import re

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
        """
        if isinstance(note, int) or isinstance(note, str) and note.isdigit():
            self.midi = int(note)
        else:
            note_str, octave = self.REGEX_NOTE.match(note.upper()).groups()
            self.midi = self.MIDI_C0 + (int(octave)*12) + self.LOOKUP_STR_NOTE[note_str]
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

def num_samples(note_frequency_hz, sample_frequency_hz=SAMPLE_FREQUENCY_HZ):
    return int(sample_frequency_hz / note_frequency_hz * 2)  # number of samples for a full oscillation

def oscillator_generator_8bit_unsigned(func, note_frequency_hz=440):
    s = num_samples(note_frequency_hz)
    return bytes(int((func(i/s)+1)*127) for i in range(s))

OSCILLATOR_SAMPLES = {
    name: oscillator_generator_8bit_unsigned(func)
    # functions that take 0.0 to 1.0 input of progress though osculation and return -1.0 to +1.0 of wave
    for name, func in {
        "sine": lambda x: math.sin(x * math.pi * 2),
        "square": lambda x: 1.0 if x < 0.5 else -1.0,
        "sawtooth": lambda x: (((x+0.5) * 2) % 2) - 1,
        "triangle": lambda x: -(abs((((x+0.25)%1)*4) - 2) - 1),
        "noise": lambda x: random.random()*2-1,
    }.items()
}

def get_frame(sample, index, rate=1.0):
    # TODO interpolation (expand and shrink)
    return sample[index % len(sample)]

def get_sample_bytes(sample_index, size, sample):
    return bytes(map(partial(get_frame, sample), range(sample_index, sample_index+size)))

def scale(data, size):
    if len(data) == size:
        return data
    if size > len(data):
        # upscale
        return None
    if size < len(data):
        # downscale
        return None
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
        audio_bytes = get_samples(self.audio_frame, frame_count, OSCILLATOR_SAMPLES['sine'])
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
