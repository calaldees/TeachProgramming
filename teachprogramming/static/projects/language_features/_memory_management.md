### Memory Management - Garbage Collection

Manual memory management or Automatic memory management

```python
aa = {'a':[1,2,3], 'b':[4,5,6]}
bb = {'c':[7,8,9], 'd':[10,11,12]}
aa = {'e':[13,14,15], 'f':[16,17,18]}
# Question: Where is the data from the first `aa`? Where did it go?
```

```python
import sys
a = []
b = a
sys.getrefcount(a)
# The reference count for the empty list object [] was 3. 
# The list object was referenced by a, b and the argument passed to sys.getrefcount().
```

Whiteboard/Visualiser: Demo?

Memory management is dangerous to get wrong. 
Most programmers mess this up because we are only human. 
So most languages prefer automattic memory management.

* Reference counting
* You don't have control over the garbage collection thread
    * This is an issue for hard realtime systems (one of the biggest complaints of java)
    * (I think) Java has 30 different garbage collection methods/strategies
* C, C++, Rust have manual memory management model
    * Memory leaks
    * Rust has excellent primitives for this
