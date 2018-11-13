
def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        data.append([int(x) for x in line.strip().split('\t')])
    return data


def checksum(data):
    return sum([max(r) - min(r) for r in data])


def checksum2(data):
    sum = 0
    for row in data:
        row = sorted(row)[::-1]
        for i, r in enumerate(row):
            for x in row[-1:i + 1:-1]:
                if r % x == 0:
                    res = int(r / x)
                    sum += res
    return sum

if __name__ == '__main__':
    data = read_input('day2_input.txt')
    print(checksum(data))
    print(checksum2(data))
