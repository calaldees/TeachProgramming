AS-Level Computing: Projects
============================

* [AQA A-Level Computing - Specification](https://filestore.aqa.org.uk/resources/computing/specifications/AQA-7516-7517-SP-2015.PDF)
    * 180 guided learning hours (school) + homework

* These are all the projects for the year 
* Tasks can be attempted in any order (self directed/ownership)
* Every task maps to theory specification
* You may use any language for each task
    * It is recommended that you use a least 2 languages (one static, one dynamic)


Training Tasks (Grade E)
-----------------------------
1. Ask the user for a username and then ask for the password. If the username and password are correct give a message `approved` and exit. After 3 incorrect attempts, print `denied` and exit.
    * Extension: delay for 2 seconds on incorrect password
2. Read a list of numbers from a file. Print the sum of all the numbers
3. Create a program that counts from 0 to 30 missing out all numbers devisable by 4
    * Program must only have one `print()` statement
4. Create a program that reads a line from the user. If the line starts with `S`. Append that line to the bottom of a text file.
5. Ask the user for 5 words. Print out a rubbish sentence putting between 10 and 20 of these words together
6. Create a program that takes user input and converts a 12h time (e.g. `4:53pm`, `6:00am`) into into a 24h time (e.g. `16:53`, `06:00`)
7. Read in a phrase from a user. If the phrase exists in a file print “Phrase exists”
    * This should ignore case
8. Read a multiline CSV file. Print the highest number
    * example file
        * ```
            5,12,983,43,2,7,11,42
            3,1,4924,23,4
            1,2,3
          ```
9. Fibonacci Sequence: Generate the following sequence under 200. `1,1,2,3,5,8,13,21,etc`
    * Add the previous 2 numbers, e.g. 2+3=5 3+5=8


Filesize Calculator (E Grade)
-----------------------------

Create a program to calculate and display the filesize in bytes of
* Bitmap Image: width, height, bit's per pixel
* Sound Sample: bits, channels, frequency, duration
* Uncompressed Video: image_size, bit-depth, frames per second, duration

### Verify
* Compare your program's output with the size of an actual uncompressed file (bmp, wav)
* Are they different? Why are they different?

### B Grade
* Combine with _Humanise task_ to report filesize in a human readable form
    * select the largest corresponding power. e.g. 1.2Gb
* Refer to humanise library via an `import`


MIDI notes (E Grade) (Optional)
-------------------------------
Play from code 'Twinkle Twinkle Little Star' by sending MIDI notes to a synthesizer
TODO: add `sleep` to cheat sheet
TODO: add example of playing 1 midi note to cheat sheet

### D Grade
* Enable the tune to be transposed up or down
* Pass a tempo in bpm


Word Reverser (D Grade)
-----------------------
Create a program that reads in a plain text file and reverses all the letters of the words but keeps the words in the correct order and writes this back to a new file. For example:

> The quick brown fox

would be converted to

> ehT kciuq nworb xof

Running the program twice should return to the original text.

### C Grade
Ensure the first letter is capitalized if the original word had a capital letter.

> Eht kciuq nworb xof

### B Grade - Command Line Options
The user should be able to use the program from the command line in the following way

```bash
    python my_reverse.py in.txt processed_words.txt
```
or
```bash
    php my_reverse.php in.txt processed_words.txt
```
etc

### Techniques
This project will assess Algorithm design, Loops, File Handling, Command line (individual research into language documentation)


Calculator (D Grade)
--------------------

* Write a calculator program that
    * Takes text input and calculates the answer
    * The input will be in the format
        * `<NUMBER><SPACE><OPERATOR><SPACE><NUMBER>`
        * Support the following mathematical operators `+-*/%`
    * The output should never be longer than 3 decimal places

```
    >>> 1 + 2
    3
    >>> 3.14 * 2
    6.28
    >>> 2 / 3
    0.667
```

### Techniques
This project is designed to get you to understand
* String splitting, Parsing strings, Float/Double/Real data-types, Rounding, Mathematical Operators

### C Grade
* If the first number is not input, use the answer from the previous step automatically
```
    >>> 1 + 2
    3
    >>> + 7
    10
```

### Extension (GUI Experience)
* In VB.NET
    * Create a GUI calculator with buttons for each digit/operation.
        * each digit will append to a `display` textbox/string

### A2 (Professional)
* Consider reverse polish and brackets (a stack?)


Validation (E to C Grade)
-------------------------

Data that is entered can be incorrect. E.g “Monkey” is not a valid postcode, “Smith53” is not a valid surname.

You must write functions that can validate the following
* Surname (E Grade)
* Parity Bit (D Grade)
* Postcode (D Grade) (Optional B Grade - full http://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom)
* ISBN 10 code (http://en.wikipedia.org/wiki/Check_digit) (C Grade)
    * The ISBN code should work with either dashes and spaces in the number or not
* Credit Card Number - with or without spaces - [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) (C Grade)

### Techniques
This project is designed to get you to
* Use "Modula Arithmetic"
* Consider careful test data


Humanise Strings (D Grade)
--------------------------
TODO
Know the names, symbols and corresponding powers of 2 for the binary prefixes:
bi=2
* kibi, Ki - 2^10
* mebi, Mi - 2^20
* gibi, Gi - 2^30
* tebi, Ti - 2^40
Know the names, symbols and corresponding powers of 10 for the decimal prefixes:
* kilo, k - 10^3
* mega, M - 10^6
* giga, G - 10^9
* tera, T - 10^12


* Byte size to human readable form (is a hard problem)
    * [The most copied StackOverflow snippet of all time is flawed!](https://programming.guide/worlds-most-copied-so-snippet.html)
        * an answer I wrote almost a decade ago was found to be the most copied snippet on Stack Overflow. Ironically it happens to be buggy.


Cypher (D to A Grade)
---------------------
Create a program to encode/decode messages.

### D Grade
```python
    >>> cypher_ceaser(1, 'abc')
    'bcd'
    >>> cypher_ceaser(1, 'hello')
    'ifmmp'
    >>> cypher_ceaser(-1, 'ifmmp')
    'hello'
    >>> cypher_ceaser(1, 'xyz')
    'yza'
```

### C Grade
```python
    >>> cypher_ceaser(-1, 'a b c')
    'z a b'
```

### B Grade - Vigenere Cipher
Takes a string 'key' to rotate each letter.
```python
    >>> cypher_vigenere('a', 'abc')
    'abc'
    >>> cypher_vigenere('b', 'abc')
    'bcd'
    >>> cypher_vigenere('abc', 'abc')
    'ace'
    >>> cypher_vigenere('b', 'bcd', sub)
    'abc'
    >>> cypher_vigenere('abc', 'z a b', sub)
    'z y a'
    >>> cypher_vigenere('pizza', 'hello i was a dog that sat on a log')
    'wmkko q vah z ddo shpb rai nm p kng'
    >>> cypher_vigenere('pizza', 'wmkko q vah z ddo shpb rai nm p kng', sub)
    'hello i was a dog that sat on a log'
```

### A Grade
Operate Vigenere on a plain bytes and encode/decode a binary file

### todo
* [Vernam cipher](https://isaaccomputerscience.org/concepts/data_encrypt_vernam) (one-time pad) is key-length==message-length is unbreakable encryption
    * xor binary


Multi Format Converter (C Grade)
--------------------------------
Write a program that converts strings from one number format to another.
* Binary to Denary (and vice versa)
* HEX to Denary (and vice versa)
* 3Bit Grey Code (and vice versa) http://en.wikipedia.org/wiki/Grey_code

### Techniques
* This project will assess Grey Codes, Suitable Test data and Algorithm design
    * To convert to and from grey codes I suggest a lookup table and the use of a Linear Search.


Networking (C Grade)
--------------------
* Create a program to
    * Parse and IPv4 address e.g. `192.168.0.12`
        * return what 'Class' of address it is (A, B, C)
        * return True or False if it is within a known subnet e.g. `255.255.127.0`

### Techniques
This project is designed to get you to
* Understand the binary structure of network address
* Understand network terminology/features
* further reading [Fun with IP address parsing](https://blog.dave.tf/post/ip-addr-parsing/)

Sorting and Searching Records (Grade D to B)
--------------------------------------------
1.	Read a set of names and address from a CSV file and output a new CSV file in surname order
2.	Search for a specific surname and output selected records to a new CSV file

### Grade D
* Read CSV into a data structure in memory
* Implement Bubble Sort
* Implement Linear Search

### Grade C
* Implement Binary Search (to return a single found surname)
* The user can select what field to sort by and what field to search with e.g. first name, town, city, DOB, etc
* Parse String Dates

### Grade B
* Return multiple surnames from binary search
* Implement one of MergeSort, Quicksort, Insertion-sort

### Techniques
* This project will assess your algorithm design, CSV handling, Records(dictionaries/associative-arrays/maps) Bubble Sort understanding and Linear/Binary Search Understanding


Generate soundwave (C grade)
------------------

* Generate a mono 44.1khz audio file containing a 440hz sin wave, square wave, triangle or saw wave with code.
* Output raw binary to a file (16bit signed) [filename.raw]
* Open in audacity? compare with wikipedia reference audio clip

Binary files, byte order (big/little endian)

### Generate all 4 wave types (B Grade)

### Create WAV file header (A grade)
* http://soundfile.sapp.org/doc/WaveFormat/
* https://stackoverflow.com/questions/28137559/can-someone-explain-wavwave-file-headers



2D Arrays & RLE Encoding (Grade C to A)
----------------------------------
Read the ConwayRLE format and display the result as ASCII
http://www.conwaylife.com/wiki/RLE
```python
    >>> load_conway((
    ...     '#C This is a glider.',
    ...     'x = 3, y = 3',
    ...     'bo$2bo$3o!',
    ... ))
    '.#.'
    '..#'
    '###'
```
### Techniques
* This project is designed to get you to use 2D Arrays and read/understand/parse an externally specified file format.

### Grade A
Implement Conways game of life in ASCII text

[comment]: # (https://www.conwaylife.com/wiki/55P9H3V0  the smallest known spaceship with an unsimplified speed of 3c/9)


2D Arrays & Algorithm Design (B to A Grade)
-------------------------------------------
* Your program should
    * Display a possible state for a game of "Connect 4" (ASCII text grid)
    * A message indicating if a player has won.
* The game does not have to playable. It just needs to report if a player has won given a known board state.

```
    ........
    ........
    ..R.....
    ..R...Y.
    RRY.RYYR
```

### Grade A
* Make the game playable for 2 players

### Techniques
* This project is designed to get you to use 2D Arrays and Pseudo Code design


Vector Graphics Format (B Grade)
--------------------------------
Create a vector graphics render that uses the following CSV file

```csv
    circle,0.0,0.0,1.0,1.0,YELLOW
    rectangle,0.2,0.7,0.6,0.1,RED
    circle,0.3,0.4,0.1,0.1,BLACK
    circle,0.6,0.4,0.1,0.1,BLACK
    line,0.2,0.3,0.4,0.2,BLACK
    line,0.8,0.3,0.6,0.2,BLACK
    image,0.45,0.45,0.1,0.2,nose.png
```

### Hints
* The file should draw a smiley face with a red mouth and a bitmap nose
* Read in the file line at a time, split it and draw it
* Try implementing a function at a time e.g. get it just drawing the circles first then move on to the others.
* The values relate to the size of the screen.
    * E.g. if the screen was width 1000 and the value was given 0.2 the co-ordinate would be 200
* Remember values with decimal points are Real numbers (doubles or floats and not integers)
* This allows the vector graphic to be rendered at ANY resolution
* Each line is in the format TYPE,X,Y,WIDTH,HEIGHT,DETAIL


British Informatics Olympiad: [Optional Projects]
-------------------------------------------------
* [British Informatics Olympiad 2009: Round One Exam](https://www.olympiad.org.uk/papers/2009/bio/bio09-exam.pdf)
    * Q1 Digit Word (A Grade)
    * Q2 Puzzle Game (Degree/Professional)
* [British Informatics Olympiad 2010: Round One Exam](https://www.olympiad.org.uk/papers/2010/bio/bio-10-exam.pdf)
    * Q1 Anagram Numbers (A Grade)
    * Q2 Die Tipping (Degree/Professional)

If you can complete _Die Tipping_ or _Puzzle Game_ you can work as a professional developer.
You are better than some university graduates.


Project Documenting
===================

* Each project should take on average 2 weeks
* For 4 projects the following documentation needs to be submitted
    * (The process will help you for all projects, but is not formally required)
* Use these headings. Every word below is from the spec and needs to be used by you in the exa
* 2 project submissions must be in a static language
* 2 projects submissions be in a dynamic language

* Analysis
    * Understand the problem
        * An English description of what, why and who
    * Define the problem
        * Bullet Points of what it must do
    * Define the boundaries
        * Any limits or restrictions (hardware, software, size of data input, time constraints)
* Test Planning
    * List test data (describe expected inputs and expected outputs)
        * Normal (typical)
        * Boundary/limit
        * Erroneous
    * Consider an average of 10 items of test data
    * Write an automated test with `assert` or `doctests`
    * DO NOT PROCEED TO DESIGN WITHOUT DOING THIS! SERIOUSLY! KNOW THE SPEC OF WHAT YOU ARE WRITING!
* Design
    * Plan Code Solution - Algorithm design
        * Structured English -> Pseudo Code -> High level code
            * Showing - Sequence, Assignment, Selection, Repetition
* Implementation (creating it)
    * Printout of code listing labelling the following
        * Data types
            Integer, Real/Float/Double, Boolean, Character, String, Date/Time, Records (Dicts, Maps, Associative-Arrays), Arrays (or equivalent)
        * Variable declaration
        * Constant declaration
        * Procedure/Function/Subroutine
        * Assignment (=)
        * Iteration (For, Do, While)
            * Sequence
        * Selection (IF)
        * Procedure and Function calling
            * Return
        * Arithmetic operators (+-*/%), integer-division
        * Relational Operators (<,>,>=,<=,==)
        * Boolean/Logical Operators (AND,OR,NOT,XOR)
        * Use of any built in functions
            * split, join, substring, val, string formatting, round
        * String conversions (Integer, Float, Date)
        * Exceptions
* Testing
    * Check Solution


Suggestions
-----------

* Have a development flow where; view code and output on a single screen at the same time
* Touch the mouse as little as possible
    * Use hotkeys to switch between code and output
* Learn to use your IDE's advanced hotkeys
* Setup your IDE to use a linter
* Use a debugger (not just `print`) (breakpoint, step into, step over, watch variable values)
* Use version control
* Write automated tests before you implement your feature/function
    * Write your tests as functions before you start
    * use `assert` or [doctests](https://docs.python.org/3/library/doctest.html)
    * [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development)
* Know how to access your language standard library documentation

