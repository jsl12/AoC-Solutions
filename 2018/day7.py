import re

REGEX = re.compile('Step (\w) must be finished before step (\w) can begin.')

def parse(line):
    match = REGEX.match(line)
    return match.group(1), match.group(2)

class Step:
    def __repr__(self):
        if not hasattr(self, 'pre_steps'):
            return '{} -> '.format(self.id)
        else:
            return '{} -> {}'.format(self.id, ', '.join(self.pre_steps))

    def __init__(self, step, pre_steps=None):
        self.id = step
        if pre_steps is not None:
            self.add_pre_step(pre_steps)

    def add_pre_step(self, pre_step):
        if not hasattr(self, 'pre_steps'):
            self.pre_steps = set(pre_step)
        else:
            self.pre_steps.add(pre_step)

def create_steps(input):
    steps = {}
    for i in [parse(line) for line in input.splitlines()]:
        if i[1] in steps:
            steps[i[1]].append(i[0])
        else:
            steps[i[1]] = [i[0]]
    return [Step(s, steps[s]) for s in steps]

def part1(input):
    steps = create_steps(input)
    return

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 7
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))