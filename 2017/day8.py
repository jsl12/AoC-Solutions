import re


def read_input(filename):
    with open(filename, 'r') as file:
        return [line.rstrip() for line in file.readlines()]


class ProcRegister:
    def __init__(self, filename):
        self.input = read_input(filename)
        self.regs = {}
        self.max_history = []

    def get_value(self, reg):
        if reg not in self.regs:
            self.regs[reg] = 0
        return self.regs[reg]

    def proc_line(self, line):
        m = re.compile('([a-z]+) (inc|dec) ([-0-9]+) if ([a-z]+) ([!=<>]{1,2}) ([-0-9]+)').match(line)
        s = 'self.get_value(\'{}\') {} {}'.format(m.group(4), m.group(5), m.group(6))
        # print(s)
        if eval(s):
            if m.group(2) == 'inc':
                op = '+'
            elif m.group(2) == 'dec':
                op = '-'
            new_val = eval('{} {} {}'.format(self.get_value(m.group(1)), op, m.group(3)))
            # print(new_val)
            self.regs[m.group(1)] = new_val
        self.max_history.append(self.max_reg())

    def proc_all(self):
        for line in self.input:
            self.proc_line(line)

    def max_reg(self):
        return max(self.regs.values())

    def historic_max(self):
        return max(self.max_history)


if __name__ == '__main__':
    main()


def main():
    pr = ProcRegister('day8_input.txt')
    pr.proc_all()
    print(pr.max_reg())
    print(pr.historic_max())
