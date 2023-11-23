"""
`python example_assertions.py`

Simple approach
Just run the file `python example_assertions.py`

Just use assertions triggered by the main method.
This technique can be used in any language
"""


def add(a, b):
  return 0


# ------------------------------------


def test():
  assert add(add(1, 2), 3) == 6
  assert add(-1, 2) == 1
  assert sub(add(1, 2), 3) == 4
  assert sub(-1, 2) == -3


if __name__ == "__main__":
  test()
