Mini 8bit Synth/Tracker
=======================

8BitUnsigned+NearestNeighbor (hard coded? or flexable?)
All typed as just bytes unsigned - super simple as possible

* Output
    * audio device
    * wav file
    * Could be 16/24bit mixing? Samples rate 11khz,22khz,44,48,96khz?
* Input
    * Track CSV
    * Realtime events (mapped to sample/channel - keep tack of playing sfx/sample and add channels)
        * Midi
        * sfx event
    * Zip file or folder
* Tracker and SFX are separate modules that use the sample mixer?
* (just samples) Pre generate sample
    * sin
    * saw
    * triangle
    * etc, by function
    * Possible multi-wave patch?
* (position to function? to allow fm synthesis?)
* 8bit per channel
* Interpolation of samples
    * Nearest neighbor
    * Linear
    * Cubic?


8bitzTr4k0r
-----

8BitUnsigned
Tracker+SFX
CSV+base64samples
One lines Funcs to generate sin,saw,tri,sq samples

Consider small implementation for javascript, C#, Python
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array
Uint8Array.fromBase64()
Uint8Array()
https://gist.github.com/JorenSix/f0bf4dc9635db41e587528ddf06c2c57
    context.decodeAudioData(audioBuffer, function(buffer) {
    //
    var source    = context.createBufferSource();
    source.buffer = buffer;
    source.connect(context.destination);
    if (nextTime == 0)
        nextTime = context.currentTime + 0.02;  /// add 50ms latency to work well across systems - tune this if you like
    source.start(nextTime);
    nextTime += source.buffer.duration;
https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext/createBufferSource
    Seems to have a stream of a random sample
