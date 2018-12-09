import numpy as np
import re

REGEX = re.compile('.*(\d+), (\d+)')

def parse(line):
    match = REGEX.match(line.strip())
    assert match is not None
    return int(match.group(1)), int(match.group(2))

def create_space(input):
    min_x = min([c[0] for c in input])
    max_x = max([c[0] for c in input])
    min_y = min([c[1] for c in input])
    max_y = max([c[1] for c in input])
    res = np.zeros((max_x, max_y), order='F', dtype=np.int16)
    return res

def distance(coord, capital):
    x = abs(coord[0] - capital[0])
    y = abs(coord[1] - capital[1])
    return x + y

def scan_space(space, input):
    it = np.nditer(space, flags=['multi_index'], op_flags=['readwrite'], order='F')
    with it:
        while not it.finished:
            d = np.array([distance(it.multi_index, cap) for cap in input])
            if d[d == d[d.argmin()]].size == 1:
                space[it.multi_index] = d.argmin()
            else:
                space[it.multi_index] = -1
            it.iternext()
    return space

def visualize(space, file):
    with open(file, 'w') as f:
        for row in space:
            row = [chr(int(x) + ord('A')) if int(x) >= 0 else '.' for x in row]
            f.write(''.join(row) + '\n')

def visualize_capitals(input, file):
    max_x = max([c[0] for c in input]) + 3
    max_y = max([c[1] for c in input]) + 3
    for i, cap in enumerate(input):
        space[cap] = chr(i + ord('A'))
    with open(file, 'w') as f:
        for line in space:
            f.write(''.join(line.tolist())+'\n')

def part1(input):
    input = [parse(line) for line in input.strip().splitlines()]
    # visualize_capitals(input, 'sample_capitals.txt')
    space = create_space(input)
    space = scan_space(space, input)
    counts = np.arange(len(input))
    with np.nditer(counts, op_flags=['readwrite']) as it:
        print(it)
    # visualize(space, 'sample_field.txt')
    return

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 6
    input = inp.read(DAY)
    input = '''1, 1
        1, 6
        8, 3
        3, 4
        5, 5
        8, 9
        '''
    print(part1(input))
    print(part2(input))