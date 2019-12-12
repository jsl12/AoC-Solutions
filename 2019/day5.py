from utils import IntcodeComputer


def part1(input):
    ic = IntcodeComputer(input)
    ic.inputs = [1]
    ic.run()
    return ic.outputs[-1]

def part2(input, initial=1):
    ic = IntcodeComputer(input)
    ic.inputs = [initial]
    ic.run()
    return ic.outputs[0]

if __name__ == '__main__':
    import aoc_input as inp

    DAY = 5
    # print(part1(inp.read(DAY)))
    assert(part2(r'3,9,8,9,10,9,4,9,99,-1,8', 8) == 1)
    assert (part2(r'3,9,8,9,10,9,4,9,99,-1,8', 7) == 0)
    assert(part2(r'3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 0) == 0)
    assert (part2(r'3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 1) == 1)
    assert (part2(r'3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 2) == 1)
    assert(part2(r'3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 0) == 0)
    assert (part2(r'3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 1) == 1)
    assert (part2(r'3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 2) == 1)
    res = part2(r'3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99').outputs
    print(part2(inp.read(DAY)))
