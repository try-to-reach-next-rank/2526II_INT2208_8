import unittest
from app.triangle import classify_triangle
class TestTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')
        self.assertEqual(classify_triangle(100, 100, 100), 'Equilateral')
        self.assertEqual(classify_triangle(50, 50, 50), 'Equilateral')

    def test_isosceles(self):
        self.assertEqual(classify_triangle(2, 2, 3), 'Isosceles')
        self.assertEqual(classify_triangle(4, 5, 5), 'Isosceles')
        self.assertEqual(classify_triangle(50, 50, 75), 'Isosceles')
        self.assertEqual(classify_triangle(100, 99, 99), 'Isosceles')
        self.assertEqual(classify_triangle(90.5, 90.5, 99), 'Isosceles')

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Scalene')
        self.assertEqual(classify_triangle(99, 100, 98), 'Scalene')
        self.assertEqual(classify_triangle(50.5, 60.5, 70.5), 'Scalene')

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'Not a triangle')
        self.assertEqual(classify_triangle(1, 10, 12), 'Not a triangle')
        self.assertEqual(classify_triangle(100, 10, 1), 'Not a triangle')
        self.assertEqual(classify_triangle(5, 1.5, 1.5), 'Not a triangle')

    def test_invalid_input(self):
        self.assertEqual(classify_triangle(-1, 2, 3), 'Invalid input')
        self.assertEqual(classify_triangle(1, -2, 3), 'Invalid input')
        self.assertEqual(classify_triangle(1, 2, -3), 'Invalid input')
        self.assertEqual(classify_triangle(0, 2, 3), 'Invalid input')
        self.assertEqual(classify_triangle(1, 0, 3), 'Invalid input')
        self.assertEqual(classify_triangle(1, 2, 0), 'Invalid input')
        self.assertEqual(classify_triangle('a', 2, 3), 'Invalid input')
        self.assertEqual(classify_triangle(1, 'b', 3), 'Invalid input')
        self.assertEqual(classify_triangle(1, 2, 'c'), 'Invalid input')

if __name__ == "__main__":
    unittest.main()