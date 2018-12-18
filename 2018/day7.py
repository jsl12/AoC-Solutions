import re

REGEX = re.compile('Step (\w) must be finished before step (\w) can begin.')

def parse(line):
    match = REGEX.match(line)
    return match.group(1), match.group(2)

def create_steps(input):
    steps = {}
    for i in [parse(line) for line in input.splitlines()]:
        if i[1] in steps:
            steps[i[1]].append(i[0])
        else:
            steps[i[1]] = [i[0]]
    return steps

def find_start(steps):
    s = next(iter(steps.keys()))
    while s in steps:
        s = steps[s][0]
    return s

def find_ready(steps, done):
    res = sorted([s for s in steps if all([ps in done for ps in steps[s]])])
    return res[0]

def part1(input):
    steps = create_steps(input)
    done = list(find_start(steps))
    n = len(steps)
    while len(done) <= n:
        done.append(find_ready(steps, done))
        steps.pop(done[-1])
    return ''.join(done)

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 7
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))