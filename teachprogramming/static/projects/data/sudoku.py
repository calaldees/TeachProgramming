"""
Sudoku Solver attempt

References
* https://dev.to/aspittel/how-i-finally-wrote-a-sudoku-solver-177g
* https://stackoverflow.com/a/57876668/3356840
* [stackoverflow.com how-to-generate-sudoku-boards-with-unique-solutions](https://stackoverflow.com/questions/6924216/how-to-generate-sudoku-boards-with-unique-solutions)
"""

import re
from itertools import chain, permutations
import random


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

# https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
# Designed to beat the brute force method. The first row is freeform
problem3 = """
000 000 000
000 003 085
001 020 000

000 507 000
004 000 100
090 000 000

500 000 073
002 010 000
000 040 009
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

# First attempt
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
        assert len(data) == 9*9
        return data

    @staticmethod
    def _percent_data_missing(data):
        return data.count(0) / (9*9)

    @classmethod
    def _valid_data(Class, data):
        """
        >>> Sudoku._valid_data((1,2,3,4,5,6,7,8,9))
        True
        >>> Sudoku._valid_data((0,0,0,0,5,6,7,8,9))
        True
        >>> Sudoku._valid_data((0,0,0,5,5,6,7,8,9))
        False
        """
        data = tuple(filter(None, data))
        return len(frozenset(data)) == len(data)

    @classmethod
    def _complete_data(Class, data):
        """
        >>> Sudoku._complete_data((1,2,3,4,5,6,7,8,9))
        True
        >>> Sudoku._complete_data((0,2,3,4,5,6,7,8,9))
        False
        >>> Sudoku._complete_data((9,8,7,6,5,4,3,2,1))
        True
        >>> Sudoku._complete_data((5,5,5,5,5,5,5,5,5))
        False
        """
        return frozenset(data) == Class.COMPLETE_NUMBER_SET


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
    def complete(self):
        """
        >>> Sudoku(problem).complete
        False
        >>> Sudoku(solution).complete
        True
        """
        return (
            len(tuple(filter(None, self.data))) == 9*9 # data is correct size
            and
            all(self._complete_data(self.row(self.data, r)) for r in range(9))
            and
            all(self._complete_data(self.col(self.data, c)) for c in range(9))
            and
            all(
                self._complete_data(self.block(self.data, x,y))
                for y in range(3)
                for x in range(3)
            )
        )
    
    def valid_cell_values(self, index):
        """
        >>> ss = Sudoku(problem)
        >>> ss.valid_cell_values(0)
        frozenset()
        >>> ss.valid_cell_values(2)
        frozenset({1, 2, 4})
        >>> ss.valid_cell_values(78)
        frozenset({1, 3, 4, 6})
        """
        if self.data[index]:
            return frozenset()
        def _valid(value):
            return all((
                self._valid_data(self.row(self.data, index//9) + [value,]),
                self._valid_data(self.col(self.data, index%9) + (value,)),
                self._valid_data(self.block(self.data, index//9//3, index%9//3) + (value,)),
            ))
        return frozenset(filter(_valid, self.COMPLETE_NUMBER_SET))


    def solve(self, index=0):
        self._debug()
        if index >= 80:
            return True
        while self._base[index]:
            index += 1
            if index >= 80:
                return True
        possible_values = self.valid_cell_values(index)
        if not possible_values:
            return  # if there are no possible values then this is not the solution
        for possible_value in possible_values:
            self.data[index] = possible_value
            solved = self.solve(index+1)
            if solved:
                return solved
        self.data[index] = 0  # backtrack - clean-up our attempt

    # Rubbish solving --------------------------------------


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



    def set_row(self, n, row_data):
        #assert len(row_data) == 9
        i, j = (9*(n+0), 9*(n+1))
        self.data[i:j] = row_data
        #assert self.match(self._base[i:j], self.data[i:j])

    def solve_rubbish(self, r=0):
        """
        This was my first attempt. It was shockingly bad. Never ever do this.
        """
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
                    self._complete_data(self.block(self.data, r//3, col))
                    for col in range(3)
                ):
                    continue
            if r==8:
                if not all(self._complete_data(self.col(self.data, c)) for c in range(9)):
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
            print(self, flush=True)
            #breakpoint()
            #time.sleep(0.5)



class Sudoku2():
    COMPLETE_NUMBER_SET = frozenset(i+1 for i in range(9))

    def __init__(self, data):
        self.data = list(int(i) for i in re.sub(r'\D', '', data))
        assert len(self.data) == 9*9
        self.empty_indexes = tuple()

    def __repr__(self):
        return "\n".join(''.join(map(str, self.data[9*(i+0):9*(i+1)])) for i in range(9))

    def _indexes_of(self, o):
        return tuple(i for i, v in enumerate(self.data) if v==o)
    def solve(self):
        self.empty_indexes = self._indexes_of(0)
        self._solve()
    def _solve(self, i=0):
        if i>=len(self.empty_indexes):
            return True
        _i = self.empty_indexes[i]
        for valid_number in self.valid_cell_values(_i):
            self.data[_i] = valid_number
            _solved = self._solve(i+1)
            if _solved:
                return _solved
        self.data[_i] = 0

    def _indexes_to_frozenset(self, indexes):
        return frozenset(map(lambda i: self.data[i], indexes))
    def row_indexes(self, r):
        return range((r*9),(r+1)*9)
    def row(self, r):
        """
        >>> ss = Sudoku2(problem)
        >>> ss.row(0)
        frozenset({0, 3, 5, 7})
        >>> ss.row(1)
        frozenset({0, 1, 5, 6, 9})
        """
        return self._indexes_to_frozenset(self.row_indexes(r))
    def col_indexes(self, c):
        return ((i*9)+c for i in range(9))
    def col(self, c):
        """
        >>> ss = Sudoku2(problem)
        >>> ss.col(0)
        frozenset({0, 4, 5, 6, 7, 8})
        >>> ss.col(1)
        frozenset({0, 9, 3, 6})
        """
        return self._indexes_to_frozenset(self.col_indexes(c))
    def block_indexes(self, row, col):
        return chain.from_iterable(range(i,i+3) for i in ((((row*3)+i)*9)+(col*3) for i in range(3)))
    def block(self, row, col):
        """
        >>> ss = Sudoku2(problem)
        >>> ss.block(0, 0)
        frozenset({0, 3, 5, 6, 8, 9})
        >>> ss.block(1, 1)
        frozenset({0, 2, 3, 6, 8})
        """
        return self._indexes_to_frozenset(self.block_indexes(row, col))
    def valid_cell_values(self, i):
        """
        >>> ss = Sudoku2(problem)
        >>> ss.valid_cell_values(2)
        frozenset({1, 2, 4})
        >>> ss.valid_cell_values(8)
        frozenset({8, 2, 4})
        >>> ss.valid_cell_values(78)
        frozenset({1, 3, 4, 6})
        """
        return self.COMPLETE_NUMBER_SET - self.row(i//9) - self.col(i%9)- self.block(i//9//3, i%9//3)

    @property
    def complete(self):
        """
        >>> Sudoku2(problem).complete
        False
        >>> Sudoku2(solution).complete
        True
        """
        return all(
            s == self.COMPLETE_NUMBER_SET
            for s in chain(
                (self.row(r) for r in range(9)),
                (self.col(c) for c in range(9)),
                (self.block(x,y) for y in range(3) for x in range(3)),
            )
        )

    @staticmethod
    def _randomize_order(data):
        return sorted(data, key=lambda k: random.random())
    def _shuffle(self):
        def swap_indexes_in_place(i1, i2):
            for _i1, _i2 in zip(i1, i2):
                _tmp = self.data[_i1]
                self.data[_i1] = self.data[_i2]
                self.data[_i2] = _tmp

        # Swap numbers in dataset
        nums = self._randomize_order(self.COMPLETE_NUMBER_SET)
        for i in range(3):
            swap_indexes_in_place(self._indexes_of(nums.pop()), self._indexes_of(nums.pop()))

        def shuffle_block_indexes():
            return self._randomize_order(range(3))
        def shuffle_row_col_indexes():
            return tuple(
                r
                for row_block in range(3)
                for r in self._randomize_order(range((row_block+0)*3, (row_block+1)*3))
            )
        # Shuffle rows (group of 3 block)
        for r1, r2 in zip(range(9), shuffle_row_col_indexes()):
            swap_indexes_in_place(self.row_indexes(r1), self.row_indexes(r2))
        # Shuffle cols (group of 3 block)
        for c1, c2 in zip(range(9), shuffle_row_col_indexes()):
            swap_indexes_in_place(self.col_indexes(c1), self.col_indexes(c2))
        # Shuffle block row
        for br1, br2 in zip(range(3), shuffle_block_indexes()):
            swap_indexes_in_place(
                chain.from_iterable(self.block_indexes(br1, col) for col in range(3)), 
                chain.from_iterable(self.block_indexes(br2, col) for col in range(3)),
            )
        # Shuffle block col
        for bc1, bc2 in zip(range(3), shuffle_block_indexes()):
            swap_indexes_in_place(
                chain.from_iterable(self.block_indexes(row, bc1) for row in range(3)), 
                chain.from_iterable(self.block_indexes(row, bc2) for row in range(3)),
            )
    def shuffle(self):
        """
        >>> ss = Sudoku2(solution)
        >>> data_copy = list(ss.data)
        >>> ss.data == data_copy
        True
        >>> ss.complete
        True
        >>> ss.shuffle()
        >>> ss.data == data_copy
        False
        >>> ss.complete
        True
        """
        for i in range(5):
            self._shuffle()
    def create(self, difficulty=20):
        """
        >>> ss = Sudoku2(solution)
        >>> ss.complete
        True
        >>> ss.create()
        >>> ss.complete
        False
        >>> ss.solve()
        >>> ss.complete
        True
        """
        assert self.complete
        self.shuffle()
        for i in self._randomize_order(range(9*9))[:difficulty]:
            self.data[i] = 0



    # Old experiment -----------------------------------------------------------

    def valid_cell_values2(self, i):
        """
        Experiment
        Alternate implementation of valid_cell_values in a single function
        I don't think this is clearer than separate functions to get collections
        >>> ss = Sudoku2(problem)
        >>> ss.valid_cell_values2(2)
        frozenset({1, 2, 4})
        >>> ss.valid_cell_values2(8)
        frozenset({8, 2, 4})
        >>> ss.valid_cell_values2(78)
        frozenset({1, 3, 4, 6})
        """
        row_num, col_num = i//9, i%9
        row_index = row_num*9
        block_row, block_col = (row_num//3)*3, (col_num//3)*3
        return (
            self.COMPLETE_NUMBER_SET
            - frozenset(self.data[row_index:row_index+9])
            - frozenset(self.data[row_num*9 + col_num] for row_num in range(9))
            - frozenset(chain.from_iterable(
                self.data[block_i:block_i+3] 
                for block_i in (((block_row+r)*9)+block_col for r in range(3))
            ))
        )






# Same as Sudoku2 but just the solver simplified
class Sudoku3():
    COMPLETE_NUMBER_SET = frozenset(i+1 for i in range(9))

    def __init__(self, data):
        self.data = list(int(i) for i in re.sub(r'\D', '', data))
        assert len(self.data) == 9*9
        self.empty_indexes = tuple(i for i, v in enumerate(self.data) if not v)

    def __repr__(self):
        return "\n".join(''.join(map(str, self.data[9*(i+0):9*(i+1)])) for i in range(9))

    def solve(self, i=0):
        if i>=len(self.empty_indexes):
            return True
        _i = self.empty_indexes[i]
        for valid_number in self.valid_cell_values(_i):
            self.data[_i] = valid_number
            _solved = self.solve(i+1)
            if _solved:
                return _solved
        self.data[_i] = 0

    def row(self, r):
        return frozenset(self.data[(r*9):(r+1)*9])
    def col(self, c):
        return frozenset(self.data[(i*9)+c] for i in range(9))
    def block(self, row, col):
        return frozenset(chain.from_iterable(self.data[i:i+3] for i in ((((row*3)+i)*9)+(col*3) for i in range(3))))
    def valid_cell_values(self, i):
        return self.COMPLETE_NUMBER_SET - self.row(i//9) - self.col(i%9)- self.block(i//9//3, i%9//3)




if __name__ == "__main__":
    ss = Sudoku2(problem)
    #print(ss)
    #print(f'Missing {Sudoku._percent_data_missing(ss._base)*100:.2f}%')
    #input()
    #breakpoint()
    ss.solve()

    #print("\033c", end='')
    #print(f"solved it in {ss._debug_counter} comparisons")
    print(ss)
    #print(ss.complete)
