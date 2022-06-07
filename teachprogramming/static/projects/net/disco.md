Disco
=====

School activity for KS3, KS4, KS5.


Teacher notes
-------------

### Principle

* Apply/Practical first - to give context - then discuss dissect/understand
* Real industry tools


Keywords
--------

### Computing
* Javascript/browser
* Context + diff
* Event
* Event Driven Programming
* WebSocket
* Protocol
  * version
* BiDirectional
* RGB (color representation)
* Distributed System
* (Network) Message Bus
* Latency
* Synchronisation (A problem, NTP)


### Other discipline/domains
* BPM (Beats per minute)


Activities
----------

* [Launch GitPod - channelServer](https://gitpod.io/#https://github.com/calaldees/channelServer) [github.com/calaldees/channelServer](https://github.com/calaldees/channelServer)
  * See debug page for `test`
  * copy and paste the WS URL from the debug window of `test1`
    * similar to `wss://9800-calaldees-channelserver-0vsy0j7vxzd.ws-eu46.gitpod.io/test1.ws`
* Dev environment
  * setup WS_URL variable beforehand
  * 16:9 screen split in half
    * Plain text editor
      * ctrl + s
    * Web browser (chrome/firefox)
      * ctrl + r
    * ![disco_student_dev_example.gif](disco_student_dev_example.gif)

### Practical - disco.html
* Teacher leads - example
* Gives students sequential `id` numbers
* Demo's bpm
  * single character on keyboard - col count
  * [Caramella Girls - Caramelldansen (Official English Version)](https://www.youtube.com/watch?v=A67ZkAd1wmI) YouTube
    * bpm 167?


Activity
--------

Where could the delay/latency come from?
Think pair share - all the places


Advanced Design
----------------

The server has no logic - we send lots of irrelevant information to each node




---
<style>
.token.inserted {font-weight: bold;}
.token.deleted {text-decoration: line-through;}
</style>
<hr style="page-break-after: always;"/>


# Network Disco Lights - HTML5/Javascript

## Base
Create a file called `disco.html` and open it in a browser
Run the program after each addition by refreshing your browser
```html
<script type="module">
const WS_URL = "ws://localhost:9800/test1.ws"
</script>
```
Open `disco.html` in a web browser
Reload the page each addition by pressing CTRL+F5

Replace `localhost` with URL your teacher gives you.

## Random Screen Color
```diff
 <script type="module">
 const WS_URL = "ws://localhost:9800/test1.ws"
+
+function randomByte() {return Math.floor(Math.random()*255)}
+function updateScreenColor(r,g,b) {
+    r = r || randomByte()
+    g = g || randomByte()
+    b = b || randomByte()
+    document.body.style = `background-color: rgb(${r},${g},${b});`
+}
+
+window.addEventListener('keydown', (event)=>{
+    updateScreenColor()
+})
+
 </script>
```
Press any key on the keyboard

## Listen to Network
```diff
+const socket = new WebSocket(WS_URL)
+window.socket = socket
+socket.addEventListener('message', (event)=>{
+            updateScreenColor()
+})

 </script>
```
When a network message is revived, your screen should change color.

## Protocol Version 1: Computer Id
Change "1" to be a unique Identifier (ID) for your computer. Teacher will give you a number.
```diff
 socket.addEventListener('message', (event)=>{
+        const id = event.data
+        if (id == "1") {
             updateScreenColor()
+        }
 })
```
When your number is sent over a network, your screen should change color.

Press F12 to enable developer tools 'console'.
```javascript
socket.send("1")
```
Change the color of our neighbors screen.

## Protocol Version 2: Color
```diff
 socket.addEventListener('message', (event)=>{
-        const id = event.data
+        const [id, r, g, b] = event.data.split(":")
         if (id == "1") {
-            updateScreenColor()
+            updateScreenColor(r,g,b)
        }
 })
```
In console
```javascript
socket.send("1:255:0:0")
```

## Protocol Version 3: Multiple Computer Id's
```diff
 socket.addEventListener('message', (event)=>{
+    const messages = event.data.split("\n")
+    for (let message of messages) {
-        const [id, r, g, b] = event.data.split(":")
+        const [id, r, g, b] = message.split(":")
         if (id == "1") {
             updateScreenColor(r,g,b)
         }
+    }
 })
```
In console
```javascript
socket.send(`
1:255:0:0
2:0:255:0
3:0:0:255
`)
```

## Calculate BPM
* Calculate the Beats Per Minuet (BPM) of a piece of music
* Count/tally the number of beats over 60 seconds
* Disco Time

## Extra
* Join another channel - replace `test1` for different channels
* Start your own server (GitHub login required)
  * https://gitpod.io#https://github.com/calaldees/channelServer


Teacher Notes
=============

```html
<script type="module">

const urlParams = new URLSearchParams(window.location.search)
const WS_URL = urlParams.get('ws_url') || "ws://localhost:9800/test1.ws"
const ID = urlParams.get('id')
// For transmitting sequence
const BPM = parseInt(urlParams.get('bpm') || 60)
const IDS = parseInt(urlParams.get('ids') || 8)


function randomByte() {return Math.floor(Math.random()*255)}
function updateScreenColor(r,g,b) {
    r = r || randomByte()
    g = g || randomByte()
    b = b || randomByte()
    document.body.style = `background-color: rgb(${r},${g},${b});`
}

// Keyboard event
window.addEventListener('keydown', (event)=>{
    updateScreenColor()
})

// Websocket event
const socket = new WebSocket(WS_URL);
window.socket = socket
socket.addEventListener('message', (event)=>{
    //console.log(event.data);
    if (!ID) {updateScreenColor(); return;}

    const messages = event.data.split('\n')
    for (let message of messages) {
        const [id, r, g, b] = message.split(":")
        if (ID == id) {
            updateScreenColor(r,g,b)
        }
    }
})

// -----------------------------------------------------------------------------

const COLORS = [
    [255,0,0], //red
    [255,255,0], //yellow
    [0,255,0], // green
    [0,255,255], // cyan
    [0,0,255], // blue
    [255,0,255], // magenta
]
export function* range(target, start=0, step=1) {for (let i=start ; i<target ; i+=step) {yield i}}

function generate_disco_message_for_frame(frame) {
    const bar = Math.floor(frame/8)
    return [...range(IDS)].map((id)=>{
        const id_offset = (id+frame)%4==0?1:0
        const COLOR = COLORS[(bar + id_offset) % COLORS.length]
        return [id,].concat(COLOR).join(":")
    }).join("\n")
}

// this is a terrible timing loop as it drifts
const sleep = (milliseconds) => new Promise((resolve, reject) => setTimeout(resolve, milliseconds))
async function call_on_bpm(bpm, call, duration_seconds=60) {
    const iterations = bpm * (duration_seconds / 60)
    const wait_in_milliseconds = 1 / (bpm / 60) * 1000
    console.log("Starting disco for", duration_seconds, "BPM", bpm, "wait_in_milliseconds", wait_in_milliseconds, "iterations", iterations)
    for (let frame=0 ; frame <= iterations ; frame++) {
        call(frame)
        await sleep(wait_in_milliseconds)
    }
}

function start_disco(duration_seconds=60) {
    call_on_bpm(
        BPM, 
        (frame)=>{
            const msg = generate_disco_message_for_frame(frame)
            console.log(msg)
            socket.send(msg)
        },
        duration_seconds=duration_seconds,
    )
}
window.start_disco = start_disco

// Use with 
// file:///C:/Users/.../disco.html?&ids=30&bpm=167&ws_url=wss://9800-XXX-channelserver-XXX.ws-XXX.gitpod.io/test1.ws
// type `start_disco(duration_seconds=60)` in console
</script>
```

### To complement: Protocol Version 1: Computer Id

Send 30 separate messages
```javascript
for (let id=0 ; id<30 ; id++) {socket.send(`${id}`)}  // Whole room!
```
Inefficient


---
<hr style="page-break-after: always;"/>

Remote Control Project
======================

display.html
------------

Display - image, text, video (mp4, youtube), redirect-webpage (frame?) (need snippets)


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
function youtube(video_id, start_seconds=0) {
  iframe(`https://www.youtube.com/embed/${video_id}?&autoplay=1&start=${start_seconds}`)
}
youtube("0jjeOYMjmDU")
```

```javascript
function image(image_url) {
  document.body.innerHTML = `<img style="width: 100%; height: 100%; object-fit: cover;" src="${image_url}">`
}
image("https://upload.wikimedia.org/wikipedia/commons/6/60/Augustine_Abbey.jpg")
// todo: animate, fade, blur
```

```javascript
function media(url) {
  document.body.innerHTML = `<video controls autoplay style="width: 100%; height: 100%; object-fit: contain;"><source src="${url}"></video>`
}
media("https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_1280_10MG.mp4")
// or mp3/ogg
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


```javascript
const renderer_functions = {iframe, youtube, image, media, speak, text}

const function_name, payload = event.data.split("---")
renderer_functions[function_name](payload)
```
Explain use `---` as split character. Don't use `:` because this is a legal character in urls


control.html
------------

Remote control - with buttons and text box's. Slider? color picker?

```javascript
const button = document.createElement("button")
button.textContent = "Console Hello"
button.addEventListener("click", ()=>console.log("hello"))
document.body.appendChild(button)
```

```html
<h1>Test</h1>

<button id="button1">Test Button 1</button>

<input type="text" id="text1"/>
<button id="button2">Test Button 2 - from textbox</button>

<label for="points">Points (between 0 and 10):</label>
<input type="range" id="points" name="points" min="0" max="10"> 

<script type="module">
    function do_thing(text) {
        console.log(text)
    }

    document.getElementById("button1").addEventListener("click", ()=>{
        do_thing('hello1')
    })

    document.getElementById("button2").addEventListener("click", ()=>{
        const text = document.getElementById("text1").value
        do_thing(`Text in the box is ${text}`)
    })
</script>
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




control.html + display.html -> comited to same repo with README as to how to launch the server