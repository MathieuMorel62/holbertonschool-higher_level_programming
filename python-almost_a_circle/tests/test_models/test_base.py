#!/usr/bin/python3

import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestsBase(unittest.TestCase):
    def test_base(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(89).id, 89)
        self.assertNotEqual(Base().id, 90)
        self.assertEqual(Base().id, 4)

    def test_id_incremental(self):
        self.assertEqual(Base().id, 5)
        self.assertEqual(Base().id, 6)

    def test_not_none(self):
        self.assertNotEqual(Base().id, None)
    
    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
    
    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])