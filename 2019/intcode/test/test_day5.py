import unittest

from context import intcode

LONG_EXAMPLE = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,' \
            '1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,' \
            '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
CASES = {
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
            (LONG_EXAMPLE, 6): 999,
            (LONG_EXAMPLE, 7): 999,
            (LONG_EXAMPLE, 8): 1000,
            (LONG_EXAMPLE, 9): 1001,
            (LONG_EXAMPLE, 10): 1001,
        }


class TestDay5(unittest.TestCase):
    def test(self):
        with self.subTest():
            ic = intcode.Computer('1002,4,3,4,33')
            ic.run()
            seq = str(ic.seq).replace(' ', '')[1:-1]
            self.assertEqual(seq, '1002,4,3,4,99')

        for (input_seq, input_val), output in CASES.items():
            with self.subTest():
                ic = intcode.Computer(input_seq, input_val)
                res = ic.run()
                self.assertEqual(res, output, f'Failed sequence:\n{str(ic.ORIGINAL_SEQ)}\n{str(ic.seq)}\n{res} != {output}')


if __name__ == '__main__':
    unittest.main()
