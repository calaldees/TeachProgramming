
```python
def is_odd(i):
    if i%2:
        return i
[n for i in range(0, 10) if (n := is_odd(i))]
```

```python
def a(max):
    for i in range(0, max):
        try:
            yield i + 1
        except:
            pass
tuple(a(12))
```
