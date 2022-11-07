Reflection
==========

Problem: You may not know what objects/functions you are working with at compile time.
Possible Use: Plugin system?


The entire language of python is built on reflection.
Live inspection of state/objects



```python
# Load an interactive python repl
# Example of reflecting on splitting a string

tt = "aa,bb,cc"
locals()
dir(tt)
type(tt)
type(tt.split)
tt.split.__doc__
tt.split(',')

nn = tt.split(',')
nn[1]

ff = getattr(tt, "split")
ff(',')
```


```python
class Test():
    def __init__(self, value):
        self.value = value
    def increment(self, increment=2):
        """
        Increment the value

        >>> tt = Test(10)
        >>> tt.value
        10
        >>> tt.increment()
        >>> tt.value
        12
        >>> tt.increment(10)
        >>> tt.value
        22
        """
        self.value += increment

tt = Test(10)

# 1. Copy and paste the code above into a python repl
# 2. Use `dir` to list the attributes of tt
# 2. Use reflection to get `value` with `getattr` of tt and display it
# 3. Use reflection to get the function `increment` and store it in a variable
# 4. Activate the stored function from 3.

```


JavaScript
----------

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys

```javascript
// language wise - no - https://stackoverflow.com/questions/2051678/getting-all-variables-in-scope

// browser only
var a = 1, b = 2, c = 3;
for ( var i in window ) {
    if (window.hasOwnProperty(i)) {
        console.log(i, typeof(window[i]), window[i]);
    }
}
```


Java
----

https://www.oracle.com/technical-resources/articles/java/javareflection.html

C#
---

* [reflection.ipynb](reflection.ipynb)

