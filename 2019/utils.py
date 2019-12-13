import operator
from itertools import permutations

def segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    # http: // www.cs.swan.ac.uk / ~cssimon / line_intersection.html
    denom = (x4 - x3) * (y1 - y2) - (x1 - x2) * (y4 - y3)
    r = ((y3 - y4) * (x1 - x3) + (x4 - x3) * (y1 - y3)) / denom
    s = ((y1 - y2) * (x1 - x3) + (x2 - x1) * (y1 - y3)) / denom

    if 0 < r < 1 and 0 < s < 1:
        x_cross = x1 + (x2 - x1) * r
        y_cross = y1 + (y2 - y1) * r
        return round(x_cross), round(y_cross)


class AmpSystem:
    def __init__(self, input, len=5):
        self.amps = [IntcodeComputer(input) for i in range(len)]

    def reset(self):
        for a in self.amps:
            a.reset()

    def assign_inputs(self, inputs):
        for i, a in enumerate(self.amps):
            a.inputs.append(inputs[i])

    def max_thruster_signal(self, possible_settings):
        return max([self.run(list(settings)) for settings in permutations(possible_settings)])

    def run(self, settings, signal = 0):
        self.reset()
        self.assign_inputs(settings)
        self.amps[0].inputs.append(signal)
        while self.amps[-1].op != 99:
            # for each amplifier, try to operate
            for i, a in enumerate(self.amps):
                # check for any outputs ready to go
                if self.amps[i-1].outputs:
                    for j in range(len(self.amps[i-1].outputs)):
                        a.inputs.append(self.amps[i-1].outputs.pop(0))
                if a.op == 3 and not a.inputs:
                    # if it needs an input and there are none available, then skip
                    continue
                try:
                    a.run()
                except IndexError:
                    # hits an index error when it tries to pull an input and there are none available
                    continue
        return self.amps[-1].outputs[0]


class IntcodeComputer:
    def __init__(self, input_str, inputs=None):
        self.seq = [int(i) for i in input_str.split(',')]
        self.ORIGINAL_SEQ = self.seq[:]
        self.pos = 0
        if inputs is not None:
            self.inputs = inputs
        else:
            self.inputs = []
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
        self.ops_completed = 0

    def __str__(self):
        res = f'{self.inputs} -> '
        for i, val in enumerate(self.seq):
            res += (f'{val}' if i != self.pos else f'({val})') + ','
        res += f' -> {self.outputs}'
        return res

    def reset(self):
        self.seq = self.ORIGINAL_SEQ[:]
        self.pos = 0
        self.outputs = []
        self.ops_completed = 0

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
        self.run()
        return self.outputs[0]

    def run(self):
        """
        Run the Intcode program until completion (opcode 99)

        :return: the last output
        """
        while self.op != 99:
            self.operate()
        if self.outputs:
            return self.outputs[0]

    def operate(self):
        """
        Complete a single operation based on wherever the current instruction pointer (self.pos) is
        :return:
        """
        op_num = self.op
        params = self.resolved_params
        func, num_params = self.op_funcs[op_num]
        jumped = False

        if op_num in [1, 2, 7, 8]:
            res = int(func(*params[:-1]))
            self.seq[self.seq[self.pos + 3]] = res
        elif op_num == 3:
            res = int(func())
            self.seq[self.seq[self.pos + 1]] = res
        elif op_num == 4:
            res = int(func(params[0]))
            self.outputs.append(res)
        elif op_num in [5, 6]:
            res = int(func(*params[:-1]))
            if res == 1:
                self.pos = params[-1]
                jumped = True
        if not jumped:
            self.advance()
        self.ops_completed += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()