Workshops
=========

Cant tell kids high level concepts - show them
Pretty narly idea of how to teach this - but it works
Secretly you want to go in the ballpool - Especially if your on work time and are being paid.

Disband the Myth
  Learn to code = Load of bollox
  -Adults don't have time
  -Kids don't have focus
  No few hours of workshop is a magic wand

Approach
  - Reference
  - Short 1 A4 examples of real stuff

Goal is to
 - highlight how computers work
 - ignite your interest and attitude
 - tit about and have fun by building something that does something


Chat
----

    curl "https://raw.githubusercontent.com/calaldees/libs/master/python3/lib/multisocket/multisocket_server.py" -O && python3 multisocket_server.py -m
    curl "https://raw.githubusercontent.com/calaldees/TeachProgramming/master/teachprogramming/static/projects/net/chat.py" -O && python3 chat.py

RAW HTTP
--------

telnet www.bbc.co.uk 80

    GET / HTTP/1.1
    Host: www.bbc.co.uk


curl "http://localhost:9872/"





MessageBoard
------------

Previously - How computers communicate
  - Plain text editor
  - Terminal
    - ls
    - cd
    - python
    - ctrl+c
  - Terminology
    - socket
    - server
    - ip address
    - port


MessageBoard
  - files - open - read/append
  - Terminal
    - touch
    - cat
    - curl
    - telnet
  - Terminology
    - Webserver
    - Cookie
    - HTTP GET/POST
  - Discussion
    - Web Security


telnet localhost 8000

    GET /messages.php HTTP/1.1


    POST /messages.php HTTP/1.1
    Cookie: username=Test
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 13

    message=Hello



Youtube embed
Alert
<script type="text/javascript">alert('You have been hacked!');</script>

Use each others messageboards
ifconfig http://{ipAddress}:8000/messages.php



curl -O https://raw.githubusercontent.com/calaldees/TeachProgramming/master/teachprogramming/static/projects/web/web_cgi.py && chmod 755 web_cgi.py
curl -O https://raw.githubusercontent.com/calaldees/TeachProgramming/master/teachprogramming/static/projects/web/messages.py && chmod 755 messages.py
ln -s ./ cgi-bin && touch messages.txt && python -m CGIHTTPServer 8000
python -m webbrowser -t "http://localhost:8000/cgi-bin/messages.py"


SMTP
----

https://users.cs.cf.ac.uk/Dave.Marshall/PERL/node175.html



Realtime graphics and input
---------------------------

* Event loop
* Image Manipulation
  * Transparency
* Web security (chrome)


Data
---

(Questionably Titled - Mining Data Not Data Mining)
Data Aggregation - Definition
Data Mining - Definition

Data Transform: Input -> Output

Data Source:
  - REGEX (html) [twitter, ebay]
  - API (json) [postcode, police crimes, tfl]

Read into 'data structures'
  - dict
  - lists

Data Output:
  - RSS (template)
  - CSV (library)

Scraping is BAD! - API keys
Beautiful Soup
https://openweathermap.org/api
url='http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1'



C/C++ Language Sheet
--------------------

C: gcc example.c -o main -ansi
C++: g++ example.cpp -o main --std=c++11
then run with ./mainno, just put yourself in the folders and
C: gcc example.c -o main -ansi
C++: g++ example.cpp -o main --std=c++11
then run with ./main
you need an "in.txt" file to run the file input
with some lines
the first thing it does is ask you for an input (but it doesnt say that)
so you need to do std input insertion before it does the rest
if you have problems compiling or running just tell me
as you can imagine, C is a lot more basic than C++, doesnt have the nice types
so you dont even know very well the length of the string when you declare it LOL
there are multiple ways of doing it
I went with the simplest
but maybe I should correct it to a more instructive way
line 52:     for (int i = 0; username[i] != '\0'; i++) {
is the smartest way in C, but the most confusing for the people who dont understand
I'd like to see all this compared with Java
side by side :slightly_smiling_face:
when will you be able to show us? :slightly_smiling_face:


Theory
------

Theory – What happens when you type google.com - What a computer actually is – Prepare to have your mind blown (a high octane enlightening talk)
(adders/multiplexers,

[ACTIVITY]
https://medium.freecodecamp.com/the-biggest-codebases-in-history-a128bb3eea73


-- Data --

Binary
Data types
integer (unsigned/singed)
hex
floating point
ASCII
Images (bitmap/vector) Font Rasterisation

compression, (run length, lossy)
JPG example [ACTIVITY]


Data is code - code is data

Von Neumann architecture (date is code and vice versa)
Turing complete machines
Emulators


 -- Hardware --

And (transister)
Or
Not

Adder
Multiplexer

Fetch execute cycle


Low level
Syncronious/Asyncrontouls
Serial/parallal
Parity
Signal Noise
Stop bit

Conrol bus



MAR -> Address bus
MBR -> data bus
PCU
 PC
 CIR -> Instruction decoder -> control circits -> control bus
ALU
Registers

8bit macine
16 bit machine
clock rate
instruction sets


-- Cryptography --

Cryptography RSA
Key exchange problem
CA [Activity]
https/rsa


-- Networks --

WIFI
OSI model
7 layer network stack (wifi is different the ethernet),
switch/hub-bus/csmacd
gateways
routing
traceroute
packet switched netwok
tcp/ip
load balancing

internet, webbrowser and www

DNS Lookup
DHCP


Traceroute [ACTIVITY] - http://www.ip2location.com/free/traceroute
Transatlantic cable - http://www.submarinecablemap.com/#/


-- Data Representation --

set operators
arrays 1d 2d 3d
linked list
stack
queue
graphs (directed/undirected) (adjacency list
trees


-- Languages --

assembly
Compiler
Interpriter

imperitive
functional
event
oo -> inhertence
parallel (channels)

arethmetic operators



--- Algorithums ---

linear search
Binary search

Sorting algorithums
 https://www.youtube.com/watch?v=BeoCbJPuvSE
 https://www.youtube.com/watch?v=kPRA0W1kECg
bubblesort
quicksort (pivot)

Algorithus
 - line crossing
 - traveling salesman
 - shortest path
 - pathfinding
 levenstine distance

recursive algoithums - fibonarchi

 p -> np

How many times can you fold a peice of paper before reaching the moon
http://scienceblogs.com/startswithabang/2009/08/31/paper-folding-to-the-moon/


-- Storage --


SSD
Spinning HD (track, sector
Raid
Parity

-- OS --

operating systems
Single core thredding/scheduling
single core
multicore - paralisation
dining philosophers


-- Protocols --

protocols
http
ftp
smtp
imap


-- Content --

css separarte content from how it looks


-- Databases--

databases
index's
sql
primary key - forigen key
postgis


-- Software engeniering --

Tests

-- Experimental --

gentic algorithums - where the solution is unknown
http://rednuht.org/genetic_cars_2/ [ACTIVITY]

perceptron - AI

