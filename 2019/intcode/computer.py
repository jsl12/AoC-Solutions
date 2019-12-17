import operator


class NoInputException(Exception):
    pass


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
        # op_num: (function, num_inputs, num_outputs)
        self.op_funcs = {
            1: (operator.add, 2, 1),
            2: (operator.mul, 2, 1),
            3: (self.input, 0, 1),
            4: (self.output, 1, 0),
            5: (self.jump_true, 2, 0),
            6: (self.jump_false, 2, 0),
            7: (operator.lt, 2, 1),
            8: (operator.eq, 2, 1),
            9: (self.adjust_rel_base, 1, 0)
        }
        self.ops_completed = 0
        self.rel_base = 0

    def __str__(self):
        res = f'{self.inputs} -> '
        for i, val in enumerate(self.seq):
            res += (f'{val}' if i != self.pos else f'({val})') + ','
        res += f' -> {self.outputs}'
        return res

    def __getitem__(self, pos):
        if pos >= len(self.seq):
            self.seq.extend([0 for i in range(pos - len(self.seq) + 1)])
        return self.seq[pos]

    def __setitem__(self, pos, value):
        if pos >= len(self.seq):
            self.seq.extend([0 for i in range(pos - len(self.seq) + 1)])
        self.seq[pos] = value

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

    def input(self):
        try:
            return self.inputs.pop(0)
        except IndexError:
            raise NoInputException

    def output(self, value):
        return value

    def jump_true(self, value):
        return value != 0

    def jump_false(self, value):
        return value == 0

    def adjust_rel_base(self, value):
        self.rel_base += value

    def advance(self):
        num = sum(self.op_funcs[self.op][1:]) + 1
        self.pos += num

    def rerun(self, new_input):
        self.reset()
        self.inputs = new_input
        self.run()
        return self.outputs[0]

    def run(self, output_stop=None):
        """
        Run the Intcode program until completion (opcode 99)

        :return: the last output
        """
        while self.op != 99:
            self.operate()
            if output_stop is not None and len(self.outputs) >= output_stop:
                break
        if self.outputs:
            return self.outputs[0]

    def operate(self):
        """
        Complete a single operation based on wherever the current instruction pointer (self.pos) is
        :return:
        """
        op_num = self.op
        func, num_inputs, num_outputs = self.op_funcs[op_num]
        jumped = False

        if op_num in [1, 2, 7, 8]:
            res = int(func(*self.resolve_inputs(num_inputs)))
            self[self.resolve_ouput(self.pos + 3, self.modes[2])] = res

        elif op_num == 3:
            res = int(func())
            self[self.resolve_ouput(self.pos + 1, self.modes[0])] = res

        elif op_num == 4:
            res = self.resolve_inputs(num_inputs)[0]
            self.outputs.append(res)

        elif op_num in [5, 6]:
            params = self.resolve_inputs(num_inputs)
            res = int(func(params[0]))
            if res == 1:
                self.pos = params[1]
                jumped = True

        elif op_num == 9:
            func(*self.resolve_inputs(num_inputs))

        if not jumped:
            self.advance()
        self.ops_completed += 1

    def resolve_inputs(self, count):
        def resolve(loc, mode):
            nonlocal self
            if mode == 0:
                return self[self[loc]]
            elif mode == 1:
                return self[loc]
            elif mode == 2:
                return self[self.rel_base + self[loc]]
        return [resolve(self.pos + i + 1, self.modes[i]) for i in range(count)]

    def resolve_ouput(self, loc, mode):
        if mode == 0:
            return self[loc]
        elif mode == 1:
            return loc
        elif mode == 2:
            return self.rel_base + self[loc]
