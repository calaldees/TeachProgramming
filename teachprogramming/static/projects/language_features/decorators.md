Decorators
----------


python
```python
# TASK:
# Attempt to modify this decorator to:
#   1. print to the screen the arguments that the decorated function was called with
#   2. modify the returned result by adding 10
# e.g. When run the output should be
#   called with (1, 2) {}
#   13

from functools import wraps

def example_decorator(original_function=None, add_your_args=None):
    """
    This pattern works for defining decorators with and without params.
        (Positional arguments to the decorator are not supported by this pattern)
    Use with 
        @example_decorator
        def my_func(a, b):
            return a + b
    or
        def my_func(a, b):
            return a + b
        my_func = example_decorator(my_func)
    """
    def _decorate(function):
        @wraps(function)
        def wrapped_function(*args, **kwargs):
            pass  # replace this line with - pre function code
            _return = function(*args, **kwargs)
            pass  # replace this line with - post function code
            return _return
        return wrapped_function
    return _decorate(original_function) if callable(original_function) else _decorate


@example_decorator
def my_func(a, b):
    return a + b


if __name__ == "__main__":
    print(my_func(1,2))
```

* What is the point of this technique?
* When/Why would you ever use it?
* Is this good? or bad?


TODO
====

## Decorators in javascript

https://www.sitepoint.com/javascript-decorators-what-they-are/

```javascript
function doSomething(name) {
  console.log('Hello, ' + name);
}

function loggingDecorator(wrapped) {
  return function() {
    console.log('Starting');
    const result = wrapped.apply(this, arguments);
    console.log('Finished');
    return result;
  }
}

const wrapped = loggingDecorator(doSomething);
```


## Typing Decorators (Python)

https://docs.python.org/3/library/typing.html#typing.ParamSpec

```python
from collections.abc import Callable
import logging

def add_logging[T, **P](f: Callable[P, T]) -> Callable[P, T]:
    '''A type-safe decorator to add logging to a function.'''
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f'{f.__name__} was called')
        return f(*args, **kwargs)
    return inner

@add_logging
def add_two(x: float, y: float) -> float:
    '''Add two numbers together.'''
    return x + y
```

```python
from typing import Awaitable, Callable, ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")


def decorator(fn: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]:
    async def decorated(*args: P.args, **kwargs: P.kwargs) -> T:
        return await fn(*args, **kwargs)

    return decorated
```
https://stackoverflow.com/a/71132186/3356840