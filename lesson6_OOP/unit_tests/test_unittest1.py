from unittest import TestCase

from lesson6_OOP.unit_tests.unittest1 import Calculator


class TestCalculator(TestCase):
    def test_add(self):
         calc = Calculator()
         self.assertEqual(calc.add(2, 3), 4)

    # def is_even(self,n):
    #     return n % 2 == 0
    #     self.assertEqual(is_even(4), True)
def divide(a,b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b