#!/usr/bin/python3

from .test_base import TestBase
from models.base import Base
from models.rectangle import Rectangle
import os
import json


class TestRectangle(TestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Rectangle)

    def test_area(self):
        """ Test the area method of the Rectangle """
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """ Test the __str__ method of the Rectangle """
        r = Rectangle(2, 3, 1, 1, 10)
        self.assertEqual(r.__str__(), "[Rectangle] (10) 1/1 - 2/3")

    def test_update(self):
        """ Test the update method of the Rectangle """
        r = Rectangle(2, 3, 1, 1, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_to_dictionary(self):
        """ Test the to_dictionary method of the Rectangle """
        r = Rectangle(2, 3, 1, 1, 10)
        expected_dict = {'id': 10, 'width': 2, 'height': 3, 'x': 1, 'y': 1}
        self.assertDictEqual(r.to_dictionary(), expected_dict)

    def test_args_validator(self):
        """ Test the args validator of the Rectangle """
        with self.assertRaises(ValueError):
            Rectangle(0, 3, 1, 1, 10)
        with self.assertRaises(ValueError):
            Rectangle(2, 0, 1, 1, 10)
        with self.assertRaises(ValueError):
            Rectangle(2, 3, -1, 1, 10)
        with self.assertRaises(ValueError):
            Rectangle(2, 3, 1, -1, 10)
