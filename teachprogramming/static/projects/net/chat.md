Chat
====

Consider asyncIO python server with both tcp and websockets in repl?

* [Building a Replit to Replit Chat App Using Node.js](https://docs.replit.com/tutorials/15-repl-chat)


```bash
curl -O https://raw.githubusercontent.com/superLimitBreak/multisocketServer/master/multisocketServer/server/multisocket_server.py
python3 multisocket_server.py --show_messages
```

GitPod connection example - replace this line
```javascript
var socket     = new WebSocket("wss://9873-jade-catfish-9fuxc59i.ws-eu18.gitpod.io/");         // VER: connect
```

See [disco.md](disco.md)


* [We Need to Talk!! &ndash; A Chatroom Application Using a Student-Designed Protocol](https://dl.acm.org/doi/10.1145/3304221.3325575)
    * > assignment for a computer networks class in which students design and implement an application-layer protocol for a chatroom using a client-server architecture running over TCP-IP. 
    * > Working collaboratively, students design a single protocol that will be implemented by all class members. 
    * > The protocol is written in a style based on that used in a Request for Comments (RFC), the international standard for describing networking protocols. 
    * > Students work in pairs to implement the protocol using a programming technology of their choice. This experience helps students to understand that different applications can communicate when they are all designed according to the same RFC specification.
    * > Students are free to choose any programming technology to implement the protocol
