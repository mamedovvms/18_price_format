import unittest
from format_price import format_price


class TestPrice(unittest.TestCase):
    def test_no_fractional(self):
        self.assertEqual(format_price('3245.00000'), '3 245')
        self.assertEqual(format_price('3245'), '3 245')
        self.assertEqual(format_price('5'), '5')

    def test_from_fractional(self):
        self.assertEqual(format_price('123456.7890'), '123 456.79')
        self.assertEqual(format_price('12.889'), '12.89')
        self.assertEqual(format_price('12.999'), '13')

    def test_negative_value(self):
        self.assertEqual(format_price('-10000'), '-10 000')
        self.assertEqual(format_price('-111.789'), '-111.79')

    def test_incorrect_value(self):
        self.assertIsNone(format_price('Not price'))
        self.assertIsNone(format_price('10000,00'))
        self.assertIsNone(format_price('10000,12'))


if __name__ == '__main__':
    unittest.main()
