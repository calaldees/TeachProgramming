import re
from itertools import chain

problem = """
var puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]];
"""
solution = """
    sudoku(puzzle);
    /*Should return
    [[5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]] 
"""

class Sudoku():
    COMPLETE_NUMBER_SET = frozenset(i+1 for i in range(9))

    @staticmethod
    def parse(data):
        """
        >>> problem = '''
        ...     var puzzle = [
        ...         [5,3,0,0,7,0,0,0,0],
        ...         [6,0,0,1,9,5,0,0,0],
        ...         [0,9,8,0,0,0,0,6,0],
        ...         [8,0,0,0,6,0,0,0,3],
        ...         [4,0,0,8,0,3,0,0,1],
        ...         [7,0,0,0,2,0,0,0,6],
        ...         [0,6,0,0,0,0,2,8,0],
        ...         [0,0,0,4,1,9,0,0,5],
        ...         [0,0,0,0,8,0,0,7,9]];
        ... '''
        >>> Sudoku.parse(problem)
        (5, 3, 0, 0, 7, 0, 0, 0, 0, 6, 0, 0, 1, 9, 5, 0, 0, 0, 0, 9, 8, 0, 0, 0, 0, 6, 0, 8, 0, 0, 0, 6, 0, 0, 0, 3, 4, 0, 0, 8, 0, 3, 0, 0, 1, 7, 0, 0, 0, 2, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0, 2, 8, 0, 0, 0, 0, 4, 1, 9, 0, 0, 5, 0, 0, 0, 0, 8, 0, 0, 7, 9)
        """
        if isinstance(data, str):
            data = (int(i) for i in re.sub(r'\D', '', data))
        data = tuple(data)
        len(data) == 9*9
        return data

    @classmethod
    def _valid(Class, data):
        """
        >>> Sudoku._valid((1,2,3,4,5,6,7,8,9))
        True
        >>> Sudoku._valid((0,2,3,4,5,6,7,8,9))
        False
        >>> Sudoku._valid((9,8,7,6,5,4,3,2,1))
        True
        >>> Sudoku._valid((5,5,5,5,5,5,5,5,5))
        False
        """
        return frozenset(data) == Class.COMPLETE_NUMBER_SET

    @classmethod
    def _missing(Class, data):
        """
        >>> Sudoku._missing((1,2,3))
        frozenset({4, 5, 6, 7, 8, 9})
        """
        return Class.COMPLETE_NUMBER_SET - frozenset(data)

    @staticmethod
    def overlay(d1, d2):
        """
        >>> Sudoku.overlay((1,2,0,4,0,6,0,8,9), (3,5,7))
        (1, 2, 3, 4, 5, 6, 7, 8, 9)
        """
        c = -1
        def inc():
            nonlocal c 
            c += 1
            return c
        return tuple(v if v else d2[inc()] for v in d1)

    @staticmethod
    def row(data, n):
        """
        >>> data = Sudoku.parse(problem)
        >>> Sudoku.row(data, 0)
        (5, 3, 0, 0, 7, 0, 0, 0, 0)
        >>> Sudoku.row(data, 1)
        (6, 0, 0, 1, 9, 5, 0, 0, 0)
        """
        return data[(n*9):(n+1)*9]

    @staticmethod
    def col(data, n):
        """
        >>> data = Sudoku.parse(problem)
        >>> Sudoku.col(data, 0)
        (5, 6, 0, 8, 4, 7, 0, 0, 0)
        >>> Sudoku.col(data, 1)
        (3, 0, 9, 0, 0, 0, 6, 0, 0)
        """
        return tuple(data[(i*9)+n] for i in range(9))

    @classmethod
    def block(Class, data, row, col):
        """
        >>> data = Sudoku.parse(problem)
        >>> Sudoku.block(data, 0,0)
        (5, 3, 0, 6, 0, 0, 0, 9, 8)
        >>> Sudoku.block(data, 1,1)
        (0, 6, 0, 8, 0, 3, 0, 2, 0)
        """
        return tuple(chain.from_iterable(
            r[(col*3):(col+1)*3]
            for r in (Class.row(data, (row*3)+i) for i in range(3))
        ))

    def __init__(self, data):
        self._base = self.parse(data)
        self.data = list(self._base)

    @property
    def valid(self):
        """
        >>> Sudoku(problem).valid
        False
        >>> Sudoku(solution).valid
        True
        """
        return (
            len(tuple(filter(None, self.data))) == 9*9 # data is correct size
            and
            all(self._valid(self.row(self.data, r)) for r in range(9))
            and
            all(self._valid(self.col(self.data, c)) for c in range(9))
            and
            all(
                self._valid(self.block(self.data, x,y))
                for y in range(3)
                for x in range(3)
            )
        )


