class MemReallocator:
    def __init__(self, filename):
        self.banks = self.read_input(filename)
        self.record_hist()

    def read_input(self, filename):
        with open(filename, 'r') as file:
            return [int(s) for s in file.read().split('\t')]

    def cycle(self):
        index = self.banks.index(max(self.banks))
        amount = self.banks[index]

        self.banks[index] = 0
        index = self.rotate_index(index)

        while amount > 0:
            self.banks[index] += 1
            amount -= 1
            index = self.rotate_index(index)
        return self.record_hist()

    def rotate_index(self, index):
        index += 1
        if index == len(self.banks):
            index = 0
        return index

    def record_hist(self):
        new = '.'.join([str(b) for b in self.banks])
        if hasattr(self, 'hist'):
            if new in self.hist:
                self.hist.append(new)
                return False
            self.hist.append(new)
        else:
            self.hist = [new]
        return True

    def reallocate(self):
        while self.cycle():
            pass
        return len(set(self.hist))

    def loop(self):
        self.reallocate()
        start = self.hist[-1]
        print(start)
        self.cycle()
        i = 1
        while self.hist[-1] != start:
            self.cycle()
            i += 1
        return i


mr = MemReallocator('day6_input.txt')
# mr.banks = [0, 2, 7, 0]
print(mr.banks)
print(mr.reallocate())

mr = MemReallocator('day6_input.txt')
print(mr.banks)
print(mr.loop())