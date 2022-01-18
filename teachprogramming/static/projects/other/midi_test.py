# ?? maybe uneeded? choco install visualcpp-build-tools
# pip install --upgrade setuptools
# pip3 install --user --pre python-rtmidi

# pip install -e libs
# curl https://raw.githubusercontent.com/superLimitBreak/stageOrchestration/master/stageOrchestration/lighting/output/realtime/dmx/ArtNet3.py -O
from ArtNet3 import ArtNet3
artnet = ArtNet3('192.168.0.111')
dmx = [0] * 16

import signal
def ctrl_handler(signum, frm):
    print("You can't cannot kill me")
    exit()
signal.signal(signal.SIGINT, ctrl_handler)


import rtmidi
midi_in = rtmidi.MidiIn()
print(midi_in.get_ports())  # ['Arturia MiniLab mkII 0', 'loopMIDI Port 1']
midi_in.open_port(1)

def handle_input(event, data=None):
    message, deltatime = event
    #print(f'message: {message}, deltatime: {deltatime}, data: {data}')
    i, v, _ = message  # input (slider number), value
    i -= 224  # for the nanoKONTROL I was using, the first slider is numbered 224 (probably encoding cc-channel and other stuff in this, but the sliders are sequential so subtracting a constant is enough)
    v << 1  #v *= 2  # midi values are 7bit 0-127 we need to expand this to 0-255 8bit
    if i<0 or i>=8:  # only use the first 8 sliders of the nanoKONTROL - anything outside this ignore
        return
    print(f'{i}:{v}')
    #breakpoint()
    dmx[i] = v
    artnet.dmx(bytes(dmx))
midi_in.set_callback(handle_input)


import time
while True:
    time.sleep(1)



