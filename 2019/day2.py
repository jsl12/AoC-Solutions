class OpSeq:
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

def part1(input):
    os = OpSeq(input)
    os.run_program(noun=12, verb=2)
    return os.seq[0]


def part2(input):
    os = OpSeq(input)
    target_val = 19690720
    noun, verb = os.scan(target_val)
    return 100 * noun + verb


if __name__ == '__main__':
    import aoc_input as inp

    DAY = 2
    print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
