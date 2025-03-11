Doctests
========

Use
---

Some notes from [teacherEducation automated_tests.md](https://github.com/calaldees/teacherEducation/blob/main/teacherEducation/automated_tests.md)

* `assert` statement
    * A shortcut to say "I expect this to be true - or break/error/stop now with a text description"
    * python `assert my_value == 3, f"I wanted my_value to be 3 but I got {my_value}"`
    * csharp `Debug.Assert(val != 2, " Value should not be 2.");` [example assert-in-csharp](https://www.educba.com/assert-in-c-sharp/)


* An example of using different types of automated test in python.
    * Tests via Main method and assertions
        * (no real test framework)
    * Doctests
        * `python example_assertions.py`
    * Doctests inline with code
        * `python -m doctest --fail-fast example_doctest_inline.py`
    * Doctest in separate MarkDown file
        * `python -m doctest --fail-fast example_markdown.md`
    * Other options `-v` `--fail-fast`
* TASKS
    1. Complete the tests that fail when you hit the run button
    2. Using the shell command-line run the (total of) 3 other methods for writing/running tests in python
        * see `.replit` for the commands for each type of test
    3. Attempt to use replit's built in unit-tests
        * I don't like the idea of vendor lock-in. We can't move between providers. Let's investigate what these tools do
        * (Since writing, replit tests are now behind paywall from August 2023) 
        * (original task) Add a repl.it unit test for subtract (the _tick_ icon on the left)
        * https://docs.replit.com/teams-edu/unit-testing
        * https://docs.replit.com/teams-edu/input-output-testing video/demo on this page

* https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/projects/data/crypto.md
* An example of use inline doctest
    * https://github.com/calaldees/libs/blob/71a86ada8d641b49215893c53b92c31190254e13/python3/calaldees/music.py#L27



Stuff
-----

run doctests
```bash
  python3 -m doctest -v *.py
  pytest --doctest-modules
```

pytest (to ignore setup.cfg)
  pytest -c /dev/null

```python
def doctest_with_error():
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
and can be infix eg `(...)` -

`...` does not work by default when using `-m doctest`
https://pymotw.com/3/doctest/
`-m doctest` does not allow ELIPSIS by default, we need to use `>>> line_to_test()  #doctest: +ELLIPSIS` on the test line or `-o ELLIPSIS` on the commandline
pytest enables `...` by default



* https://stackoverflow.com/questions/1024411/can-python-doctest-ignore-some-output-lines
* https://hub.packtpub.com/basic-doctest-python/

* For multiline strings consider
    * https://docs.python.org/3/library/textwrap.html#textwrap.dedent