import unittest
from unit_testing.calc import *


class TestCalc(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(10,20),30)
        self.assertEqual(addition(-5,4),-1)
        self.assertIsNotNone(addition(56,4))
        self.assertEqual(addition("a","b"),"ab")
        self.assertEqual(addition(5.0,7.0),12.0)
        self.assertIsNone(addition())

    def test_subtraction(self):
        self.assertEqual(subtraction(10, 20), -10)
        self.assertEqual(subtraction(-5, 4), -9)
        self.assertEqual(subtraction(-5,-4), -1)
        self.assertIsNotNone(subtraction(56, 4))
        self.assertEqual(subtraction(5.0, 7.0), -2)
        self.assertIsNone(subtraction())

    def test_multiplication(self):
        self.assertEqual(multiplication(10, 20), 200)
        self.assertEqual(multiplication(-10, 20), -200)
        self.assertIsNotNone(subtraction(56, 4))
        self.assertRaises((AnythingMultipliedByZeroisZero,),multiplication,10,0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises((ZeroDivisionError,), divide, 10, 0)


if __name__ == '__main__':
    unittest.main()