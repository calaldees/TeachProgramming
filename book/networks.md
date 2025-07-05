The Missing Piece - Networks
============================

Back in the 80's and 90's, the Computing spec for schools took shape.
The core tenet's of:
* Variables/Arrays
* Control structures: If/Else, Iteration (bounded and unbounded)
* Functions/Params/Returns
* Logical operators, Arithmetic
* Reading and Writing to files
All of those are fundamental, but they don't allow you to do much.


So what is missing?
-------------------
Why does this spec from the 80's 90's feel so restrictive.
It is the fundamentals of using a computer to perform something useful.

Some might also add _graphics_ and the api's around performing those.
That adds a relatable superpower to the output of young peoples programs.

We've been stuck here for years.
Struggling to teach loops that count from 0 to 10 missing out the odd numbers.


Network Communication
---------------------

* Reading and writing files
* Sending a message over a network (UDP/TCP)
(The unix creators cottoned on to this. Everything is a stream.)


Why is this a revelation?
-------------------------

We now have a useful use case that is the underpinning of our use of computers in society.
Immediately we can count from 0 to 10 but send them over a network to another persons machine.

* Creating programs now becomes more social
    * Working with others
    * Defining specs for what to send
* Demo sending a message via UDP and TCP. Ask an 11 year old "Do we know if the message got to it's destination". 'With UDP, **** knows, with TCP it dies/crashes'.
* The theory is real. Computers have numbers (address's). Ack's. Protocol design is real.
* Immediately reveals language interop (see channel server)


Activities
----------

* Disco lights -> Chromecast
* tictactoe or connect4 over udp
* Copter co-ordinate draw
* Network paint (Careful of TTP)


Tools
-----

* Channel Server (Websocket->TCP/UDP conversion)
    * Pattern: First joiner privileged
        * Allows development of client/server patterns without changing the client tooling (learning a whole new language api/pattern for server).
    * Web shit isn't blocked by most schools. CodeSpaces/GitPod can do this


(Interest)
----------

* [Bill Gates’ Internet Tidal Wave Microsoft memo](https://dfarq.homeip.net/bill-gates-internet-tidal-wave-microsoft-memo/) 1995 (commentary 2025)