#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
   def test_instance(self):
        """ Test instantiation """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 4)
        self.assertEqual(Base().id, 3.5)
        self.assertEqual(Base().id, "Holberton")
        self.assertEqual(Base().id, ["list", 2, 5.5])
        self.assertEqual(Base(89).id, 89)
        self.assertNotEqual(Base().id, 20)

if __name__ == '__main__':
    unittest.main()