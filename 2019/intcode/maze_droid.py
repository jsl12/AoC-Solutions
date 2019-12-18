from .computer import Computer


class Completed(Exception):
    pass


class MazeDroid:
    dirs = (1, 4, 2, 3)
    reverse = {
        1: 2,
        2: 1,
        3: 4,
        4: 3
    }

    def __init__(self, seq):
        self.ic = Computer(seq)
        self.pos = [0, 0]
        self._dir = 0
        self.path = []

    def __str__(self):
        return f'Path: {self.path}'

    @property
    def x(self):
        return self.pos[0]

    @x.setter
    def x(self, val):
        self.pos[0] = val

    @property
    def y(self):
        return self.pos[1]

    @x.setter
    def y(self, val):
        self.pos[1] = val

    @property
    def last_move(self):
        return self.path[-1]

    @property
    def last_rev(self):
        return self.reverse[self.last_move]

    @property
    def dir(self):
        return self.dirs[self._dir]

    def turn(self, dir):
        if 'r' in dir:
            self._dir += 1
        elif 'l' in dir:
            self._dir -= 1

        if 3 < self.dir:
            self._dir = 0
        elif self._dir < 0:
            self._dir = 3

    def move_straight(self, dir):
        count = 0
        while self.move(dir) == 1:
            count += 1
            yield count

    def move(self, input_cmd):
        if not (1 <= input_cmd <= 4):
            raise ValueError(f'Invalid move: {input_cmd}')

        self.ic.inputs.append(input_cmd)
        res = self.ic.run(1)

        if res == 1:
            if input_cmd == 1:
                self.y += 1
            elif input_cmd == 2:
                self.y -= 1
            elif input_cmd == 3:
                self.x -= 1
            elif input_cmd == 4:
                self.x += 1

            if not self.path:
                self.path.append(input_cmd)
            else:
                if input_cmd == self.last_rev:
                    self.path.pop()
                else:
                    self.path.append(input_cmd)
        elif res == 2:
            raise Completed(f'Found end of puzzle at {self.pos}')
        return res

    def probe(self, input_cmd):
        res = self.move(input_cmd)
        if res == 0:
            return False
        elif res == 1:
            res = self.move(self.reverse[input_cmd])
            assert res == 1
            return True

    def probe_all(self):
        return [d for d in self.dirs if self.probe(d)]
