import unittest
import os
import json
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
        """Test rectangle display exists"""
        r = Rectangle(2, 2, 2, 2)
        with StringIO() as buffer, redirect_stdout(buffer):
            r.display()
            self.assertEqual(buffer.getvalue(), "\n\n  ##\n  ##\n")

    def test_to_dictionary(self):
        """Test Rectangle to_dictionary"""
        r = Rectangle(2, 5, 4, 1, 7)
        expected_output = {'id': 7, 'width': 2, 'height': 5, 'x': 4, 'y': 1}
        self.assertDictEqual(r.to_dictionary(), expected_output)

    def test_update(self):
        """ Test update method with arbitrary number of arguments """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (1) 4/5 - 2/3")

    def test_update_args_1(self):
        """ Test update method with one argument """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_args_2(self):
        """ Test update method with two arguments """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_args_3(self):
        """ Test update method with three arguments """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_args_4(self):
        """ Test update method with four arguments """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_args_5(self):
        """ Test update method with five arguments """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_create(self):
        """Test Rectangle.create() method"""
        rect = Rectangle(10, 9, 8, 7, 6)
        rect_dictionary = rect.to_dictionary()
        second_rect = Rectangle.create(**rect_dictionary)
        self.assertEqual(second_rect.id, 6)

    def test_save_to_file_None(self):
        """Test Rectangle save_to_file method with None as argument"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty_list(self):
        """Test Rectangle save_to_file method with empty list as argument"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file(self):
        """Test save_to_file method with a list of Rectangle instances"""
        rect1 = Rectangle(1, 1, 1, 1, 1)
        rect2 = Rectangle(2, 2, 2, 2, 2)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            ls = [rect1.to_dictionary(), rect2.to_dictionary()]
            self.assertEqual(json.dumps(ls), file.read())

    def test_load_from_file_no_file(self):
        """Test Rectangle load_from_file method when file doesn't exist"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])
