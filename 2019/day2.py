from utils import IntcodeComputer

def part1(input):
    os = IntcodeComputer(input)
    os.noun_verb(noun=12, verb=2)
    return os.seq[0]


def part2(input):
    os = IntcodeComputer(input)
    target_val = 19690720
    noun, verb = os.scan(target_val)
    return 100 * noun + verb


if __name__ == '__main__':
    import aoc_input as inp

    DAY = 2

    sample = r'1,1,1,4,99,5,6,0,99'
    ic = IntcodeComputer(sample)
    ic.run()
    assert(r'30,1,1,4,2,5,6,0,99' == ','.join([str(i) for i in ic.seq]))
    # print(part1(r'2,4,4,5,99,02,4,4,5,99,0'))
    # ic = IntcodeComputer(inp.read(DAY))
    # ic.get_modes('1002')
    # ic.get_modes('11002')
    # ic.get_modes('00102')

    print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))

