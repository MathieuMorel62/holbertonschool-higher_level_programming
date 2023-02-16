import unittest
from models.base import Base


class test_base(unittest.TestCase):

    def test_unique_id(self):
        """Test that a new instance of Base has a unique ID"""
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id, "ID should be unique")

    def test_automatic_id(self):
        """Test that an ID is correctly assigned to a new instance of Base"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_passed_id(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_to_json_string(self):
        """Test to_json_string method with None argument"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_from_json_string_list_empty(self):
        """ Test from_json_string returns an empty list """
        self.assertTrue(hasattr(Base, 'from_json_string'))
        self.assertEqual(Base.from_json_string("[]"), [])

if __name__ == '__main__':
    unittest.main()
