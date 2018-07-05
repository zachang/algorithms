# coding=utf-8
from power_digit_sum import power_sum
import unittest


class TestCalculatePowerSum(unittest.TestCase):

    def test_power_digit_sum(self):
        first_result = power_sum(1000)
        second_result = power_sum(1000)
        self.assertEqual(first_result, second_result)


if __name__ == '__main__':
    unittest.main()
