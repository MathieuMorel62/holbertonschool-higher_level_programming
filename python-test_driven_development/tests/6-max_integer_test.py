""" Unittest for max_integer([ ]) """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_int(self):
        """ Tests for a positive integers """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_float_list(self):
        """ Test for a float list """
        self.assertAlmostEqual(max_integer([1.0, 1.5, 1.9, 4.2, 2.8]), 4.2)

    def test_empty_list(self):
        """ Test for an empty list """
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        """ Test for a string """
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_negative_integers(self):
        """ Test for a negative integers """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_beginning(self):
        """ Test where the max element is at the beginning list """
        self.assertEqual(max_integer([5, 2, 3, 4]), 5)

    def test_middle(self):
        """ Test where the max element is at the middle list """
        self.assertEqual(max_integer([1, 5, 3]), 5)

    def test_diff_types(self):
        """ Test for a list containing elements of different types """
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'c'])

    def test_none(self):
        """ Test for a list containing None values """
        with self.assertRaises(TypeError):
            max_integer([1, 2, None])

    def test_single_element_list(self):
        """ Test for a single element list """
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-7]), -7)


if __name__ == '__main__':
    unittest.main()
