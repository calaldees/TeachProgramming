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
    >>> maths_error_with_doctest(3, "bob")
    Traceback (most recent call last):
    T...


    "..." is a wildcard catchall in dcotest

    """
    return a / b

'''
Doctests
--------

run doctests
  python3 -m doctest -v *.py
  pytest --doctest-modules

pytest (to ignore setup.cfg)
  pytest -c /dev/null

```python
def dotest_with_error():
    """
    >>> x
    Traceback (most recent call last):
    NameError: name 'x' is not defined
    """
    pass
```
https://stackoverflow.com/a/63539385/3356840 - `...` is not needed for exception detail
`...` is a wildcard
https://www.py4u.net/discuss/154095
but cant be used as the start of a string (as this conflicts with the line continuation) 
and can be infix eg `(...)` - this does not work when using `-m doctest` but does when pytest is used?
Answer here
https://pymotw.com/3/doctest/
`-m doctest` does not allow ELIPSIS by default, we need to use `>>> line_to_test()  #doctest: +ELLIPSIS` on the test line or `-o ELLIPSIS` on the commandline

'''