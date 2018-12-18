import numpy as np
import re

REGEX = re.compile('(\d+), (\d+)')

def parse(line):
    match = REGEX.match(line.strip())
    assert match is not None
    return int(match.group(2)), int(match.group(1))

def create_space(input, value=0, offset=3):
    max_x = max([c[0] for c in input]) + offset
    max_y = max([c[1] for c in input]) + offset
    res = np.full((max_x, max_y), value, order='F')
    return res

def distance(coord, capital):
    x = abs(coord[0] - capital[0])
    y = abs(coord[1] - capital[1])
    return x + y

def scan_space(space, input):
    with np.nditer(space, flags=['multi_index'], op_flags=['readwrite'], order='F') as it:
        for cell in it:
            d = np.array([distance(it.multi_index, capital) for capital in input])
            if d[d == d.min()].size == 1:
                space[it.multi_index] = d.argmin()
            else:
                space[it.multi_index] = -1
    return space

def get_counts(space, inputs):
    counts = np.arange(len(inputs))
    with np.nditer(counts, op_flags=['readwrite'], order='F') as it:
        for x in it:
            counts[x] = len(space[space == x])
    return counts

def filter_borders(space, inputs):
    res = set()
    for i, row in enumerate(space):
        if i == 0 or i == space.shape[1]:
            res.update(row)
        else:
            res.update([row[0], row[-1]])
    filtered = [i for i in range(len(inputs))]
    [filtered.pop(i) for i in sorted(res)[-1:0:-1]]
    return filtered

def part1(input):
    input = [parse(line) for line in input.splitlines()]
    # visualize_capitals(input, 'sample_capitals.txt')
    space = create_space(input)
    space = scan_space(space, input)
    counts = get_counts(space, input)
    # visualize(space, 'sample_field.txt')
    valid_counts = [counts[i] for i in filter_borders(space, input)]
    return max(valid_counts)

def part2(input):
    input = [parse(line) for line in input.splitlines()]
    space = scan_space(create_space(input), input)
    return

def visualize(space, file):
    with open(file, 'w') as f:
        for row in space:
            row = [chr(int(x) + ord('A')) if int(x) >= 0 else '.' for x in row]
            f.write(''.join(row) + '\n')

def visualize_capitals(input, file):
    space = create_space(input, '.')
    for i, capital in enumerate(input):
        space[capital] = chr(i + ord('A'))
    with open(file, 'w') as f:
        for line in space:
            f.write(''.join(line.tolist())+'\n')

if __name__ == '__main__':
    import input as inp
    DAY = 6
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))
    #
    # sample_input = [
    #     (1, 1),
    #     (1, 6),
    #     (8, 3),
    #     (3, 4),
    #     (5, 5),
    #     (8, 9),
    # ]
    # sample_input = '\n'.join(['{}, {}'.format(cap[0], cap[1]) for cap in sample_input])
    # print(part1(sample_input))