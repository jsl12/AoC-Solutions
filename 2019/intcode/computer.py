import operator


class Computer:
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