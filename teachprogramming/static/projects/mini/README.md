Mini Algorithm Projects
=======================

Code Environment
----------------

* Local
    * Local IDE
* Online
    * [jupyterhub.canterbury.ac.uk](https://jupyterhub.canterbury.ac.uk/)
    * Browser Based
        * [w3schools.com/tryit](https://www.w3schools.com/tryit/trycompiler.asp?filename=demo_python)
        * [OneCompiler](https://onecompiler.com/)
        * [mycompiler.io](https://www.mycompiler.io/)
        * [tutorialspoint.com/codingground](https://www.tutorialspoint.com/codingground.htm)
        * [glot.io](https://glot.io/)
    * Browser Based - Live Share
        * [Repl.it](https://replit.com/)
        * [codebunk](https://codebunk.com)
    * Other
        * [dotnetfiddle.net](https://dotnetfiddle.net/) csharp
        * [glitch.com](https://glitch.com/) node.js
        * [create.withcode.uk](https://create.withcode.uk/) python only - but has input box support
        * Limited
            * [ideone.com](https://ideone.com)
            * [codepad.org](http://codepad.org)
            * [tio.run](https://tio.run/)


* Once you've solved a problem in one language - build your skills by implementing it in another
    * https://computingteachers.uk/static/langauge_reference.html


Pair Programming
----------------

* Pair programming IS slower - but the quality of the result is higher
* Aim to
    * Talk 50% of the time
    * Type 50% of the time
* Methods
    1. Plug two keyboards into one machine
    2. Take turns with keyboard (driver and navigator)
    3. Live share
* Don't use the word "No" - (stretch your vocabulary) use - unlikely, probably not, unsure, possibly
    * Psychology of "Yes and" in improvisation
* You may not _like_ your partner - you have to communicate professionally
* Choice of partner
    * This week: You choose your partner
    * Next week: I will allocate you a partner
* Focus talk on "the problem"



---


Bit-manipulation
String manipulation
Recursion

String '.''-' morse code


Next year - join the dots - Egineering

https://www.educative.io/edpresso/what-is-the-rsa-algorithm
https://scanftree.com/programs/c/c-code-to-implement-rsa-algorithmencryption-and-decryption/
https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.rsacryptoserviceprovider?view=net-6.0


* [Instructional Pseudocode Guide to Teach Problem-Solving](https://dl.acm.org/doi/10.1145/3304221.3325581) 2019
    * > This paper introduces how technical writing techniques and problem-solving strategies can be combined to help students find those questions and develop programming code through writing instructions and documenting their design process. 




Fibbonach
---------
```python
def fib(v):
    """
    >>> next_fib(0):
    1
    >>> next_fib(1):
    1
    """
    return
```






is_anagram(a, b) {

}


Single digets only
123 ok
1223 not ok
321 ok
3321 not ok
67 ok
66 not ok




is_prime



```python
def fizzbuzz(i):
    """
    * [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz#Programming_interviews) [_](https://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/)
        * > Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
        * In under 5min (Pro) - in under 10min (A Grade)
        * [Tom Scott commentary and solution](https://www.youtube.com/watch?v=QPZ0pIK_wsc)

    >>> tuple(map(fizzbuzz, range(100)))
    ('fizzbuzz', 1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz', 'fizz', 22, 23, 'fizz', 'buzz', 26, 'fizz', 28, 29, 'fizzbuzz', 31, 32, 'fizz', 34, 'buzz', 'fizz', 37, 38, 'fizz', 'buzz', 41, 'fizz', 43, 44, 'fizzbuzz', 46, 47, 'fizz', 49, 'buzz', 'fizz', 52, 53, 'fizz', 'buzz', 56, 'fizz', 58, 59, 'fizzbuzz', 61, 62, 'fizz', 64, 'buzz', 'fizz', 67, 68, 'fizz', 'buzz', 71, 'fizz', 73, 74, 'fizzbuzz', 76, 77, 'fizz', 79, 'buzz', 'fizz', 82, 83, 'fizz', 'buzz', 86, 'fizz', 88, 89, 'fizzbuzz', 91, 92, 'fizz', 94, 'buzz', 'fizz', 97, 98, 'fizz')
    """
    r = ''
    if i % 3 == 0:
        r += 'fizz'
    if i % 5 == 0:
        r += 'buzz'
    if not r:
        r = i
    return r
```



