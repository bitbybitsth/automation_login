import unittest
from unit_testing.calc import *


class TestCalc(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(10, 20), 30)
        self.assertNotEqual(addition(5, 6), 9)
        self.assertIsNotNone(addition(10, 20))
        # self.assertIsNone(addition(10,20))

    def test_subtration(self):
        self.assertEqual(subtraction(20, 10),10)
        self.assertNotEqual(subtraction(7, 8), 20)
        self.assertIsNotNone(addition(2, 3))

    def test_multiplication(self):
        self.assertEqual(multiplication(10,20),200)
        self.assertIsNotNone(multiplication(3,4))
        self.assertNotEqual(multiplication(2,3), 20000)
        # self.assertRaises((ZeroDivisionError,),multiplication,10,0)
        self.assertRaises((AnythingMultipliedByZeroisZero,), multiplication,10,0)


    def test_divide(self):
        self.assertEqual(divide(10,2), 5)
        self.assertNotEqual(divide(8,2), 6)
        self.assertIsNotNone(divide(18,3))
        self.assertRaises((ZeroDivisionError,),divide,10,0)



if __name__ == '__main__':
    unittest.main()