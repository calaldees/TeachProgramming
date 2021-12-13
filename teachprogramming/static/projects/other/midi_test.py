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
    i, v, _ = message
    i -= 224
    v *= 2
    if i<0 or i>=8:
        return
    print(f'{i}:{v}')
    #breakpoint()
    dmx[i] = v
    artnet.dmx(bytes(dmx))
midi_in.set_callback(handle_input)


import time
while True:
    time.sleep(1)



