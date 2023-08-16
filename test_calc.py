# run with  python test_calc.py in terminal
import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):  # always start test with test_
        self.assertEqual(calc.add(1, 1), 2)  # two positive numbers
        self.assertEqual(calc.add(-1, 1), 0)  # negative and positive numbers
        self.assertEqual(calc.add(-1, -1), -2)  # two negative numbers

    def test_subtract(self):  # always start test with test_
        self.assertEqual(calc.subtract(1, 1), 0)  # two positive numbers
        self.assertEqual(calc.subtract(-1, 1), -2)  # negative and positive numbers
        self.assertEqual(calc.subtract(1, -1), 2)  # negative and positive numbers
        self.assertEqual(calc.subtract(-1, -1), 0)  # two negative numbers

    def test_multiply(self):  # always start test with test_
        self.assertEqual(calc.multiply(1, 2), 2)  # two positive numbers
        self.assertEqual(calc.multiply(-1, 2), -2)  # negative and positive numbers
        self.assertEqual(calc.multiply(-1, -2), 2)  # two negative numbers

    def test_divide(self):  # always start test with test_
        self.assertEqual(calc.divide(4, 2), 2)  # two positive numbers
        self.assertEqual(calc.divide(-4, 2), -2)  # negative and positive numbers
        self.assertEqual(calc.divide(-4, -2), 2)  # two negative numbers
        self.assertEqual(calc.divide(5, 2), 2.5)  # not integer
        with self.assertRaises(ValueError):  # catch divided by 0
            calc.divide(10, 0)

    # try a failed test
    def test_failedadd(self):
        self.assertEqual(calc.add(10, 5), 14)


if __name__ == '__main__':
    unittest.main()
