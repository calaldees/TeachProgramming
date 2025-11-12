import re
import random
import math
from typing import Self, NamedTuple


class Note():
    """
    todo: make this a namedtuple? that way its immutable and can be joined with `+`?
    https://en.wikipedia.org/wiki/Scientific_pitch_notation
    """
    LOOKUP_NOTE_STR = {0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}
    LOOKUP_STR_NOTE = {text: note for note, text in LOOKUP_NOTE_STR.items()}
    MIDI_C0 = 12
    REGEX_NOTE = re.compile(r'([ABCDEFG]#?)(-?\d{1,2})')
    @classmethod
    def parse(cls, note: str) -> Self:
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
            return cls(int(note))
        elif isinstance(note, str) and (match:=cls.REGEX_NOTE.match(note.upper())):
            note_str, octave = match.groups()
            return cls(cls.MIDI_C0 + (int(octave)*12) + cls.LOOKUP_STR_NOTE[note_str])
        raise ValueError(f'Unable to parse {cls.__class__.__name__}: {note}')
    def __init__(self, midi: int):
        assert isinstance(midi, int) and midi>=0 and midi<=127
        self.midi = midi
    def __eq__(self, obj) -> bool:
        return isinstance(obj, Note) and obj.midi == self.midi
    def __str__(self) -> str:
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
    def hz(self) -> float:
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
