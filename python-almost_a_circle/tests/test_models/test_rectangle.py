#!/usr/bin/python3

from .test_base import TestBase
from models.rectangle import Rectangle


class TestRectangle(TestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Rectangle, width=10, height=20)

    def test_width(self):
        self.assertEqual(self.obj.width, 10)

    def test_height(self):
        self.assertEqual(self.obj.height, 20)
