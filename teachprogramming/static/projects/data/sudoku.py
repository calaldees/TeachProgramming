import re
from itertools import chain, permutations

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

problem2 = """
var puzzle = [
   [[5,0,0,6,7,8,0,1,2],
    [0,7,0,1,0,5,0,0,8],
    [1,0,8,0,4,2,0,6,7],
    [8,5,0,7,0,1,0,2,3],
    [0,0,0,8,0,3,7,9,0],
    [0,1,0,0,2,0,8,5,6],
    [9,6,0,5,3,0,2,8,4],
    [0,8,7,0,1,9,6,0,5],
    [0,4,0,0,8,6,0,0,9]] 

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

    @staticmethod
    def _percent_data_missing(data):
        return data.count(0) / (9*9)

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
        assert d1.count(0) == len(d2)
        c = -1
        def inc():
            nonlocal c 
            c += 1
            return c
        return tuple(v if v else d2[inc()] for v in d1)

    # just used for assertions
    # @staticmethod
    # def match(d1, d2):
    #     """
    #     Match ignoring 0's
    #     >>> Sudoku.match((1,2,0,4,0,6,0,8,9), (1,2,3,4,5,6,7,8,9))
    #     True
    #     >>> Sudoku.match((1,2,5,4,3,6,7,8,9), (1,2,3,4,5,6,7,8,9))
    #     False
    #     >>> Sudoku.match((1,2,5,4,3,6,7,8,9), (1,2,0,4,0,6,0,8,9))
    #     True
    #     """
    #     return all(
    #         a==b if a!=0 and b!=0 else True
    #         for a, b in zip(d1,d2)
    #     )

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
        >>> Sudoku.block(data, 0, 0)
        (5, 3, 0, 6, 0, 0, 0, 9, 8)
        >>> Sudoku.block(data, 1, 1)
        (0, 6, 0, 8, 0, 3, 0, 2, 0)
        """
        return tuple(chain.from_iterable(
            r[(col*3):(col+1)*3]
            for r in (Class.row(data, (row*3)+i) for i in range(3))
        ))

    def __init__(self, data):
        self._base = self.parse(data)
        self.data = list(self._base)
        self._debug_counter = 0

    def __repr__(self):
        r"""
        >>> repr(Sudoku(problem))
        '530070000\n600195000\n098000060\n800060003\n400803001\n700020006\n060000280\n000419005\n000080079'
        """
        return "\n".join(
            ''.join(map(str, self.data[9*(i+0):9*(i+1)]))
            for i in range(9)
        )

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

    def set_row(self, n, row_data):
        #assert len(row_data) == 9
        i, j = (9*(n+0), 9*(n+1))
        self.data[i:j] = row_data
        #assert self.match(self._base[i:j], self.data[i:j])

    def solve(self, r=0):
        if r>=9:
            assert False, "How? What? No?"
        missing = self._missing(self.row(self._base, r))
        for proposed_row in (
            self.overlay(self.row(self._base, r), p)
            for p in permutations(missing, len(missing))
        ):
            #print(f'{r=} {proposed_row=}')
            self.set_row(r, proposed_row)
            self._debug()

            if r==2 or r==5 or r==8:
                if not all(
                    self._valid(self.block(self.data, r//3, col))
                    for col in range(3)
                ):
                    continue
            if r==8:
                if not all(self._valid(self.col(self.data, c)) for c in range(9)):
                    continue
                else:
                    return True
                    #raise Exception("DID IT!")
            _return = self.solve(r+1)
            if _return:
                return True

    def _debug(self):
        self._debug_counter += 1
        if self._debug_counter % 100000 == 0:
            print("\033c", end='')
            print(f"{self._debug_counter=}")
            print(self)


if __name__ == "__main__":
    ss = Sudoku(problem)
    print(ss)
    print(f'Missing {Sudoku._percent_data_missing(ss._base)*100:.2f}%')
    input()
    ss.solve()

    print("\033c", end='')
    print(f"solved it in {ss._debug_counter} comparisons")
    print(ss)
    print(ss.valid)
