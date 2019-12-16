import unittest

from day10 import Asteroid, Field
from day12 import PlanetSystem
from intcode import Computer, AmpSystem


DAY2 = {
            '1,0,0,0,99': '2,0,0,0,99',
            '2,3,0,3,99': '2,3,0,6,99',
            '2,4,4,5,99,0': '2,4,4,5,99,9801',
            '1,1,1,4,99,5,6,0,99': '30,1,1,4,2,5,6,0,99'
        }
long_example = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,' \
            '1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,' \
            '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
DAY5 = {
            # equal to 8, position mode
            ('3,9,8,9,10,9,4,9,99,-1,8', 8): 1,
            ('3,9,8,9,10,9,4,9,99,-1,8', 7): 0,
            # less than 8, position mode
            ('3,9,7,9,10,9,4,9,99,-1,8', 8): 0,
            ('3,9,7,9,10,9,4,9,99,-1,8', 7): 1,
            # equal to 8, immediate mode
            ('3,3,1108,-1,8,3,4,3,99', 8): 1,
            ('3,3,1108,-1,8,3,4,3,99', 7): 0,
            # less than 8, immediate mode
            ('3,3,1107,-1,8,3,4,3,99', 8): 0,
            ('3,3,1107,-1,8,3,4,3,99', 7): 1,
            # non-zero check, position mode
            ('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 0): 0,
            ('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 2): 1,
            # non-zero check, immediate mode
            ('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 0): 0,
            ('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 2): 1,
            (long_example, 6): 999,
            (long_example, 7): 999,
            (long_example, 8): 1000,
            (long_example, 9): 1001,
            (long_example, 10): 1001,
        }
DAY7_PART1 = {
            ('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0', '4,3,2,1,0'): 43210,
            ('3,23,3,24,1002,24,10,24,1002,23,-1,23,'
            '101,5,23,23,1,24,23,23,4,23,99,0,0', '0,1,2,3,4'): 54321,
            ('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,'
            '1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0', '1,0,4,3,2'): 65210
        }
DAY7_PART2 = {
            ('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,'
            '27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5', '9,8,7,6,5'): 139629729,
            ('3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,'
            '-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,'
            '53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10', '9,7,8,5,6'): 18216
        }
DAY9_PART1 = {
            '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99': '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99',
            '1102,34915192,34915192,7,4,7,99,0': 1219070632396864,
            '104,1125899906842624,99': 1125899906842624,
        }
DAY12_PART1 = '<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>'


class PlanetTest(unittest.TestCase):
    def test_gravity(self):
        ps = PlanetSystem(DAY12_PART1)
        for i in range(3):
            ps.simulate_dimension(i, 10)
        self.assertEqual(ps.total_energy, 179)

    def test_cycle(self):
        ps = PlanetSystem(DAY12_PART1)
        total = ps.total_cycle_time()
        self.assertEqual(total, 2772)


class AmpSystemTest(unittest.TestCase):
    def test_day7_part1(self):

        # test just running and getting the right answer
        for (input_seq, settings), signal in DAY7_PART1.items():
            sys = AmpSystem(input_seq)
            settings = [int(i) for i in settings.split(',')]
            res = sys.run(settings)
            self.assertEqual(res, signal, f'{input_seq}\n{settings}\n{res} != {signal}')

        # test to make sure it arrives at that answer as the max separately
        for (input_seq, settings), signal in DAY7_PART1.items():
            sys = AmpSystem(input_seq)
            res = sys.max_thruster_signal([i for i in range(5)])
            self.assertEqual(res, signal, f'{input_seq}\n{settings}\n{res} != {signal}')

    def test_day7_part2(self):
        # test just running and getting the right answer
        for (input_seq, settings), signal in DAY7_PART2.items():
            sys = AmpSystem(input_seq)
            settings = [int(i) for i in settings.split(',')]
            res = sys.run(settings)
            self.assertEqual(res, signal, f'{input_seq}\n{settings}\n{res} != {signal}')

        # test to make sure it arrives at that answer as the max separately
        for (input_seq, settings), signal in DAY7_PART2.items():
            sys = AmpSystem(input_seq)
            settings = [int(i) for i in settings.split(',')]
            res = sys.max_thruster_signal([i for i in range(5, 10)])
            self.assertEqual(res, signal, f'{input_seq}\n{settings}\n{res} != {signal}')


class IntcodeComputerTest(unittest.TestCase):
    def test_day2(self):
        for input, output in DAY2.items():
            ic = Computer(input)
            ic.run()
            self.assertEqual(str(ic.seq).replace(' ', '')[1:-1], output)

    def test_day5(self):
        ic = Computer('1002,4,3,4,33')
        ic.run()
        self.assertEqual(str(ic.seq).replace(' ', '')[1:-1], '1002,4,3,4,99')

        for (input_seq, input_val), output in DAY5.items():
            ic = Computer(input_seq)
            ic.inputs.append(input_val)
            res = ic.run()
            self.assertEqual(res, output, f'Failed sequence:\n{str(ic.ORIGINAL_SEQ)}\n{str(ic.seq)}\n{res} != {output}')

    def test_day9(self):
        input_seq = list(DAY9_PART1.keys())[0]
        output = DAY9_PART1.pop(input_seq)
        ic = Computer(input_seq)
        ic.run()
        self.assertEqual(output, ','.join([str(i) for i in ic.outputs]))

        for input_seq, output in DAY9_PART1.items():
            ic = Computer(input_seq)
            res = ic.run()
            self.assertEqual(res, output, f'Failed sequence:\n{str(ic.ORIGINAL_SEQ)}\n{str(ic.seq)}\n{res} != {output}')

        ic = Computer('109,5,203,0,104,0,99', [69])
        res = ic.run()
        self.assertEqual(res, 69)

class test_day10(unittest.TestCase):
    def test_samples(self):
        field = '.#..#\n.....\n#####\n....#\n...##'
        f = Field(field)
        base, visible_ast_count = f.max_visible()
        self.assertEqual(visible_ast_count, 8)

    def test_angles(self):
        base = (1,1)
        self.assertEqual(Asteroid((0, 2)).angle(*base), 45)
        self.assertEqual(Asteroid((2, 2)).angle(*base), 135)
        self.assertEqual(Asteroid((2, 0)).angle(*base), 225)
        self.assertEqual(Asteroid((0, 0)).angle(*base), 315)


if __name__ == '__main__':
    unittest.main()
