import unittest

from context import intcode

CASES_PART1 = {
            ('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0', '4,3,2,1,0'): 43210,
            ('3,23,3,24,1002,24,10,24,1002,23,-1,23,'
            '101,5,23,23,1,24,23,23,4,23,99,0,0', '0,1,2,3,4'): 54321,
            ('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,'
            '1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0', '1,0,4,3,2'): 65210
        }
CASES_PART2 = {
            ('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,'
            '27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5', '9,8,7,6,5'): 139629729,
            ('3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,'
            '-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,'
            '53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10', '9,7,8,5,6'): 18216
        }


class TestDay7(unittest.TestCase):
    def test_part1(self):
        # test just running and getting the right answer
        for (input_seq, settings), signal in CASES_PART1.items():
            with self.subTest():
                sys = intcode.AmpSystem(input_seq)
                settings = [int(i) for i in settings.split(',')]
                res = sys.run(settings)
                self.assertEqual(res, signal, f'{input_seq}\n{settings}\n{res} != {signal}')

        # test to make sure it arrives at that answer as the max separately
        for (input_seq, settings), signal in CASES_PART1.items():
            with self.subTest():
                sys = intcode.AmpSystem(input_seq)
                res = sys.max_thruster_signal([i for i in range(5)])
                self.assertEqual(res, signal, f'{input_seq}\n{settings}\n{res} != {signal}')

    def test_part2(self):
        # test just running and getting the right answer
        for (input_seq, settings), signal in CASES_PART2.items():
            with self.subTest():
                sys = intcode.AmpSystem(input_seq)
                settings = [int(i) for i in settings.split(',')]
                res = sys.run(settings)
                self.assertEqual(res, signal, f'{input_seq}\n{settings}\n{res} != {signal}')

        # test to make sure it arrives at that answer as the max separately
        for (input_seq, settings), signal in CASES_PART2.items():
            with self.subTest():
                sys = intcode.AmpSystem(input_seq)
                settings = [int(i) for i in settings.split(',')]
                res = sys.max_thruster_signal([i for i in range(5, 10)])
                self.assertEqual(res, signal, f'{input_seq}\n{settings}\n{res} != {signal}')


if __name__ == '__main__':
    unittest.main()
