from . import Computer

class Arcade:
    def __init__(self, input):
        self.ic = Computer(input)

    def count_blocks(self):
        blocks = 0
        while self.ic.op != 99:
            self.ic.run(output_stop=3)
            if self.ic.op != 99:
                x = self.ic.outputs.pop(0)
                y = self.ic.outputs.pop(0)
                tile = self.ic.outputs.pop(0)

                if tile == 2:
                    blocks += 1
        return blocks
