Disco
=====

School activity for KS3, KS4, KS5.

https://github.com/calaldees/channelServer
Run in GitPod or Repl
TODO - what are the external address's?


Real industry tools


Keywords
--------

### Computing
Javascript
Event
Event Driven Programming
WebSocket
Protocol
BiDirectional
RGB
Distributed System
(Network) Message Bus
Port
Latency
Synchronisation (A problem, NTP)

### Other
BPM


Activity
--------

Where could the delay/latency come from?
Think pair share - all the places

Advanced Design
---------------

The server has no logic - we send lots of irrelevant information to each node


Followup
========

Presenter project

Remote control - with buttons and text box's. Slider? color picker?
Receiver - image, text, video (mp4, youtube), redirect-webpage (frame?) (need snippets)
video that moves from left to right (timed?)

```
<iframe width="560" height="315" src="https://www.youtube.com/embed/[Video ID]I?&autoplay=1" frameborder="0" allowfullscreen></iframe>
```

Image blur - guess what it is - slowly unblur

This is sort of What chromecast is


text to speach?

https://stackoverflow.com/a/22234035/3356840
```javascript
window.speechSynthesis.speak(new SpeechSynthesisUtterance('Hello World'));
```
```javascript
function say(m) {
  var msg = new SpeechSynthesisUtterance();
  var voices = window.speechSynthesis.getVoices();
  msg.voice = voices[10];
  msg.voiceURI = "native";
  msg.volume = 1;
  msg.rate = 1;
  msg.pitch = 0.8;
  msg.text = m;
  msg.lang = 'en-US';
  speechSynthesis.speak(msg);
```





control.html + display.html -> comited to same repo with README as to how to launch the server

