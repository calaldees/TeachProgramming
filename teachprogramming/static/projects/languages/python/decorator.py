from functools import wraps


def example_decorator(original_function=None, add_your_args=None):
    """
    Write a doc-comment with examples
    This pattern works for decorators with and without params
    Positional arguments to the decorator are not supported by this pattern
    Use with 
        @example_decorator
        def my_func(a,b):
            return a + b
    or
        def my_func(a,b):
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
def test_1(a, b):
    return a + b

import json
json.loads = example_decorator(json.loads)



if __name__ == "__main__":
    print(test_1(1,2))
    print(json.loads("[1,2,          3]"))
