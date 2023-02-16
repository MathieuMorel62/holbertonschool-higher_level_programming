import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Square class"""
        s = Square(5, 2, 3, 7)
        expected_output = {'id': 7, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(s.to_dictionary(), expected_output)

    def test_square_creation(self):
        """Test creation of a Square"""
        self.assertEqual(Square(1).size, 1)
        self.assertEqual(Square(1, 2).x, 2)
        self.assertEqual(Square(1, 2, 3).y, 3)

    def test_invalid_arguments(self):
        """Test invalid arguments"""
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_negative_size(self):
        """Test creation of a square with negative size"""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0, 10).size

    def test_str(self):
        """Test the str method of the Square class."""
        square = Square(4, 5, 6, 7)
        expected_output = '[Square] (7) 5/6 - 4'
        self.assertEqual(str(square), expected_output)

    def test_update(self):
        """Test update method in Square"""
        square = Square(10, 10, 10, 1)
        square.update(id=4)
        self.assertEqual(square.id, 4)