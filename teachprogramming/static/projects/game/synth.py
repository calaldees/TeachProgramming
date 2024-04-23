import math
import random
from functools import partial


def oscillator_generator_8bit_unsigned(func, sample_frequency_hz, note_frequency_hz=440):
    num_samples = int(sample_frequency_hz / note_frequency_hz * 2)  # number of samples for a full oscillation
    return bytes(int((func(s/num_samples)+1) * 127) for s in range(num_samples))

OSCILLATOR_SAMPLES = {
    name: oscillator_generator_8bit_unsigned(func, 22050)
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

import pyaudio
class Audio():
    def __init__(self):
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
