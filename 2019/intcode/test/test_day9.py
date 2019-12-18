import unittest

from context import intcode

CASES = {
            '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99': '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99',
            '1102,34915192,34915192,7,4,7,99,0': 1219070632396864,
            '104,1125899906842624,99': 1125899906842624,
}


class TestDay9(unittest.TestCase):
    def test(self):
        input_seq = list(CASES.keys())[0]
        output = CASES.pop(input_seq)
        ic = intcode.Computer(input_seq)
        ic.run()
        with self.subTest():
            self.assertEqual(output, ','.join([str(i) for i in ic.outputs]))

        for input_seq, output in CASES.items():
            with self.subTest():
                ic = intcode.Computer(input_seq)
                res = ic.run()
                self.assertEqual(res, output, f'Failed sequence:\n{str(ic.ORIGINAL_SEQ)}\n{str(ic.seq)}\n{res} != {output}')

        ic = intcode.Computer('109,5,203,0,104,0,99', [69])
        res = ic.run()
        with self.subTest():
            self.assertEqual(res, 69)


if __name__ == '__main__':
    unittest.main()
