def part1(input):
    res = input
    i = 0

    def check():
        nonlocal res
        nonlocal i
        if 97 <= ord(res[i]) <= 122:
            # lower case letter
            if res[i + 1] == res[i].upper():
                res = res[:i] + res[i+2:]
                i -= 1
            else:
                i += 1
        elif 65 <= ord(res[i]) <= 90:
            # upper case letter
            if res[i + 1] == res[i].lower():
                res = res[:i] + res[i+2:]
                i -= 1
            else:
                i += 1
        elif ord(res[i]) == 10:
            # newline
            i += 1
        else:
            print('Unrecognized char: {}'.format(input[i]))

    while i < len(res) - 1:
        check()

    with open('res.txt', 'w') as file:
        file.write(res)
    return len(res)

def part2(input):
    return

if __name__ == '__main__':
    from pathlib import Path
    p = Path(r'C:\Users\lanca_000\Documents\Software\Python\AoC Benchmark\AoC-Inputs\2018')
    with open(p / 'day5.txt', 'r') as file:
        input = file.read()
        print(part1(input[:100]))

    # input = 'dabAcCaCBAcCcaDA'
    print(part1(input))

    # print(part2(input))