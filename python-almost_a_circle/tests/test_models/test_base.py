#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
   def test_instance(self):
        """ Test instantiation """

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(4)
        self.assertEqual(b2.id, 4)
        b3 = Base(3.5)
        self.assertEqual(b3.id, 3.5)
        b4 = Base(float('inf'))
        self.assertEqual(b4.id, float('inf'))
        b5 = Base("Holberton")
        self.assertEqual(b5.id, "Holberton")
        b6 = Base(["list", 2, 5.5])
        self.assertEqual(b6.id, ["list", 2, 5.5])
        b7 = Base(None)
        self.assertEqual(b7.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)
        

if __name__ == '__main__':
    unittest.main()