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
    def __init__(self, input_str):
        self.seq = [int(i) for i in input_str.split(',')]
        self.ORIGINAL_SEQ = self.seq[:]
        self.pos = 0
        self.outputs = []

    def __str__(self):
        return str(self.seq)

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


    def reset(self):
        self.seq = self.ORIGINAL_SEQ[:]
        self.pos = 0

    def noun_verb(self, noun, verb):
        self.seq[1] = noun
        self.seq[2] = verb
        while True:
            if self.seq[self.pos] == 99:
                break
            self.operate()

        return self.seq[0]

    def operate(self):
        opcode = f'{self.seq[self.pos]:0>5d}'
        op = int(opcode[-2:])

        params = self.get_params()

        if op == 1:
            self.seq[params[2]] = params[0] + params[1]
        elif op == 2:
            self.seq[params[2]] = params[0] * params[1]
        elif op == 3:
            self.seq[params[0]] = self.inputs.pop()
        elif op == 4:
            self.outputs.append(self.seq[params[0]])
        self.pos += len(params) + 1


    def get_params(self):
        opcode = f'{self.seq[self.pos]:0>5d}'
        op = int(opcode[-2:])

        if op == 1 or op == 2:
            num_params = 3
        elif op == 3 or op == 4:
            num_params = 1
        else:
            print(f'Unknown op: {op}')

        modes = opcode[::-2][:num_params]

        params = []
        for i, m in enumerate(modes):
            param_loc = self.pos + i + 1
            if m == '0':
                param = self.seq[self.seq[param_loc]]
            elif m == '1':
                param = self.seq[param_loc]
            else:

            params.append(param)
        return params


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