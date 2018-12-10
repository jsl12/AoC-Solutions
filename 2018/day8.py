import numpy as np

def part1(input):
    input = np.array([int(i) for i in input.split(' ')], dtype=np.uint8)

    def sum_node(iterator):
        # assumes start of node
        nonlocal input
        count_child = input[iterator.iterindex]
        count_md = input[iterator.iterindex+1]
        total = 0

        iterator.iterindex += 2
        if count_child > 0:
            for i in range(count_child):
                total += sum_node(iterator)
        total += sum_metadata(iterator, count_md)
        return total

    def sum_metadata(iterator, count):
        # assumes start of metadata
        nonlocal input
        start = iterator.iterindex
        end = start + count
        if iterator.itersize > end:
            iterator.iterindex = end
        else:
            while not iterator.finished:
                iterator.iternext()
        return sum(input[start:end])

    with np.nditer(input, op_flags=['readonly'], flags=['f_index']) as it:
        while not it.finished:
            total = sum_node(it)
    return total

def part2(input):
    return

if __name__ == '__main__':
    import input as inp
    DAY = 8
    input = inp.read(DAY)
    # input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    print(part1(input))
    # print(part2(input))