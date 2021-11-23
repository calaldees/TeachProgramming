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


# Bonus
# Example of augmenting an existing library function
#import json
#json.loads = example_decorator(json.loads)
#print(json.loads("[1,2,          3]"))
