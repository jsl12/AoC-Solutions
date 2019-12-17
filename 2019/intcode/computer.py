import operator
from collections.abc import Iterable


class NoInputException(Exception):
    pass


class Computer:
    def __init__(self, input_str, inputs=None):
        self.seq = [int(i) for i in input_str.split(',')]
        self.ORIGINAL_SEQ = self.seq[:]
        self.rel_base = 0
        self.reset()

        if isinstance(inputs, Iterable):
            self.inputs = list(inputs)
        elif inputs is None:
            self.inputs = []
        else:
            self.inputs = [inputs]

        # op_num: (function, num_inputs, num_outputs)
        self.op_funcs = {
            1: (operator.add, 2, 1),
            2: (operator.mul, 2, 1),
            3: (self.pop_from_input, 0, 1),
            4: (self.output, 1, 0),
            5: (self.jump_true, 2, 0),
            6: (self.jump_false, 2, 0),
            7: (operator.lt, 2, 1),
            8: (operator.eq, 2, 1),
            9: (self.adjust_rel_base, 1, 0)
        }

    def __str__(self):
        res = f'{self.inputs} -> '
        for i, val in enumerate(self.seq[:16]):
            res += (f'{val}' if i != self.pos else f'({val})') + ','
        if len(self.seq) > 16:
            res += f' ...({len(self.seq[16:])} more nums)'
        res += f' -> {self.outputs}'
        return res

    def __getitem__(self, pos):
        if pos is None:
            return self.pop_from_input()
        else:
            if pos >= len(self.seq):
                self.seq.extend([0 for i in range(pos - len(self.seq) + 1)])
            return self.seq[pos]

    def __setitem__(self, pos, value):
        if pos is None:
            self.outputs.append(value)
        else:
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

    def pop_from_input(self):
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

    def run(self, output_count=None):
        res = None
        for op_num in self.op_gen():
            self.proc(
                op_num=op_num,
                inputs=self.resolve_inputs(self.num_inputs(op_num)),
                output_pos=self.output_pos(op_num)
            )

            if op_num != 5 and op_num != 6:
                self.advance()

            if output_count is not None and len(self.outputs) >= output_count:
                res = [self.outputs.pop(0) for i in range(output_count)]
                break

        if self.outputs:
            res = self.outputs

        if res is not None:
            if len(res) == 1:
                return res[0]
            else:
                return res

    def op_gen(self):
        while self.op != 99:
            yield self.op

    def proc(self, op_num, inputs, output_pos):
        op_func = self.op_funcs[op_num][0]
        if op_num in [1, 2, 3, 4, 7, 8]:
            self[output_pos] = int(op_func(*inputs))

        elif op_num == 5 or op_num == 6:
            res = int(op_func(inputs[0]))
            if res == 1:
                self.pos = inputs[1]
            else:
                self.advance()

        elif op_num == 9:
            op_func(*inputs)

        else:
            raise ValueError(f'Unknown opcode: {op_num}')

    def advance(self):
        num = sum(self.op_funcs[self.op][1:]) + 1
        self.pos += num

    def num_inputs(self, op_num):
        return self.op_funcs[op_num][1]

    def num_outputs(self, op_num):
        return self.op_funcs[op_num][0]

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

    def output_pos(self, op_num):
        param_count = sum(self.op_funcs[op_num][1:])
        loc = self.pos + param_count
        mode = self.modes[param_count-1]

        if op_num == 4:
            return None
        elif mode == 0:
            return self[loc]
        elif mode == 1:
            return loc
        elif mode == 2:
            return self.rel_base + self[loc]
