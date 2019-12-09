from utils import IntcodeComputer

def part1(input):
    os = IntcodeComputer(input)
    os.run_program(noun=12, verb=2)
    return os.seq[0]


def part2(input):
    os = IntcodeComputer(input)
    target_val = 19690720
    noun, verb = os.scan(target_val)
    return 100 * noun + verb


if __name__ == '__main__':
    import aoc_input as inp

    DAY = 2
    print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
