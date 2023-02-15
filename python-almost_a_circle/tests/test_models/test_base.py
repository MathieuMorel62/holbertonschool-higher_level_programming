#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
   @classmethod
   def setUpClass(cls, class_name=Base, **kwargs):
        cls._class_name = class_name
        cls._class_kwargs = kwargs
        cls.init_id = cls._class_name(**cls._class_kwargs).id

   def test_instance(self):
        """ Test instantiation """
        first_obj = self._class_name(**self._class_kwargs)
        second_obj = self._class_name(**self._class_kwargs)
        third_obj = self._class_name(89, **self._class_kwargs)
        fourth_obj = self._class_name(56, **self._class_kwargs)
        fifth_obj = self._class_name('a', **self._class_kwargs)

        self.assertEqual(first_obj.id, self.init_id + 1)
        self.assertEqual(second_obj.id, first_obj.id + 1)
        self.assertEqual(third_obj.id, 89)
        self.assertEqual(fourth_obj.id, 56)
        self.assertEqual(fifth_obj.id, 'a')    

if __name__ == '__main__':
    unittest.main()