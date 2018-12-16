import numpy as np

def part1(input):
    serial_num = int(input)
    space = np.empty((300,300), dtype=np.int32)
    assign_power(space, serial_num)
    values = max_square(space, 3)
    return get_max_idx(values)

def get_max_idx(values):
    return np.unravel_index(values.argmax(), values.shape)[::-1]

def assign_power(space, serial_num):
    with np.nditer(space, flags=['multi_index'], op_flags=['readwrite']) as it:
        for cell in it:
            x = it.multi_index[0]
            y = it.multi_index[1]

            idx = x + 10
            power = (idx * y + serial_num) * idx
            power = int(power / 100) % 10
            space[x,y] = power - 5

def max_square(space, size):
    values = np.empty((space.shape[0] - size, space.shape[1] - size), dtype=np.int32)
    with np.nditer(space[:-size, :-size], flags=['multi_index'], op_flags=['readwrite']) as it:
        for cell in it:
            x = it.multi_index[0]
            y = it.multi_index[1]
            values[x,y] = space[sorted(list(range(y, y + size)) * size), list(range(x, x + size)) * size].sum()
    return values

def part2(input):
    serial_num = int(input)
    space = np.empty((300, 300), dtype=np.int8)
    assign_power(space, serial_num)

    max_powers = np.arange(1, 300)
    with np.nditer(max_powers, flags=['f_index'], op_flags=['readwrite']) as it:
        for p in it:
            max_powers[it.index] = max_square(space, max_powers[it.index]).max()
    return

if __name__ == '__main__':
    import input as inp
    DAY = 11
    input = inp.read(DAY)
    print(part1(input))
    print(part2(input))
    # print(part1('42'))