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


API
---

https://openweathermap.org/api
url='http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1'



Data Transform: Input -> Output
Data Source:
  - REGEX (html)
  - API (json)

Read into dict/lists

Data Output:
  - RSS (template)
  - CSV (library)

Scraping is BAD! - API keys
Beautiful Soup



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