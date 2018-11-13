class CPUTramp:
    def __init__(self, filename):
        self.input = self.read_input(filename)
        self.i = 0
        self.step_count = 0

    def read_input(self, filename):
        with open(filename, 'r') as file:
            return [int(s) for s in file.readlines()]

    def move(self):
        if not self.i >= len(self.input):
            self.step_count += 1
            start = self.i
            self.i += self.input[self.i]
            self.shift(start)
            # print(self.input, start, self.i)
            return True
        return False

    def shift(self, index):
        self.input[index] += 1

    def escape(self):
        try:
            i = 0
            while self.move():
                i += 1
                # if i >= 2000000:
                #     break
        except:
            print('Error')
            print(self.i, len(self.input))
        return self.step_count


class CPUTramp2(CPUTramp):
    def shift(self, index):
        if self.input[index] >= 3:
            self.input[index] -= 1
        else:
            self.input[index] += 1

# ct = CPUTramp('day5_input.txt')
# print(ct.escape())

ct = CPUTramp2('day5_input.txt')
# ct.input = [0, 3, 0, 1, -3]
# ct.input = ct.input[:10]
print(ct.escape())
print(ct.input)