#!/usr/bin/python3
import unittest
import json
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.square = Square(3, 2, 3, 4)

    def test_inheritance(self):
        """ Test inheritance """
        self.assertIsInstance(self.square, Square)
        self.assertTrue(issubclass(type(self.square), Square))
        self.assertNotIsInstance(self.square, list)
        self.assertNotIsInstance(self.square, dict)

    def test_size(self):
        """ Test size property """
        self.assertEqual(self.square.size, 3)
        self.square.size = 10
        self.assertEqual(self.square.size, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.square.size = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.square.size = 1.5
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.square.size = "test"
