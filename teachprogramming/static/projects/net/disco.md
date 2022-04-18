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


```javascript
document.body.style = "margin:0; background-color:black;"  // remove the default html border
```

```javascript
function iframe(url) {
  document.body.innerHTML = `<iframe style="width: 100%; height: 100%;" src="${url}" frameborder="0" allowfullscreen></iframe>`
}
iframe("https://canterbury.ac.uk/")
```

```javascript
function youtube(video_id) {
  iframe(`https://www.youtube.com/embed/${video_id}?&autoplay=1`)
}
youtube("0jjeOYMjmDU")
```

```javascript
function image(image_url) {
  document.body.innerHTML = `<img style="width: 100%; height: 100%; object-fit: cover;" src="${image_url}">`
}
image("https://upload.wikimedia.org/wikipedia/commons/6/60/Augustine_Abbey.jpg")
```

```javascript
function media(url) {
  document.body.innerHTML = `<video controls autoplay style="width: 100%; height: 100%; object-fit: contain;"><source src="${url}"></video>`
}
media("https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_1280_10MG.mp4")
```
consider `mute` and `loop` and `controls`

```javascript
function speak(text) {
  window.speechSynthesis.speak(new SpeechSynthesisUtterance(text));
}
speak('Hello World');
```

```javascript
function text(text) {
  document.body.innerHTML = `<p>${text}</p>`
}
text('Hello World');
// TODO: set font size and color and font? center? wrap?
// Animation? scroll in?
```


* Browser [Event reference](https://developer.mozilla.org/en-US/docs/Web/Events#event_listing)
```javascript
const $text = document.createElement('div');
document.body.appendChild($text);
window.addEventListener('pointermove', (event)=>{
    $text.textContent = `x=${Math.round(event.x/window.innerWidth*100)}% y=${Math.round(event.y/window.innerHeight*100)}%`
})
```


Image blur - guess what it is - slowly unblur

This is sort of What chromecast is


text to speach?






control.html + display.html -> comited to same repo with README as to how to launch the server

