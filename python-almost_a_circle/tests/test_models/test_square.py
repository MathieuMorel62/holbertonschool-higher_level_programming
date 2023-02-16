import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Square class"""
        s = Square(5, 2, 3, 7)
        expected_output = {'id': 7, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(s.to_dictionary(), expected_output)
