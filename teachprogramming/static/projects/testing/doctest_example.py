# https://docs.python.org/3/library/doctest.html

def doctest_with_error():
    """
    >>> x
    Traceback (most recent call last):
        ...
    NameError: name 'x' is not defined
    """
    pass


def maths_error_with_doctest(a, b):
    """
    >>> maths_error_with_doctest(3, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero

    >>> maths_error_with_doctest(3, "bob")
    Traceback (most recent call last):
    TypeError: ...

    >>> maths_error_with_doctest(3, "bob")
    Traceback (most recent call last):
    T...

    "..." is a wildcard catchall in doctest

    """
    return a / b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
