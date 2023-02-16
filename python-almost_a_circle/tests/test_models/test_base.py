import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):

    def test_unique_id(self):
        """Test that a new instance of Base has a unique ID"""
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id, "ID should be unique")
