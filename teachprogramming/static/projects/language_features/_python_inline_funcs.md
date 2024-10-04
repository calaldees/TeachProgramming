
```python
import timeit

def outer_func(a):
   return a['foo'] == 'bar'


def outer_parent():
    a = {'foo': 'bar'}
    outer_func(a)

def inner_parent():
    def inner_function(a):
        return a['foo'] == 'bar'

    a = {'foo': 'bar'}
    inner_function(a)

print(f"Outer function time: {timeit.timeit(outer_parent, number=10000000)}")
# Prints Outer function time: 0.7449549169996317
print(f"Inner function time: {timeit.timeit(inner_parent, number=10000000)}")
# Prints Inner function time: 1.1750925420001295
```
