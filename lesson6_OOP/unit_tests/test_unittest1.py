from unittest import TestCase

from lesson6_OOP.unit_tests.unittest1 import Calculator


class TestCalculator(TestCase):
    def test_add(self):
         calc = Calculator()
         self.assertEqual(calc.add(2, 3), 4)
