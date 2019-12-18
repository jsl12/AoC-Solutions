import unittest

from context import intcode

CASES = {
            '1,0,0,0,99': '2,0,0,0,99',
            '2,3,0,3,99': '2,3,0,6,99',
            '2,4,4,5,99,0': '2,4,4,5,99,9801',
            '1,1,1,4,99,5,6,0,99': '30,1,1,4,2,5,6,0,99'
        }


class TestDay2(unittest.TestCase):
    def test(self):
        for input, output in CASES.items():
            ic = intcode.Computer(input)
            ic.run()
            seq = str(ic.seq).replace(' ', '')[1:-1]
            with self.subTest(failed_seq=seq):
                self.assertEqual(seq, output)


if __name__ == '__main__':
    unittest.main()
