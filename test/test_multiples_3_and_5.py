# coding=utf-8
import unittest
from largest_prime_factor import largest_prime_factor, is_factor


class TestLargestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor(self):
        prime_factors = largest_prime_factor(is_factor, 15000)
        expected_value = prime_factors.get('max_prime_factor')
        self.assertEqual(expected_value, prime_factors.get('max_prime_factor'))
        self.assertIn(5, prime_factors.get('prime_factors'))


if __name__ == '__main__':
    unittest.main()