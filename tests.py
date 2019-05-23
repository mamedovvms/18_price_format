import unittest
from format_price import format_price


class TestPrice(unittest.TestCase):
    def test_no_fractional(self):
        self.assertEqual(format_price('3245.000000'), '3 245')

    def test_from_fractional(self):
        self.assertEqual(format_price('123456.7890'), '123 456,789')

    def test_incorrect_value(self):
        self.assertIsNone(format_price('Not price'))
        self.assertIsNone(format_price('-10'))


if __name__ == '__main__':
    unittest.main()
