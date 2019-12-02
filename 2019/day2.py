from dataclasses import dataclass
from typing import List

class OpSeq:
    def __init__(self, input_str):
        self.seq = [int(i) for i in input_str.split(',')]
        self.pos = 0

    def reset(self):
        self.seq[1] = 12
        self.seq[2] = 2

    def process_opcode(self, opcode, val1_pos, val2_pos, res_pos):
        if opcode == 1:
            self.seq[res_pos] = self.seq[val1_pos] + self.seq[val2_pos]
        elif opcode == 2:
            self.seq[res_pos] = self.seq[val1_pos] * self.seq[val2_pos]

    def process(self, reset=True):
        if reset:
            self.reset()
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


def part1(input, reset=False):
    os = OpSeq(input)
    os.process(reset)
    return os.seq[0]


def part2(input):
    return


if __name__ == '__main__':
    import aoc_input as inp

    DAY = 2
    print(part1(inp.read(DAY), reset=True))
    # print(part2(inp.read(DAY)))
