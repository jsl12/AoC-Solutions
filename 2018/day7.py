import re

REGEX = re.compile('Step (\w) must be finished before step (\w) can begin.')

def parse(line):
    match = REGEX.match(line)
    return match.group(2), match.group(1)

def find_ready(dependencies, completed):
    ready = sorted([key for key in dependencies if all([c in completed for c in dependencies[key]])])
    new_ready = [c for c in ready if c not in completed]
    return new_ready

def part1(input):
    input = sorted([parse(line) for line in input.splitlines()])
    dependencies = {}
    for i in range(ord('A'), ord('Z')):
        dependencies[chr(i)] = [inp[1] for inp in input if inp[0] == chr(i)]

    completed = []
    def proc(dependencies, completed):
        ready = find_ready(dependencies, completed)
        if ready:
            completed.extend(ready)
            proc(dependencies, completed)
    proc(dependencies, completed)
    return ''.join(completed)

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 7
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))