#!/usr/bin/python3
from .test_base import TestBase
from models.square import Square

class TestSquare(TestBase):
    @classmethod
    def setUpClass(cls, **kwargs):
        super().setUpClass(Square, **kwargs)
