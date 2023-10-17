Chat
====

Overview
--------


Server
------

### Cloud Based IDE

* Launch [channelServer](https://github.com/calaldees/channelServer)
    * [GitHub CodeSpaces](https://codespaces.new/calaldees/channelServer?quickstart=1)
        * Make ports public (cant specify this in config)
    * [GitPod](https://gitpod.io/#https://github.com/calaldees/channelServer)

### Local

* git + docker required

```bash
git clone https://github.com/calaldees/channelServer
cd channelServer
ifconfig  # find ip
make run
```

#### Websocket

GitPod connection example - use the `wss://` address e.g.
```javascript
const url = "wss://9873-jade-catfish-9fuxc59i.ws-eu18.gitpod.io/test1.ws"
```

#### TCP (Python)
Python will not work in GitPod. GitPod cannot share plain/raw TCP ports. Ports are proxied through a web-server, so only secure traffic like `wss://`, `https://` is proxied


Printing
--------

Each programming activity should not be more that one side of A4. (More than one page creates cognitive navigation overhead)

* With VSCode Markdown extensions. `Open in Browser`. 
* In Firefox, `ctrl+p`. 
    * 'Pages per sheet: `2`'
    * 'Pages': Custom: `2-3,4-5` (duplex print `char.html` on one page and `chat.py` on the reverse)
    * Scale: `80%`
    * Margins: `Minimum`
    * Two-sided printing: `flip on short edge`
    * Print backgrounds `tick`


Related Projects
----------------
* See [disco.md](disco.md) for an alternate activity.
* [[paint]] for graphical shared whiteboard
* Consider in `copter` sending `player_number:xpos:ypos`->`1:150:93` every alternate frame `frame%2==0`
* Consider udp activity (python)



Slide Notes - exemplar outreach activity (2 hours)
-----------

What technical terms do you know about computer networking?
Brainstorm as many technical terms as possible
(What foundational knowledge do leaners have - active participants straight away)

Have you programming in:
Python, Javascript, Python&Javascript, neither


* Aim
    * Write a program to send and receive data over a network
    * Build technical domain specific terminology
    * Understand some concepts about network client technology
* Key Words
    * Diff
        * `+` `-` Context
    * Event
        * Event Driven Programming
    * Client/Server
        * Echo Server
    * Protocol
        * (each ends message `\n` NEW_LINE)
    * TCP
        * Websocket
        * BiDirectional
        * IP v4 Address Range
    * Keyboard/IDE/Editor
        * Compile/Run `F5`
        * `ctrl+c` stop
        * `F12` (builtin REPL, debugger)
* Key points
    * "Data" is independent of "programming language"
        * Your language is a tool for working with data
    * Professional programmers use a 'Diff' to describe changes to code
    * Networked applications often have a Client and a Server
    * The concept of an 'Echo' Server
    * We send raw data as text/bytes
    * we need to define a 'protocol' (http, smtp)


* We have created a VERY simple network chat application
* Proof of identity? Signing?
    * Who sent the offensive message?
* Data types - images?
* Formatting?
* Data storage
    * Where stored?
    * WhatsApp/Signal don't store on server
    * Facebook/Discord stored on server
* Multiple Servers?
    * My implementation can probably handle 100 to 1000 connections
    * Different languages (systems level)





---

<style>
@media print {
    hr {display: none;}
    h1 {page-break-before: always;}
    h1:first-of-type {page-break-before: avoid;}
}
pre[class*="language-"] {background-color: #e7e7e7; border: 1px grey solid;} /* code blocks print visibly on paper*/
.token.inserted {font-weight: bolder; color: green;}
.token.deleted {text-decoration: line-through; color: red;}
</style>

---

chat.html
=========

Create a file called `chat.html` and open it in a browser.
Run the program after each section by refreshing your browser with the `F5` key.
See extra debug/errors with `F12` (Or `Shift+Option+Command+c` on Safari after enabling devtools in Preferences).

### base
```html
<!DOCTYPE html>
<html>
<head>
    <title>Chat Client</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Chat Client</h1>
<script>

</script></body></html>
```

### connect
Replace `localhost` with the servers websocket url. (Starts with `wss://` or `ws:/`).
```diff
 <script>
 
+const url = "ws://localhost:9800/test1.ws"
+const socket = new WebSocket(url)
+
 </script></body></html>
```
Look at the server to see if your IP address connected.

### send_one
```diff
 const socket = new WebSocket(url)
 
+function open() {
+    socket.send("Hello I am JAVASCRIPT"+"\n")
+}
+socket.addEventListener("open", open)
+
 </script></body></html>
```
Look at the server to see if the server received your message.

### send
```diff
-    socket.send("Hello I am JAVASCRIPT"+"\n")
+    socket.send(prompt()+"\n")
 }
 socket.addEventListener("open", open)
```
Type a message and press enter. See if the server got your message.

### recv
```diff
 socket.addEventListener("open", open)
+ 
+function receive(msg) {
+    console.log("got: " + msg.data)
+}
+socket.addEventListener("message", receive)
```
See messages by showing devtools `F12` and viewing `console`.

### gui
```diff
     <h1>Chat Client</h1>
+    <input    id="text_field" style="width:300px;" />
```
```diff
 const socket = new WebSocket(url)
 
-function open() {
-    socket.send(prompt()+"\n")
-}
-socket.addEventListener("open", open)

+const text_field = document.getElementById("text_field")
+function textEventKeyDown(event) {
+    if (event.key=='Enter') {
+        socket.send(text_field.value+"\n")
+        text_field.value = ""
+    }
+}
+text_field.addEventListener("keydown", textEventKeyDown, true)
 
 function receive(msg) {
```

### gui_recv
```diff
     <h1>Chat Client</h1>
+    <textarea id="text_area"  style="width:300px;" rows="15" readonly></textarea><br/>
     <input    id="text_field" style="width:300px;" />
```
```diff
+const text_area = document.getElementById("text_area")
 function receive(msg) {
-    console.log("got: " + msg.data)
+    text_area.value = text_area.value + msg.data
 }
 socket.addEventListener("message", receive)
```

### gui_scroll
```diff
 function receive(msg) {
     text_area.value = text_area.value + msg.data
+    text_area.scrollTop = text_area.scrollHeight
 }
```

### gui_username
```diff
     if (event.keyCode==13) {
-        socket.send(text_field.value+"\n")
+        socket.send("Yourname: "+text_field.value+"\n")
         text_field.value = ""
```

<!--PAGE BREAK --><hr style="page-break-after: always;"/>

chat.py
=======

Create a file `chat.py`.
Run the program after each addition in a terminal with `python chat.py`. If using IDLE run with `F5`.
Stop the program with `ctrl+c`

### base
```python
import socket, threading
```

### connect
Replace `localhost` with the servers IP address example: `192.168.0.1`
```diff
 import socket, threading
 
+address = ("localhost", 9801)
+sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+sock.connect(address)
```
Look at the server to see if your IP address connected.

### send_one
```diff
 sock.connect(address)
 
+sock.sendall('Hello I am PYTHON\n'.encode('utf-8'))
```
Look at the server to see if the server received your message.

### send
```diff
 sock.sendall('Hello I am PYTHON\n'.encode('utf-8'))
+while True:
+    print("type something:")
+    sock.sendall(f'{input()}\n'.encode('utf-8'))
```
Type a message and press enter. See if the server got your message.

### recv
```diff
 sock.connect(address)
 
+def connection(sock):
+    while True:
+        data_recv = sock.recv(4098)
+        if not data_recv:
+            break
+        print(data_recv)
+    sock.close()
+connection(sock)
+
 sock.sendall('Hello I am PYTHON\n'.encode('utf-8'))
```
You will need to wait to be sent a message to see it. You cannot send messages in this state.

Windows Only Issue: `ctrl+c` does not stop the program until another message is received. Press `ctrl+c` and wait patently.

### send_recv
```diff
-connection(sock)
 
+thread = threading.Thread(target=connection, args=(sock,))
+thread.daemon=True
+thread.start()
```
Windows Only Issue: Windows terminal blocks on `input()` - received messages are displayed garbled and only after sending a message.
<!-- TODO: consider async python -->

### gui
```diff
 import socket, threading
+import tkinter
```
```diff
 sock.connect(address)
+ 
+root = tkinter.Tk()
+root.title("Chat Client")
+input_box = tkinter.Entry(root)
+input_box.pack(fill=tkinter.BOTH)
+def handle_user_input(e):
+    sock.sendall(f'{input_box.get()}\n'.encode('utf-8'))
+    input_box.delete(0, tkinter.END)
+input_box.bind("<KeyRelease-Return>", handle_user_input)
+input_box.focus_set()

 def connection(sock):
```
```diff
-sock.sendall('Hello I am PYTHON\n'.encode('utf-8'))
-while True:
-    print("type something:")
-    sock.sendall(f'{input()}\n'.encode('utf-8'))
+
+root.mainloop()
```

### gui_recv
```diff
 import tkinter
+import tkinter.scrolledtext
```
```diff
-        print(data_recv)
+        output_box.insert(tkinter.END, data_recv)
```
```diff
 root.title("Chat Client")
+output_box = tkinter.scrolledtext.ScrolledText(root, width=40, height=15)
+output_box.pack(fill=tkinter.BOTH, expand=1)
 input_box = tkinter.Entry(root)
```

### gui_scroll
```diff
         output_box.insert(tkinter.END, data_recv)
+        output_box.yview(tkinter.END)
```

### gui_username
```diff
-    sock.sendall(f'{input_box.get()}\n'.encode('utf-8'))
+    sock.sendall((f'Yourname: {input_box.get()}\n').encode('utf-8'))
```

### (bonus) http request
(only `http` not `https`)
```diff
-address = ("localhost", 9801)
+address = ("neverssl.com", 80)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)
+sock.sendall(b'''GET / HTTP/1.1\r\nHost: neverssl.com\r\nUser-Agent: curl/7.81.0\r\nAccept: */*\r\n\r\n''')
```
Extra: `ping neverssl.com` to get IP address


#### http standalone
```python
import socket
address = ("neverssl.com", 80)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
sock.connect(address)
sock.sendall(b'''GET / HTTP/1.1\r\nHost: neverssl.com\r\nUser-Agent: curl/7.81.0\r\nAccept: */*\r\n\r\n''')
while True:
    response = sock.recv(65535)
    if not response:
        break
    print(response.decode())
sock.close()
```


---

Notes
=====

* [We Need to Talk!! \&ndash; A Chatroom Application Using a Student-Designed Protocol](https://dl.acm.org/doi/10.1145/3304221.3325575)
    * > assignment for a computer networks class in which students design and implement an application-layer protocol for a chatroom using a client-server architecture running over TCP-IP. 
    * > Working collaboratively, students design a single protocol that will be implemented by all class members. 
    * > The protocol is written in a style based on that used in a Request for Comments (RFC), the international standard for describing networking protocols. 
    * > Students work in pairs to implement the protocol using a programming technology of their choice. This experience helps students to understand that different applications can communicate when they are all designed according to the same RFC specification.
    * > Students are free to choose any programming technology to implement the protocol

Other similar concepts
----------------------
* [Building a Replit to Replit Chat App Using Node.js](https://docs.replit.com/tutorials/15-repl-chat)
* [kchat](https://github.com/srpeck/kchat) -  Persistent group chat in <50 lines using kdb+/k/q web sockets and JS
* [kkuchta / css-only-chat](https://github.com/kkuchta/css-only-chat) -  A truly monstrous async web chat using no JS whatsoever on the frontend 

Old/Alternative Server (for reference)
----------------------
Previous server reference
```bash
curl -O https://raw.githubusercontent.com/superLimitBreak/multisocketServer/master/multisocketServer/server/multisocket_server.py
python3 multisocket_server.py --show_messages
```
