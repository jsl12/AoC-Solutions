def part1(input):
    return len(react(input))

def react(input):
    def check(i, res):
        if 97 <= ord(res[i]) <= 122:
            # lower case letter
            if res[i + 1] == res[i].upper():
                res = res[:i] + res[i + 2:]
                i -= 1
            else:
                i += 1
        elif 65 <= ord(res[i]) <= 90:
            # upper case letter
            if res[i + 1] == res[i].lower():
                res = res[:i] + res[i + 2:]
                i -= 1
            else:
                i += 1
        elif ord(res[i]) == 10:
            # newline
            i += 1
        else:
            print('Unrecognized char: {}'.format(input[i]))
        return i, res

    res = ''.join([line for line in input.splitlines()])
    i = 0

    while i < len(res) - 1:
        i, res = check(i, res)
    return res

def remove(input, lower_base):
    input = input.replace(lower_base, '')
    input = input.replace(lower_base.upper(), '')
    return input

def part2(input):
    res = []
    for i in range(ord('a'), ord('z') + 1):
        removed = remove(input, chr(i))
        res.append(len(react(removed)))
    return min(res)

if __name__ == '__main__':
    import input as inp
    DAY = 5
    input = inp.read(DAY)
    print(part1(input))
    print(part2(input))
