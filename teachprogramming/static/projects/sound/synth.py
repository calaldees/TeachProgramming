import math
import random
from functools import partial
import re
from typing import NamedTuple
import typing as t
import csv
from pathlib import Path


#Something to consider https://sfxr.me/ online js sound effect generator



class Note():
    """
    https://en.wikipedia.org/wiki/Scientific_pitch_notation
    """
    LOOKUP_NOTE_STR = {0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}
    LOOKUP_STR_NOTE = {text: note for note, text in LOOKUP_NOTE_STR.items()}
    MIDI_C0 = 12
    REGEX_NOTE = re.compile(r'([ABCDEFG]#?)(-?\d{1,2})')
    @classmethod
    def parse(cls, note):
        """
        >>> Note.parse(60).midi
        60
        >>> Note.parse('60').midi
        60
        >>> Note.parse('C-1').midi
        0
        >>> Note.parse('C0').midi
        12
        >>> Note.parse('C4').midi
        60
        >>> Note.parse('C#4').midi
        61
        >>> Note.parse('A4').midi
        69
        >>> Note.parse('G9').midi
        127

        >>> Note.parse('^^')
        '^^'
        """
        if isinstance(note, int) or isinstance(note, str) and note.isdigit():
            return Note(int(note))
        elif isinstance(note, str) and (match:=cls.REGEX_NOTE.match(note.upper())):
            note_str, octave = match.groups()
            return Note(cls.MIDI_C0 + (int(octave)*12) + cls.LOOKUP_STR_NOTE[note_str])
        return note
    def __init__(self, midi):
        assert isinstance(midi, int) and midi>=0 and midi<=127
        self.midi = midi
    def __eq__(self, obj):
        return isinstance(obj, Note) and obj.midi == self.midi
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
        see wikipedia article for formula
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
    # Annoyingly a full oscillation (one up + one down) is actually 2hz. So the code (s_hz/n_hz*2) makes a 220 wave when the n_hz is 440
    return int(sample_frequency_hz / note_frequency_hz * 2)


class Sample():
    @staticmethod
    def from_oscillator(func, hz:float=440, sample_frequency_hz:int=SAMPLE_FREQUENCY_HZ):
        s = num_samples_for_full_oscillation(hz)
        data = bytes(int((func(i/s)+1)*127) for i in range(s))
        return Sample(data, hz=hz, sample_frequency_hz=sample_frequency_hz, loop=True)
    @staticmethod
    def from_file(p:Path, **kwargs):
        return Sample(p.read_bytes(), **kwargs)
    def __init__(self, data:bytes, hz:float=440, sample_frequency_hz:int=SAMPLE_FREQUENCY_HZ, loop:bool=False):
        self.data = data
        self.hz = hz
    def get_value_at(self, index:float):
        """
        >>> s = Sample(bytes((4,3,2,1,6)))
        >>> s.get_value_at(1)
        3
        >>> s.get_value_at(1.5)
        2.5
        >>> s.get_value_at(3.5)
        3.5
        """
        s = self.data
        i = int(index)
        a = s[(i  )%len(s)]
        b = s[(i+1)%len(s)]
        return (b-a)*(index%1) + a


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


SAMPLES = {
    name: Sample.from_oscillator(func)
    # functions that take 0.0 to 1.0 input of progress though osculation and return -1.0 to +1.0 of wave
    for name, func in {
        "sine": sine,
        "square": square,
        "sawtooth": sawtooth,
        "triangle": triangle,
        "noise": noise,
    }.items()
} | {
    name: Sample.from_file(name)
    for name in map(Path, (
        'piano-everlast.raw',
    ))
}



class TrackNote():
    def __init__(self, start_pos:int, end_pos:int, note:Note, sample:Sample=None):
        self.start_pos:int = start_pos
        self.end_pos:int = end_pos
        self.note:Note = note
        self.sample:Sample = sample
    def __str__(self) -> str:
        # "C#4 13 .."  tracker style
        raise NotImplementedError()
    def __repr__(self) -> str:
        return f'{self.note}'  # TODO: fixed width?
    def value_at(self, pos:float):
        if pos < self.start_pos or pos > self.end_pos:
            return None
        return self.sample.get_value_at((pos-self.start_pos)/(self.sample.hz/self.note.hz))



