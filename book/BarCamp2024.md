BarCamp 2024
============

* I've worked in secondary schools, taught at HE/University, contracted to run code clubs, trained secondary computing teacher across Kent.
* I have left education.
* I wasn't intending to present this. Most of my thoughts are not fully formed, but I hope consolidating some ideas in a talk will help me work though some ideas. I figured that this talk would be reasonably universal and interesting to the attendees at BarCamp.


* How did you learn your tech skills?

<details>

* My hunch is that many of your cite your own interest.
* It's possible, but unlikely you had a great teacher.
</details>



Preface: Computing Education Sux
--------------------------------

### Expectation vs Qualification

* Q: What is young peoples experience/perception of Computing?
  * Mobile phones? Youtube? ChatGPT? Hackers? VR? 3D open world games?
  * Now you enter your GCSE class and we do
    * Hex to binary
    * 3 months of network theory
    * (Neither of those are relevant to the young persons)
  * The Computing GCSE is not relevant to most young people
    * [Number of girls in England taking computing GCSE plummets, study finds](https://www.theguardian.com/technology/article/2024/jun/27/number-of-girls-in-england-taking-computing-gcse-plummets-study-finds)
      * > Introduction of new syllabus may be reason number of girls taking subject more than halved in eight years, academics say
* Q: So what is important for young people?
  * The grand answer: Self actualization and altering the world though self action and building something
  * The simple answer: Choose to build shit

### Qualifications vs Certification

* Academia is broken untrustworthy shit - Many CS graduates don't know CS and cant build anything - Many courses are of poor quality
* Professional Citification are gaining momentum and prove competence in a field rather than ephemeral low value CS degrees and school curriculums.



Solution (Part 1 or 2): The intangible fluffy stuff
----------------------

* Not everyone can code and should code. There are way better things long term they can work towards that are more useful.
* Everyone should enjoy building something with autonomy (and that something may be with code)

The only way to get the exposure (time) and challenge (appropriate difficulty) is self direction


### Children should be bored

* [Children should be allowed to get bored, expert says](https://www.bbc.co.uk/news/education-21895704) BBC March 2023
  * To develop autonomy and creativity
  * We have robbed our young people of this opportunity
* [Teenagers who watch screens in free time 'do worse in GCSEs'](https://www.theguardian.com/education/2015/sep/04/teenagers-who-watch-screens-in-free-time-do-worse-in-gcses)

### Learner Autonomy

Learner Autonomy rather than 74+ exercises in order.

#### My 52 week experiment
I failed - experiment over lockdown. 52 weeks. 2 motivated learners. I layed out a fantastic 52 weeks of perfect progression. I failed to take into account autonomy. If all a learner does is move on to exercise 37 out of 78, it does not work.
Only a small minority of people can access education presented in a cold linear fashion.

Q: What demographic/characteristics can access this education?

<details>

* Obedient (indoctrinated that education is important)
* Affluent (the learner has a quiet space to focus - Most children don't have access to a desk and quiet space. Just their mobile phone in a shared bedroom)
* Autistic?

Who can sit for hours and hours in a seat doing stuff they are told to do?
</details>


#### Game-ification is counter to autonomy

* Game-ification of content erodes autonomy and should not be used
  * > You get 50 stars if you complete this exercise - you have 279 stars currently - your next level of silver is at 300 stars
  * This is not developing intrinsic motivation and puts the leaner as a controlled subject rather than developing there own autonomy
  * I would consider this strategy over the long term dangerous.


### Identity Comes before skill

* Example: "The guitar kid"


### Stop using ...

* Realtime manipuation of state - you can see and feel your code manifest into reality ... but
* 'Games' to teach programming
  * The entirety of all of computing ... and the only think you can think of that has worth is trivially using it for entertainment. Thats lame.
  * Focusing on games alienate some demographics and trivializes the discipline.
  * e.g. my [[dna]] activity


Solution (Part 2 of 2): The tangible stuff
-----------------------

### Assessment

Students need a framework to:
* identify where they are
* rate/rank/measure/critique others

It has to be something an 11 year old can do. and scale to 18+


* Complexity (11 years old + can use this same grid)
	* Have you used a variable?
	* Have you used a function?
	* Have you used one paramiter?
	* have you used two paramiters?
	* Does your function return something?
	* Does your function call another function?
	* Have you created a function that calls itself?
	* Do you have a loop?
	* Have you used bounded iteration
	* Have you used unbounded iteration
	* Have you used a loop within a loop
* > “The spirit and style of student assessment defines the de facto curriculum.”  Rowntree (Reference Rowntree1977)

Why is networks always only taught as theory?
Use Dig, whois, bitwise xor a subnet mask, use curl -vvv, send UDP packets
The multisocket server


### Same Surface Different Depth (SSDD)



### Typing speed

* You cant engage with coding if you cant use a keyboard. You need a keyboard because you need 4 different types of brackets and quotes.
* Touch screen keyboard are not sufficient. Drag and drop is not sufficient. Audio transcription is not sufficient.
* Every week, measure your number (Year 7 to Year 9?) (I only know one school that does this)

### Pair Programming


* If you can say it or write it, your don't know it
* Equal access to machine (2 keyboards)
* That's how you actually build something
* Conveying ideas + feedback are essential
  * (kid in the bedroom just strumming the same chords and noone to tell them the way there wrist is angled is preventing them from making progress)


### Cheat Sheet

(foundation to use all languages without fear)

https://computingteachers.uk/static/langauge_reference.html#py,vb

* Learners understand/identify the abstract concepts, not fixated on the particular incarnation of brackets
* Learners feel they can progress (another language is not that hard once you know the concept in one language)
* l33t hax0rs can do the exercises in lua, C or golang while the rest of the class are plodding though in python. (Even 6th formers)


### Guided Engineering Projects

* Build real things of value, incrementally from a diff
  * (nay-sayers will call this 'just copying' but this is short sighted)

* rational
  * build something with low skill set
  * feel what is possible
  * build a mental reference (I've sent messages across a network before .. when did I do that?)

Make something ..see it work ...  then disect it
Build actual shit make it real


#### Project Examples

* [channelServer](https://github.com/calaldees/channelServer) - WebSocket, TCP, UDP - Echo server
  * The secret network sauce
* [Copter](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/docs/copter.py.pdf) [[copter]]
* [MessageBoard]()
* [Font](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/projects/graphics/font/font.md) + Demoscene [[font]]
* [Disco](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/docs/disco.pdf) Lights + Chromecast [[disco]]
* [Chat](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/docs/Network%20Chat%20(js%20python).pdf) [[chat]]
* [Map](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/projects/web/harry-potter-map/index.html) Marauders map? (concept)
* Engineering projects (diffs: many computing teachers don't know what this)
  * Copter, Chat, NetworkWhiteboard
* Real
  * Escape room
  * Wearables (creativity)

* etextiles - wearables - fashion
    * Strips of LEDs
    * https://learn.adafruit.com/gemma-led-sneakers
    * https://learn.adafruit.com/category/led-strips
    * https://learn.adafruit.com/cardboard-obsidian-sword
    * https://learn.adafruit.com/sound-activated-shark-mask


#### Higher level (degree? 6thform)
* Web Module - add a feature after someone else
  * [WebProgramming](https://github.com/calaldees/frameworks_and_languages_module/blob/main/docs/future/WebProgramming.md)
* [Frameworks and Languages module](https://github.com/calaldees/frameworks_and_languages_module/tree/main/docs)







Hardware
--------

* You cant code on a mobile phone or tablet


Programming Environment
-----------------------

### Visual Abstractions

* Visual programming abstractions are not effective.
  * Hard things are hard. There are no short cuts. Learn the tools/principles not the colours.
  * Text IS the code, not the colors of the text.
  * frame-based editing may have legs - as this does not undermine the focus on text
  * [From Blocks to Professional Development – Thoughts on the Future of Educational Programming](https://dl.acm.org/doi/10.1145/3605468.3609785) Kölling 2023
      * > block-based systems built around structure editors almost exclusively used for early programming instruction to young learners,
        > and professional environments that use text-based languages and are edited at character level.
        > Here, we argue that combining the two approaches into a single system can have benefits. We discuss frame-based editing, a combination of text and blocks, and its potential to improve the landscape of programming education




Lesson Meta
-----------

* [Pedagogy by proxy: developing computing PCK through shared lesson resources](https://sure.sunderland.ac.uk/id/eprint/13728/) Hidson, Elizabeth (2021)
  * Most lesson resources don't include metadata about _why_ the approach was chosen



Undocumented Future
------------

* Largely, my computing education work is undocumented.
* They are not documented enough for another computing teacher to utilise them
* I have considered a _book_? But have no idea where to begin
* As I have left the education profession. I currently have no outlet to education and much of my work is set to be left to atrophy

* I now sit in an office and write code behind closed office doors. I get paid. I will repeat this until I retire.

* What do I do?