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

    def __str__(self):
        return str(self.seq)

    def reset(self):
        self.seq = self.ORIGINAL_SEQ[:]
        self.pos = 0

    def op_codes(self):
        res = []
        self.pos = 0
        while self.pos < len(self.seq):
            val = int(str(self.seq[self.pos])[-2:])
            res.append(val)
            if val == 1 or val == 2:
                self.pos += 4
            elif val == 3 or val == 4:
                self.pos += 2
        return res

    def run(self):
        """
        Run the Intcode program until completion

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
        >>> ic.outputs[0]
        1
        >>> ic = IntcodeComputer('3,9,8,9,10,9,4,9,99,-1,8', [7])
        >>> ic.run()
        >>> ic.outputs[0]
        0
        >>> ic = IntcodeComputer('3,9,7,9,10,9,4,9,99,-1,8', [7])
        >>> ic.run()
        >>> ic.outputs[0]
        1
        >>> ic = IntcodeComputer('3,9,7,9,10,9,4,9,99,-1,8', [8])
        >>> ic.run()
        >>> ic.outputs[0]
        0
        >>> ic = IntcodeComputer('3,3,1108,-1,8,3,4,3,99', [8])
        >>> ic.run()
        >>> ic.outputs[0]
        1
        >>> ic = IntcodeComputer('3,3,1108,-1,8,3,4,3,99', [7])
        >>> ic.run()
        >>> ic.outputs[0]
        0
        >>> ic = IntcodeComputer('3,3,1107,-1,8,3,4,3,99', [7])
        >>> ic.run()
        >>> ic.outputs[0]
        1
        >>> ic = IntcodeComputer('3,3,1107,-1,8,3,4,3,99', [8])
        >>> ic.run()
        >>> ic.outputs[0]
        0
        >>> ic = IntcodeComputer('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', [7])
        >>> ic.run()
        >>> ic.outputs[0]
        1
        >>> ic = IntcodeComputer('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', [0])
        >>> ic.run()
        >>> ic.outputs[0]
        0
        """
        while self.seq[self.pos] != 99:
            self.operate()

    def operate(self):
        params = self.get_params()
        op = params.pop(0)
        params[-1] = self.seq[self.pos+len(params)]

        jumped = False
        if op == 1:
            self.seq[params[2]] = params[0] + params[1]
        elif op == 2:
            self.seq[params[2]] = params[0] * params[1]
        elif op == 3:
            self.seq[params[0]] = self.inputs.pop()
        elif op == 4:
            self.outputs.append(self.seq[params[0]])
            pass
        elif op == 5:
            if params[0] != 0:
                self.pos = params[1]
                jumped = True
        elif op == 6:
            if params[0] == 0:
                self.pos = params[1]
                jumped = True
        elif op == 7:
            if params[0] < params[1]:
                self.seq[params[2]] = 1
            else:
                self.seq[params[2]] = 0
        elif op == 8:
            if params[0] == params[1]:
                self.seq[params[2]] = 1
            else:
                self.seq[params[2]] = 0

        if not jumped:
            self.pos += len(params) + 1

    def get_params(self):
        """
        Resolves the actual values needed for the operation

        :return: [op, value1, value2, ..., placeholder]

        >>> ic = IntcodeComputer('1002,4,3,4,33')
        >>> ic.get_params()
        [2, 33, 3, 0]
        """
        params = self.get_modes(self.seq[self.pos])
        # last one is usually position, so it doesn't need to be resolved
        for i, m in enumerate(params[1:-1]):
            param_loc = self.pos + i + 1
            if m == 0:
                param = self.seq[self.seq[param_loc]]
            elif m == 1:
                param = self.seq[param_loc]
            else:
                raise ValueError(f'invalid mode: {m}')
            params[i+1] = param
        return params

    def get_modes(self, input):
        """
        Get the modes of the parameters - positional (0) or immediate (1)

        :param input: str
        :return: [op, mode1, mode2, ...]

        >>> ic = IntcodeComputer('1,0,0,0,99')
        >>> ic.get_modes(ic.seq[ic.pos])
        [1, 0, 0, 0]
        >>> ic = IntcodeComputer('1002,4,3,4,33')
        >>> ic.get_modes(ic.seq[ic.pos])
        [2, 0, 1, 0]
        """
        opcode = f'{int(input):0>5d}'
        op = int(opcode[-2:])

        param_table = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3
        }
        try:
            modes = [op] + [int(c) for c in opcode[:-2][:param_table[op]][::-1]]
        except KeyError as e:
            print(f'Invalid operation: {self.seq}')
            raise
        return modes

    def noun_verb(self, noun, verb):
        self.seq[1] = noun
        self.seq[2] = verb
        while True:
            if self.seq[self.pos] == 99:
                break
            self.operate()

        return self.seq[0]

    def scan(self, target_val):
        for noun in range(99):
            for verb in range(99):
                self.reset()
                self.noun_verb(noun, verb)
                if self.seq[0] == target_val:
                    break
            if self.seq[0] == target_val:
                break
        return noun, verb

if __name__ == '__main__':
    import doctest
    doctest.testmod()