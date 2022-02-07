Tower - Answers
---------------

Understand the problem

|n|`_`|`#`|i|
|-|---|---|-|
|1|0|1|0|
|2|1|1|0|
| |0|3|1|
|3|2|1|0|
| |1|3|1|
| |0|5|2|
|4|3|1|0|
| |2|3|1|
| |1|5|2|
| |0|7|3|


### Answers

#### Python
```python
def tower(n):
    r"""
    >>> tower(1)
    '#'
    >>> tower(2)
    ' #\n###'
    >>> tower(3)
    '  #\n ###\n#####'
    >>> tower(4)
    '   #\n  ###\n #####\n#######'
    """
    return '\n'.join(
        ' '*(n-1-i) + '#'*(i*2+1)
        for i in range(n)
    )
```

#### C#
More in notebook
```csharp
String repeat(String s, int n){
    return string.Concat(Enumerable.Repeat(s, n));
}
String tower(int n) {
    return String.Join("\n", Enumerable.Range(0, n).Select(
        (i) => repeat(" ", n-1-i) + repeat("#", i*2+1)
    ));
}

if (tower(4) != "   #\n  ###\n #####\n#######") {Console.WriteLine($"It's broken - I got:\n{tower(4)}");}

```
