digits = {
    3: 7,
    2: 1,
    4: 4,
    7: 8
}

def part1(inp):
    return sum(
        len(word) in digits
        for line in inp
        for word in line.split(' | ')[1].split()
    )

def classify():
    return