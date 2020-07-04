
class Conway():

    def __init__(self, state=None, width=0, height=0):
        self._state = state or set()
        self.width = width
        self.height = height

    def get_cell(self, x, y):
        return (x, y) in self._state

    def next(self):
        def _count_neighbours(i):
            x, y = i
            return len(self._state & {
                (x + _x, y + _y)
                for _y in (-1, 0, 1)
                for _x in (-1, 0, 1)
                if not (_x == 0 and _y == 0)
            })
        def _is_cell_alive(i):
            neighbour_count = _count_neighbours(i)
            return (
                neighbour_count == 3 or
                (i in self._state and neighbour_count == 2)
            )
        def _cells_to_check_generator():
            for i in self._state:
                x, y = i
                yield from {
                    (x + _x, y + _y)
                    for _y in (-1, 0, 1)
                    for _x in (-1, 0, 1)
                }
        self._state = {i for i in set(_cells_to_check_generator()) if _is_cell_alive(i)}


class ConwayFactory():

    @staticmethod
    def conway_from_file(filename):
        return Conway(*ConwayFactory.parse(filename))

    @staticmethod
    def parse(filename):
        with open(filename, 'rt', encoding='utf-8') as filehandle:
            if filename.endswith('.txt'):
                return ConwayFactory._parse_txt(filehandle)
            if filename.endswith('.rle'):
                return ConwayFactory._parse_rle(filehandle)

    @staticmethod
    def _parse_txt(filehandle):
        r"""
        >>> ConwayFactory._parse_txt((
        ...     '.#.',
        ...     '###',
        ...     '..#',
        ... ))
        ({(0, 1), (2, 1), (2, 2), (1, 0), (1, 1)}, 3, 3)
        """
        state = set()
        width = 0
        height = 0
        for y, line in enumerate(filehandle):
            height = y + 1
            width = max(width, len(line))
            for x, i in enumerate(line.rstrip()):
                if not (i == '.' or i == ' '):
                    state.add((x, y))
        return (state, width, height)

    @staticmethod
    def _parse_cells(filehandle):
        """
        TODO: `.cells` format is a formal format on conway wiki and should be implemented
        Maybe the txt parser can be updated to use cells
        (
            '! comment',
            '.O.',
            'OOO',
            '..O',
            '',
            'OO',
            'O',
            '',
        )
        """
        pass

    @staticmethod
    def _parse_rle(filehandle):
        r"""
        http://www.conwaylife.com/wiki/RLE

        >>> ConwayFactory._parse_rle((
        ...     '#C This is a glider.',
        ...     'x = 3, y = 3',
        ...     'bo$2bo$3o!',
        ... ))
        ({(1, 2), (2, 1), (2, 2), (1, 0), (0, 2)}, 3, 3)
        """
        import re
        state = set()
        width = 0
        height = 0
        x = 0
        y = 0
        for line in filehandle:
            if line.startswith('#'):
                continue
            if not width and not height:
                width, height = map(int, re.search('x\s*=\s*(?P<x>\d+),\s*y\s*=\s*(?P<y>\d+)', line).groups())
                continue
            for match in re.finditer(r'(?P<repeat>\d{0,4})(?P<char>[bo$!])', line):
                repeats, cell = match.groups()
                repeats = int(repeats) if repeats else 1
                if cell == 'o':
                    for i in range(repeats):
                        state.add((x, y))
                        x += 1
                if cell == 'b':
                    x += repeats
                if cell == '$':
                    for i in range(repeats):
                        y += 1
                    x = 0
                if cell == '!':
                    break
            y += 1
            x = 0
        return (state, width, height)


def conway_display(conway):
    for y in range(conway.height):
        print(''.join(
            '#' if conway.get_cell(x, y) else '.'
            for x in range(conway.width)
        ))


if __name__ == "__main__":
    import sys
    filename = sys.argv[1] if len(sys.argv) == 2 else 'conway.txt'

    conway = ConwayFactory.conway_from_file(filename)
    conway_display(conway)

    import time
    for i in range(20):
        time.sleep(1)
        print('')
        conway.next()
        conway_display(conway)
