TeachProgramming
================

History
-------

Years ago I created this repo to store a range of code I used for teaching young people how to code.

It evolved into a dynamic website that showed the incremental code for small games in a range of languages. Next to the code was runnable browser based html5 version of what the code would look like.

Over the years I added more coding examples. Many of these new examples were not visual or interactive like the game ideas.

One resource stood out. A language cheat sheet for multiple languages. This was a binary file (openoffice document) that was periodicity updated.
Many of the code examples did not actually work. They had never been through a compiler/interpreter and caused much frustration for learners.

Eventually these code snippets made their way into runnable code files. The concept to build the cheat sheet from these was never completed.


The Plan
--------

This repo is a mess. The pyramid webserver project needs to be disposed of.
The new plan is to make a data API that can serve all of the versions of the programs (as complete programs or diffs) so that they can be rendered (hopefully trivially) by a frontend.
The same technology that can show incremental bits of games in multiple languages could also be used for the generating the cheat sheet.

Step 1: create data api
Step 2: consider how to display the data (online or printable)

I'm not going to start a whole new repository because I think the journey is reasonably interesting.
I will move this repo out into an organization so that other can collaborate on it.
I will move it once it's been tidied up a bit.

Other similar projects?
-----------------------

### Language reference

* see [language_reference/README.md](teachprogramming/static/language_reference/README.md)

### Projects (in steps)

https://github.com/algorithm-archivists/algorithm-archive
* [executable-tutorials](https://github.com/dharmatech/executable-tutorials)
    * mechanism for doing what my version system sort of accomplishes
* [Code Tour: VSCode Extension](https://marketplace.visualstudio.com/items?itemName=vsls-contrib.codetour)
* [Storyteller](https://markm208.github.io/)
    * [markm208/storyteller](https://github.com/markm208/storyteller) Telling stories about how code evolves
    * web navigable animations
* [codeamigo.dev](https://codeamigo.dev/)
    * online tutorials with steps
* [textframe.app](https://textframe.app/)
    * Text documentation commentary with animated/tweened preview inline
    * A similar concept to my projects



Groups
------

* [codingdojo.org](https://codingdojo.org/) - kata
* [coderdojo.com](https://coderdojo.com/) - under 16


Old README.MD
=============

This will be removed in time.

Description
-----------

A dynamic website structure to showcase exiting simple programming projects
in a variety of different languages.

THIS REPO IS MESS AND NEEDS SOME SERIOUS REWORKING!
There is peril here.
It is not a finished masterpiece.

Getting Started
---------------

Linux & Windows
- make setup
- make run

(AllanC - TODO: Need instructions/script for setting up virtualenv in windows)


<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB"><img alt="Creative Commons Licence" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">TeachProgamming</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://calaldees.tnkd.net/" property="cc:attributionName" rel="cc:attributionURL">Allan Callaghan</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/calaldees/TeachProgramming" rel="dct:source">https://github.com/calaldees/TeachProgramming</a>.


Other references

https://twitter.com/ID_AA_Carmack/status/1202980347295612929
https://github.com/jackpal/Dandy-Dungeon
https://github.com/nanochess/Invaders


* [Updating “101 Basic Computer Games” for 2021](https://discourse.codinghorror.com/t/updating-101-basic-computer-games-for-2021/7927)
    * Project to implement lots of old BASIC games in multiple modern languages
    * [BASIC Computer Games](http://www.vintage-basic.net/games.html) 1978 Book
    * [basic-computer-games](https://github.com/coding-horror/basic-computer-games)