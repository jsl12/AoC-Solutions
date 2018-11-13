from ast import literal_eval


class DataSteam:
    def read_input(self, filename):
        with open(filename, 'r') as file:
            self.input = file.read().rstrip()

    def scrub_cancels(self):
        # Scrubs cancelled characters
        while '!' in self.input:
            index = self.input.find('!')
            self.input = self.input[:index] + '  ' + self.input[index + 2:]

    def scrub_garbage(self):
        # Scrubs garbage
        while '<' in self.input:
            start = self.input.find('<')
            end = self.input.find('>', start)
            self.input = self.input[:start] + self.input[end + 1:]

    def scrub_commas(self):
        self.input = self.input.replace(',', '')

    def check(self):
        return self.input.count('{') == self.input.count('}')

class Group:
    def __init__(self, text):
        self.text = text

# ds = DataSteam('day9_input.txt', 100)
ds = DataSteam()
ds.read_input('day9_input.txt')
# ds.input = r'{{<a!>},{<a!>},{<a!>},{<ab>}}'
# ds.input = r'{{<!!>},{<!!>},{<!!>},{<!!>}}'
# ds.input = r'{{<ab>},{<ab>},{<ab>},{<ab>}}'
# ds.input = r'<{o"i!a,<{i<a>'
ds.scrub_cancels()
ds.scrub_garbage()
# ds.scrub_commas()
print(ds.check())
print(ds.input)
# print(ds.dict)