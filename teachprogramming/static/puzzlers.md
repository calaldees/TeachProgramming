Puzzlers
========

Guess the output
* [Java Puzzlers](http://www.javapuzzlers.com/) - traps, pitfalls and corner cases (book)
    * Expert
* Other language books?

TODO - more

```python
s = "hello"
d = {}
for i, d[i] in enumerate(s):
    i = 1
    # print(d)
print(d)
```
`{0: 'h', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}`


Mid tier python problems
------------------------

https://blog.finxter.com/10-best-python-puzzles-to-discover-your-true-skill-level/
10 * interactive mini python programs where you predict the output


Expert level python problems
----------------------------
https://speakerdeck.com/alangpierce/python-puzzlers

```python
nope = False 
zilch = 0 
nada = [] 
if (nope, 
 zilch and 
 nada): 
 print 'How positive!' 
else: 
 print 'Don't be so negative!'
```
(the original slides had incorrect syntax highlighting)

(a)How positive!
(b)SyntaxError
(c)Don't be so negative!
(d)TypeError


Moral
● I am trying to trick you; don't trust the syntax 
highlighting. 
● Watch out for accidental tuples. 
o Parentheses not required! 
● Learn the semantics for truthy/falsy values.


```python
class SmartList(object): 
 """List that maintains its sum.""" 
 def __init__(self, arr=[], z=0): 
 self.arr = arr 
 self.sum = sum(arr, z) 
 def append(self, elem): 
 self.sum += elem 
 self.arr.append(elem) 
 def __getitem__(self, item): 
 return self.arr[item]

 list1 = SmartList() 
list1.append(3) 
list1.append(5) 
list2 = SmartList( 
 arr=[['Hello'], ['World']], z=[]) 
list3 = SmartList(z=False) 
list3.append(False) 
list3.append(True) 
list3.append(True) 
print "List3's sum: %s" % list3.sum
```

(a)TypeError
(b)List3's sum: 10
(c)List3's sum: 2
(d)List3's sum: True

Moral
● Never use a mutable value for a default 
argument. 
● bool is a subclass of int, and True and False 
behave similar to 1 and 0 in many ways.


Try to make the program crash!
```python
# quit_util.py 
 import quitter 
except: 
 exit(0) 
quitter.do_not_crash()

# quitter.py
def do_not_crash(): 
 exit(0) 
 # Add one line here (indented to be within do_not_crash
 # exit = None (ANSWER)
```

Command being run: python quit_util.py

Moral
● Not much of one. 
● Python looks ahead to determine the set of 
locals in each function, so it may not be as 
line-by-line as you think.


```python
import math 
class PolarPoint(object): 
 x, y = 0, 0 
 def __init__(self, base_point): 
 if base_point: 
 x, y = base_point 
 def radius(self): 
 return math.sqrt(x**2 + y**2) 
 def angle(self): 
 return math.atan2(y, x)

points = [(3, 4), (5, 12)] 
rev_points = [ 
 (y, x) for x, y in points] 
all_points = map( 
 PolarPoint, 
 points + rev_points + [None]) 
print [int(p.radius()) 
 for p in all_points]
```
 (a)[0, 0, 0, 0, 0]
(b)[5, 12, 5, 12, 0]
(c)[5, 13, 5, 13, 0]
(d)[13, 13, 13, 13, 13] ANSWER

`x, y` require `self.`. It compiles because x,y are leaked global variables!!!

Moral
● List comprehensions leak their variables. 
o Dictionary, set, and generator 
comprehensions don't. 
● Limit usage of global variables (including list 
comprehensions in global scope). 
● Methods don't have implicit access to values 
declared in the class directly