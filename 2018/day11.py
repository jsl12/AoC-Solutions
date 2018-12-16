import numpy as np

def part1(input):
    serial_num = int(input)
    space = np.empty((300,300), dtype=np.int32)
    values = np.empty((space.shape[0]-3, space.shape[1]-3), dtype=np.int32)

    with np.nditer(space, flags=['multi_index'], op_flags=['readwrite']) as it:
        for cell in it:
            x = it.multi_index[0]
            y = it.multi_index[1]

            idx = x + 10
            power = (idx * y + serial_num) * idx
            power = int(power / 100) % 10
            space[x,y] = power - 5

    with np.nditer(space[:-3, :-3], flags=['multi_index'], op_flags=['readwrite']) as it:
        for cell in it:
            x = it.multi_index[0]
            y = it.multi_index[1]
            values[x,y] = space[sorted(list(range(y, y + 3)) * 3), list(range(x, x + 3)) * 3].sum()

    return np.unravel_index(values.argmax(), values.shape)[::-1]

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 11
    input = inp.read(DAY)
    print(part1(input))
    # print(part2(input))
    # print(part1('42'))