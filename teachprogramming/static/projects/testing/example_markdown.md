Example
=======

Example of tests in a separate Markdown document.

* Write your implementation in `example_markdown.py` 
<!--

    This is actual python that is run by the doctest - we need to import the code to be tested
    >>> from example_markdown import *

    >>> from pathlib import Path
    >>> code = Path('example_markdown.py').open().read()

-->

Everything in the code below that is indented with `>>>` is executed as part of the doctest


Addition
--------

Implement a function called `add`

    >>> add(1, 2)
    3
    >>> add(-1, 2)
    1
    >>> add(add(1,2), 3)
    6


Subtraction
-----------

Implement a function called `sub`

    >>> sub (2, 1)
    1
    >>> sub(-1, 2)
    -3
    >>> sub(add(1,2), 3)
    4


Other
-----

* Make sure your code has
  * A `sub` function
  * A relational operator

```

    Here you could use any for of regex on `code`

    >>> assert "def sub(" in code, "Your code does not have a `sub` function yet"

    >>> assert ">=" in code, "(example) Your code should have a relationl operator in it"

```