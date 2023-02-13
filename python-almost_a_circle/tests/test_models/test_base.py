#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_id_argument(self):
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base(89)
        self.assertEqual(b1.id, 89)
        

if __name__ == '__main__':
    unittest.main()