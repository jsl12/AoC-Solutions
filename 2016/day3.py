class SpiralMem:
    def __init__(self):
        self.pos = (0, 0)
        self.value = 1
        self.vals = {self.pos: self.value}
        self.side_length = 1
        self.dir = 'RIGHT'

    def move(self, distance=1):
        if distance > self.side_length:
            distance = self.side_length
        if self.dir == 'RIGHT':
            self.pos = (self.pos[0] + distance, self.pos[1])
        elif self.dir == 'UP':
            self.pos = (self.pos[0], self.pos[1] + distance)
        elif self.dir == 'LEFT':
            self.pos = (self.pos[0] - distance, self.pos[1])
        elif self.dir == 'DOWN':
            self.pos = (self.pos[0], self.pos[1] - distance)

        if self.vals.get(self.pos, None) is None:
            self.value = self.calc_value()
            self.vals[self.pos] = self.value
        else:
            self.value = self.vals[self.pos]
        return self.pos

    def calc_value(self):
        return self.value + 1

    def move_along_side(self):
        for i in range(self.side_length):
            self.move()
            if self.value >= self.input:
                return
        self.turn()

    def turn(self, dir='CCW'):
        dirs = {
            'RIGHT': 'UP',
            'UP': 'LEFT',
            'LEFT': 'DOWN',
            'DOWN': 'RIGHT'
        }
        if dir != 'CCW':
            dirs = dict((v, k) for k, v in dirs.items())

        self.dir = dirs[self.dir]
        if self.dir == 'RIGHT' or self.dir == 'LEFT':
            self.side_length += 1

    def move_to(self, input):
        self.input = input
        while self.value < self.input:
            self.move_along_side()

        return self.origin_distance()

    def origin_distance(self):
        return sum([abs(self.pos[0]), abs(self.pos[1])])


class SumSpiral(SpiralMem):
    def calc_value(self):
        self.adj = [cell for cell in self.vals.keys() if abs(cell[0] - self.pos[0]) <= 1 and abs(cell[1] - self.pos[1]) <= 1]
        return sum([self.vals[cell] for cell in self.adj])

    def move_to(self, input):
        self.input = input
        while self.value <= self.input:
            self.move_along_side()
        return self.value

input = 368078
sm = SpiralMem()
print('Input: {}'.format(input))
print('Day 3, Part 1 Answer: {}'.format(sm.move_to(input)))
print(sm.pos, sm.value)

input = 368078
ssm = SumSpiral()
print('Input: {}'.format(input))
print('Day 3, Part 2 Answer: {}'.format(ssm.move_to(input)))
print(ssm.pos)