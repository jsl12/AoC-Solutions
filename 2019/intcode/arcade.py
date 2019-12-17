import numpy as np

from . import Computer, NoInputException


class Arcade:
    def __init__(self, input, free=True):
        self.ic = Computer(input)
        if free:
            self.ic.seq[0] = 2
        self.array = np.full((25, 50), ' ')

    def input(self, val):
        self.ic.inputs.append(val)

    def print(self):
        for i, line in enumerate(self.render()):
            if i == 0:
                line = line.replace('|', '-')
            print(line)

    def render(self):
        for row in self.array:
            yield ''.join(row)

    def count_blocks(self):
        blocks = 0
        for x, y, tile in self.tile_gen():
            if tile == 2:
                blocks += 1
        return blocks

    def tile_gen(self):
        while self.ic.op != 99:
            try:
                self.ic.run(output_stop=3)
            except NoInputException:
                self.input(0)
                continue

            if self.ic.op != 99:
                res = tuple(self.ic.outputs[:])
                self.ic.outputs = []
                yield res
        return

    def play(self):
        tiles = {
            3: 'Paddle',
            4: 'Ball'
        }
        for x, y, tile in self.tile_gen():
            if x == -1 and y == 0:
                self.score = tile
            else:
                self.handle_tile(x, y, tile)
        return self.score

    def handle_tile(self, x, y, tile):
        chars = {
            0: ' ',
            1: '|',
            2: '@',
            3: '~',
            4: '.'
        }
        self.array[y, x] = chars[tile]

        if tile == 3:
            self.paddle = (y, x)
        elif tile == 4:
            self.ball = (y, x)
            if hasattr(self, 'paddle'):
                if self.ball[1] < self.paddle[1]:
                    res = -1
                elif self.ball[1] > self.paddle[1]:
                    res = 1
                else:
                    res = 0
                self.input(res)

                # if abs(self.ball[1] - self.paddle[1]) <= 1:
                #     self.print()
