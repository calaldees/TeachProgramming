
class Conway():

    def __init__(self, state=None, width=0, height=0):
        self._state = state or {}
        self.width = width
        self.height = height

    def _count_neighbours(self, x, y):
        return sum(
            self._get_cell(x+_x, y+_y)
            for _y in (-1, 0, 1)
            for _x in (-1, 0, 1)
            if not (_x == 0 and _y == 0)
        )

    def _get_cell(self, x, y):
        return self._state.get((x, y), False)

    def next(self):
        new_state = {}
        for y in range(self.height):
            for x in range(self.width):
                neighbour_count = self._count_neighbours(x, y)
                alive = (
                    neighbour_count == 3 or
                    (self._get_cell(x, y) and neighbour_count == 2)
                )
                if alive:
                    new_state[(x, y)] = True
        self._state = new_state


def _conway_load(filehandle):
    r"""
    >>> _conway_load()
    ''
    """
    state = {}
    width = 0
    height = 0
    for y, line in enumerate(filehandle):
        height = y + 1
        width = max(width, len(line))
        for x, i in enumerate(line.strip()):
            if not (i == '.' or i == ' '):
                state[(x, y)] = True
    return (state, width, height)
def conway_load(filename):
    with open(filename, 'rt', encoding='utf-8') as filehandle:
        return _conway_load(filehandle)


def conway_display(conway):
    for y in range(conway.height):
        print(''.join(
            '#' if conway._get_cell(x, y) else '.'
            for x in range(conway.width)
        ))

conway = Conway(*conway_load('conway.txt'))
conway_display(conway)

import time
for i in range(20):
    time.sleep(1)
    print('')
    conway.next()
    conway_display(conway)
