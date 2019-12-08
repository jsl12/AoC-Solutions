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

    def __str__(self):
        return str(self.seq)

    def reset(self):
        self.seq = self.ORIGINAL_SEQ[:]
        self.pos = 0

    def process_opcode(self, opcode, val1_pos, val2_pos, res_pos):
        if opcode == 1:
            self.seq[res_pos] = self.seq[val1_pos] + self.seq[val2_pos]
        elif opcode == 2:
            self.seq[res_pos] = self.seq[val1_pos] * self.seq[val2_pos]

    def run_program(self, noun, verb):
        self.seq[1] = noun
        self.seq[2] = verb
        while True:
            if self.seq[self.pos] == 99:
                break
            else:
                self.process_opcode(
                    opcode=self.seq[self.pos],
                    val1_pos=self.seq[self.pos + 1],
                    val2_pos=self.seq[self.pos + 2],
                    res_pos=self.seq[self.pos + 3]
                )
                self.pos += 4
        return self.seq[0]

    def scan(self, target_val):
        for noun in range(99):
            for verb in range(99):
                self.reset()
                self.run_program(noun, verb)
                if self.seq[0] == target_val:
                    break
            if self.seq[0] == target_val:
                break
        return noun, verb