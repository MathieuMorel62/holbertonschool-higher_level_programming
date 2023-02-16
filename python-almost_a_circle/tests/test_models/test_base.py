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

    def test_automatic_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_passed_id(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

if __name__ == '__main__':
    unittest.main()
