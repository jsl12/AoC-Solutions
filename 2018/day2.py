def part1(input):
    twos = 0
    threes = 0

    for line in input.splitlines():
        letters = {}
        for c in line:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        if [letters[c] for c in letters if letters[c] == 2]:
            twos += 1
        if [letters[c] for c in letters if letters[c] == 3]:
            threes += 1

    checksum = twos * threes
    return checksum

def part2(input):
    input = input.splitlines()

    for word1 in input:
        for word2 in input:
            if compare(word1, word2):
                return solution(word1, word2)

def compare(a, b):
    res = 0
    for i, c in enumerate(a):
        if c != b[i]:
           res += 1
        if res > 1:
            return False
    if res == 1:
        return True

def solution(a, b):
    res = ''
    for i, c in enumerate(a):
        if c == b[i]:
            res += c
    return res

if __name__ == '__main__':
    import input as inp
    DAY = 2
    input = inp.read(DAY)
    print(part1(input))
    print(part2(input))