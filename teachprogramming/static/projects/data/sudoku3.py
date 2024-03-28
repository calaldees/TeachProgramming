from itertools import chain
import re

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


if __name__ == '__main__':
        s = Sudoku3("""
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
        """)
        print(s)
        print()
        s.solve()
        print(s)