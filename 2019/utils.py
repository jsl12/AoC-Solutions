import operator

def segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    # http: // www.cs.swan.ac.uk / ~cssimon / line_intersection.html
    denom = (x4 - x3) * (y1 - y2) - (x1 - x2) * (y4 - y3)
    r = ((y3 - y4) * (x1 - x3) + (x4 - x3) * (y1 - y3)) / denom
    s = ((y1 - y2) * (x1 - x3) + (x2 - x1) * (y1 - y3)) / denom

    if 0 < r < 1 and 0 < s < 1:
        x_cross = x1 + (x2 - x1) * r
        y_cross = y1 + (y2 - y1) * r
        return round(x_cross), round(y_cross)


class IntcodeComputer:


    def __init__(self, input_str, inputs=None):
        self.seq = [int(i) for i in input_str.split(',')]
        self.ORIGINAL_SEQ = self.seq[:]
        self.pos = 0
        if inputs is not None:
            self.inputs = inputs
        self.outputs = []
        self.op_funcs = {
            1: (operator.add, 3),
            2: (operator.mul, 3),
            3: (self.input, 1),
            4: (self.output, 1),
            5: (self.jump_true, 2),
            6: (self.jump_false, 2),
            7: (operator.lt, 3),
            8: (operator.eq, 3)
        }

    def __str__(self):
        return str(self.seq)

    def reset(self):
        self.seq = self.ORIGINAL_SEQ[:]
        self.pos = 0
        self.outputs = []

    @property
    def full_opcode(self):
        return f'{self.seq[self.pos]:0>5d}'

    @property
    def op(self):
        return int(self.full_opcode[-2:])

    @property
    def modes(self):
        return [int(i) for i in self.full_opcode[:-2]][::-1]

    @property
    def resolved_params(self):
        """
        >>> ic = IntcodeComputer('1,0,0,0,99')
        >>> ic.resolved_params
        [1, 1, 1]
        >>> ic = IntcodeComputer('2,3,0,3,99')
        >>> ic.resolved_params
        [3, 2, 3]
        """
        modes = self.modes
        op_num = self.op
        num_params = self.op_funcs[op_num][1]
        raw_params = [self.seq[self.pos + i + 1] for i in range(num_params)]
        resolved_params = [self.seq[p] if modes[i] == 0 else p for i, p in enumerate(raw_params)]

        if op_num == 4:
            resolved_params.append('pad')
        return resolved_params

    def input(self):
        return self.inputs.pop(0)

    def output(self, value):
        return value

    def jump_true(self, value):
        return value != 0

    def jump_false(self, value):
        return value == 0

    def advance(self):
        num = self.op_funcs[self.op][1] + 1
        self.pos += num

    def rerun(self, new_input):
        self.reset()
        self.inputs = new_input
        return self.run()

    def run(self):
        """
        Run the Intcode program until completion (opcode 99)

        :return:

        >>> ic = IntcodeComputer('1,0,0,0,99')
        >>> ic.run()
        >>> ic.seq
        [2, 0, 0, 0, 99]
        >>> ic = IntcodeComputer('2,3,0,3,99')
        >>> ic.run()
        >>> ic.seq
        [2, 3, 0, 6, 99]
        >>> ic = IntcodeComputer('2,4,4,5,99,0')
        >>> ic.run()
        >>> ic.seq
        [2, 4, 4, 5, 99, 9801]
        >>> ic = IntcodeComputer('1,1,1,4,99,5,6,0,99')
        >>> ic.run()
        >>> ic.seq
        [30, 1, 1, 4, 2, 5, 6, 0, 99]
        >>> ic = IntcodeComputer('1002,4,3,4,33')
        >>> ic.run()
        >>> ic.seq
        [1002, 4, 3, 4, 99]

        >>> ic = IntcodeComputer('3,9,8,9,10,9,4,9,99,-1,8', [8])
        >>> ic.run()
        1
        >>> ic.rerun([7])
        0

        >>> ic = IntcodeComputer('3,9,7,9,10,9,4,9,99,-1,8', [7])
        >>> ic.run()
        1
        >>> ic.rerun([8])
        0


        >>> ic = IntcodeComputer('3,3,1108,-1,8,3,4,3,99', [8])
        >>> ic.run()
        1
        >>> ic.rerun([7])
        0

        >>> ic = IntcodeComputer('3,3,1107,-1,8,3,4,3,99', [7])
        >>> ic.run()
        1
        >>> ic.rerun([8])
        0

        >>> ic = IntcodeComputer('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', [7])
        >>> ic.run()
        1
        >>> ic.rerun([0])
        0

        >>> ic = IntcodeComputer('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', [7])
        >>> ic.run()
        1
        >>> ic.rerun([0])
        0

        >>> ic = IntcodeComputer(
        ...     '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99',
        ...     [7])
        >>> ic.run()
        999
        >>> ic.rerun([8])
        1000
        >>> ic.rerun([9])
        1001
        """
        while self.op != 99:
            self.operate()
        if self.outputs:
            return self.outputs.pop(0)

    def operate(self):
        op_num = self.op
        params = self.resolved_params
        func, num_params = self.op_funcs[op_num]
        res = int(func(*params[:-1]))
        jumped = False

        if op_num in [1, 2, 7, 8]:
            self.seq[self.seq[self.pos + 3]] = res
        elif op_num == 3:
            self.seq[self.seq[self.pos + 1]] = res
        elif op_num == 4:
            self.outputs.append(res)
        elif op_num in [5, 6]:
            if res == 1:
                self.pos = params[-1]
                jumped = True
        if not jumped:
            self.advance()


if __name__ == '__main__':
    import doctest
    doctest.testmod()