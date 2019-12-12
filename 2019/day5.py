from utils import IntcodeComputer


def part1(input):
    ic = IntcodeComputer(input)
    ic.inputs = [1]
    ic.run()
    return ic.outputs[-1]

def part2(input):
    return

if __name__ == '__main__':
    import aoc_input as inp

    DAY = 5
    print(part1(inp.read(DAY)))
    # print(part2(inp.read(DAY)))