class Track():
    @staticmethod
    def from_file(p:Path):
        with p.open() as f:
            meta = f.readline()  # todo - parse meta first line
            # maybe the first row of the CSV is a base64 encoded sample for each channel?
            return Track(rows=tuple(tuple(map(Note.parse, row)) for row in csv.reader(f)))
    @staticmethod
    def _Notes_to_TrackNotes(rows: tuple[tuple[Note]]) -> tuple[tuple[TrackNote]]:
        """
        >>> nn = Track._Notes_to_TrackNotes((
        ...     tuple(map(Note.parse, ('A4', 'C4', 'F4', None))),
        ...     tuple(map(Note.parse, ('C4', '^^', 'G4', None))),
        ...     tuple(map(Note.parse, ('^^', 'None', '^^', None))),
        ... ))
        >>> nn[0][0].note = Note.parse('A4')
        """
        active_notes = [None] * 8  # HACK - hard code to 8 channels max
        def _active_note(row:int, channel:int, note:Note):
            if active_notes[channel]:
                active_notes[channel].end_pos = row
            if isinstance(note, Note):
                active_notes[channel] = TrackNote(start_pos=row, end_pos=row, note=note)
            if note == "^^":
                active_notes[channel] = None
            return active_notes[channel]
        return tuple(
            tuple(_active_note(row, channel, note) for channel, note in enumerate(notes))
            for row, notes in enumerate(rows)
        )
    def __init__(self, rows:tuple[tuple[Note]], bpm=90):
        self.bpm = bpm
        self.rows = self._Notes_to_TrackNotes(rows)
    def notes_at(self, pos:int) -> tuple[TrackNote]:
        return self.rows[pos%len(self.rows)]

class Player():
    def __init__(self, track:Track, SAMPLE_FREQUENCY_HZ:int=22050):
        self.track = track
        self.SAMPLE_FREQUENCY_HZ = SAMPLE_FREQUENCY_HZ
    def frame_to_pos(self, frame) -> float:
        """
        >>> class MockTrack():
        ...    bpm = 120
        >>> p = Player(MockTrack)
        >>> p.frame_to_pos(0)
        0.0
        >>> p.frame_to_pos(22050)
        2.0
        >>> p.frame_to_pos(44100)
        4.0
        """
        return frame/self.SAMPLE_FREQUENCY_HZ/60*self.track.bpm
    def values_at(self, pos:float) -> tuple[int]:  # actually tuple[int or None] - ready for mixing!
        # there is something not quite right here - the pos relates to bpm - so need to think about note.value_at
        return tuple(note.value_at(pos) for note in self.track.notes_at(int(pos)))
    def get_sample_bytes(self, frame, frame_count):
        return bytes(
            self.mix(self.values_at(self.frame_to_pos(_frame)))
            for _frame in range(frame, frame+frame_count)
        )
    @staticmethod
    def mix(values):
        values = tuple(filter(None, values))
        return int(sum(values)/len(values))


tt = Track.from_file(Path('synth.csv'))
# TODO: Consider live reloading of track edit - filewatch
#breakpoint()

import pyaudio
class Audio():
    def __init__(self):
        self.pyaudio = pyaudio.PyAudio()
        self.audio_frame = 0
        self.audio_stream = self.pyaudio.open(format=pyaudio.paUInt8, channels=1, rate=SAMPLE_FREQUENCY_HZ, output=True, stream_callback=self.pyaudio_stream_callback)
    def pyaudio_stream_callback(self, in_data, frame_count, time_info, status):
        audio_bytes = get_sample_bytes(self.audio_frame, frame_count, SAMPLES['sine'])
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
        audio_bytes = get_sample_bytes(self.audio_frame, frame_count, SAMPLES['sine'])
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
