import unittest
from format_price import format_price


class TestPrice(unittest.TestCase):
    def test_no_fractional(self):
        self.assertEqual(format_price('3245'), '3 245')

    def test_zero(self):
        self.assertEqual(format_price('0'), '0')

    def test_zero_fractional(self):
        self.assertEqual(format_price('3245.00000'), '3 245')

    def test_smal_value_no_fractional(self):
        self.assertEqual(format_price('5'), '5')

    def test_from_fractional(self):
        self.assertEqual(format_price('123456.7890'), '123 456.79')

    def test_smal_value_fractional(self):
        self.assertEqual(format_price('12.889'), '12.89')

    def test_round_result(self):
        self.assertEqual(format_price('12.999'), '13')

    def test_negative_value(self):
        self.assertEqual(format_price('-10000'), '-10 000')

    def test_negative_smal_value(self):
        self.assertEqual(format_price('-111.789'), '-111.79')

    def test_incorrect_value_not_number(self):
        self.assertIsNone(format_price('Not price'))

    def test_incorrect_value_separator(self):
        self.assertIsNone(format_price('10000,00'))

    def test_value_list(self):
        self.assertIsNone(format_price([1, 2, 3]))

    def test_value_set(self):
        self.assertIsNone(format_price(
            set('123')
        ))

    def test_value_dict(self):
        self.assertIsNone(format_price(
            {
                'price1': 100.0,
                'price2': '200'
            }
        ))

    def test_value_class(self):
        class MyClass(object):
            pass
        self.assertIsNone(format_price(MyClass()))

    def test_value_none(self):
        self.assertIsNone(format_price(None))

    def test_value_bool_true(self):
        self.assertIsNone(format_price(True))

    def test_value_bool_false(self):
        self.assertIsNone(format_price(False))

if __name__ == '__main__':
    unittest.main()
