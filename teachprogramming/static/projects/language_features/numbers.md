Number Handling
---------------

Static/Compiled seem to be different to Dynamic/Interpreted. Let's look.

Run all of these

java
```java
int a = Integer.MAX_VALUE;
System.out.println(a);
System.out.println(a+1);
```

csharp
```csharp
int a = Int32.MaxValue;
Console.WriteLine(a);
Console.WriteLine(a+1);
```
https://en.wikipedia.org/wiki/Nuclear_Gandhi

python
```python
import sys
a = sys.maxsize
print(a)
print(a+1)
```

javascript
```javascript
let a = Number.MAX_SAFE_INTEGER;
console.log(a);
console.log(a+1);
Number.MAX_SAFE_INTEGER+1 === Number.MAX_SAFE_INTEGER+2
```


Dynamic Vs Static Langauges
===========================

* [How Many Lines of C it Takes to Execute a + b in Python?](https://codeconfessions.substack.com/p/cpython-dynamic-dispatch-internals) - Understand the mechanics of dynamic dispatch implementation in CPython
    * Amazing breakdown of the `c` files responsible for numeric operations
* [](https://www.trickster.dev/post/lesser-known-parts-of-python-standard-library/)
  * 'did you know' article about python that has an interesting example
  * ```
    >>> 1.2 + 2.2
    3.4000000000000004
    
    >>> from decimal import *
    >>> one_point_two = Decimal('1.2')
    ```