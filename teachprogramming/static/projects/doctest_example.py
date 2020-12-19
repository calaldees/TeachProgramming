# https://stackoverflow.com/questions/1024411/can-python-doctest-ignore-some-output-lines
# https://hub.packtpub.com/basic-doctest-python/


def dotest_with_error():
    """
    >>> x
    Traceback (most recent call last):
        ...
    NameError: name 'x' is not defined
    """
    pass


def maths_error_with_doctest(a, b):
    """
    >>> maths_error_with_doctest(3, "bob")
    Traceback (most recent call last):
    TypeError: ...

    "..." is a wildcard catchall in dcotest

    """
    return a / b

