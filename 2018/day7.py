import re

REGEX = re.compile('Step (\w) must be finished before step (\w) can begin.')

def parse(line):
    match = REGEX.match(line)
    return match.group(2), match.group(1)

class Step:
    def __repr__(self):
        return '{} -> {}'.format(self.pre_step, self.step)

    def __init__(self, pre_step, step):
        self.pre_step = pre_step
        self.step = step

def part1(input):
    input = [Step(*parse(line)) for line in input.splitlines()]
    return

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 7
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))