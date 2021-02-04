# test the calculator
import unittest
import calculator

# The following tests use the unittest framework
class testCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.addition(10, 1), 11)
        self.assertEqual(calculator.addition(-10, 1), -9)
        self.assertEqual(calculator.addition(0, 1), 1)
        self.assertEqual(calculator.addition(-1, 1), 0)
        self.assertEqual(calculator.addition(1.5, 1), 2.5)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(10, 1), 9)
        self.assertEqual(calculator.subtraction(-10, 1), -11)
        self.assertEqual(calculator.subtraction(0, 1), -1)
        self.assertEqual(calculator.subtraction(-1, 1), -2)
        self.assertEqual(calculator.subtraction(1.5, 1), 0.5)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(10, 1), 10)
        self.assertEqual(calculator.multiplication(-10, 1), -10)
        self.assertEqual(calculator.multiplication(0, 1), 0)
        self.assertEqual(calculator.multiplication(-1, 1), -1)
        self.assertEqual(calculator.multiplication(1.5, 1), 1.5)
        self.assertEqual(calculator.multiplication(.5, .5), .25)

    def test_division(self):
        self.assertEqual(calculator.division(10, 1), 10)
        self.assertEqual(calculator.division(-10, 1), -10)
        self.assertEqual(calculator.division(0, 1), 0)
        self.assertRaises(ZeroDivisionError, calculator.division, 1, 0)
        self.assertEqual(calculator.division(1.5, 1), 1.5)
        self.assertEqual(calculator.division(3, 2), 1.5)

if __name__ == '__main__':
    unittest.main(verbosity=2)