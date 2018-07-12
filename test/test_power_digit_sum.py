# coding=utf-8
from power_digit_sum import power_sum
import unittest


class TestCalculatePowerSum(unittest.TestCase):

    def test_power_digit_sum(self):
        summation = power_sum(4)
        self.assertEqual(7, summation)


if __name__ == '__main__':
    unittest.main()
