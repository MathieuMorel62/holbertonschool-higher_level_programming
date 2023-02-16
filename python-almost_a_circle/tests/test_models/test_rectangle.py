import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base


class test_rectangle(unittest.TestCase):

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

    def test_area_exists(self):
        """Test that the area method exists"""
        self.assertEqual(Rectangle(4, 5).area(), 20)

    def test_str_output(self):
        """Test that str method returns the expected string representation"""
        r = Rectangle(3, 4, 2, 1, 10)
        expected_output = "[Rectangle] (10) 2/1 - 3/4"
        self.assertEqual(str(r), expected_output)

    def test_display_without_x_y(self):
        """
        Test that the display method outputs the correct
        representation of a rectangle
        """
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

    def test_display(self):
        """Test display exists"""
        r = Rectangle(2, 2, 2, 2)
        with StringIO() as buffer, redirect_stdout(buffer):
            r.display()
            self.assertEqual(buffer.getvalue(), "\n\n  ##\n  ##\n")
