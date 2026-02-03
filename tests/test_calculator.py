import unittest
from src.calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):
   def test_add(self):
       self.assertEqual(add(2, 3), 5)
       self.assertEqual(add(-1, 1), 0)
       self.assertEqual(add(-1, -1), -2)

   def test_subtract(self):
       self.assertEqual(subtract(10, 3), 7)
       self.assertEqual(subtract(-1, 1), -2)
       self.assertEqual(subtract(-5, -2), -3)

   def test_divide(self):
       self.assertEqual(divide(10, 2), 5)
       self.assertEqual(divide(-9, 3), -3)
       self.assertAlmostEqual(divide(1, 3), 1/3)

if __name__ == '__main__':
   unittest.main()
