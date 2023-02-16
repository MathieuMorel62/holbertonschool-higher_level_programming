import unittest
from models.rectangle import Rectangle
from models.base import Base
from .test_base import TestBase



class testRectangle(TestBase):

    def test_rectangle_instance(self):
        """Test if rectangle instance is created successfully"""
        rect = Rectangle(1, 2)
        self.assertIsInstance(rect, Base)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, rect._Base__nb_objects)

    def test_rectangle_str_width(self):
        """Test that passing a string as width raises a TypeError"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5)

    def test_Rectangle_negative_or_zero_args(self):
        """
        Test if creating Rectangle instance with negative
        or zero args raises ValueError
        """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)


if __name__ == '__main__':
    unittest.main()
