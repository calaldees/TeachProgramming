Digit Word
----------

From: [2009 British Informatics Olympiad Round One exam](https://www.olympiad.org.uk/papers/2009/bio/round_one.html) (an under 18's coding competition)

A digit word is a word where, after possibly removing some letters, you are left with one of the single digits: 
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT or NINE.
For example:
• BOUNCE and ANNOUNCE are digit words, since they contain the digit ONE.
• ENCODE is not a digit word, even though it contains an O, N and E, since they are not in order

Write a program which reads in a single upper-case word (with at most fifteen letters) 
and determines if it is a digit word. 
If the word is not a digit word you should output the word NO. If the word is a digit 

word you should output the digit it contains, as a number.
You will not be given any words which contain more than one digit

```
Sample run 1
BOUNCE
1
```
```
Sample run 2
ENCODE
NO
```
