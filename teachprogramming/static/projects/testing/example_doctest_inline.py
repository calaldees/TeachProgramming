# python -m doctest --fail-fast example_doctest_inline.py

def add(a, b):
    r"""
    This text should describe the exercise to the student.

    This function should do things.

    >>> add(add(1,2), 3)
    6

    try to make sure the thing

    >>> add(-1, 2)
    1
    """
    return 0
