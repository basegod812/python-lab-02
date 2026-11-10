import unittest

from main import odd_sum, greatest_common_divisor, count_vowels
from euclid import euclidean_gcd


class TestLab(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(odd_sum(10), 25)
        self.assertEqual(odd_sum(0), 0)

    def test_gcd(self):
        self.assertEqual(greatest_common_divisor(48, 18), 6)
        self.assertEqual(euclidean_gcd(-48, 18), 6)

    def test_vowels(self):
        self.assertEqual(count_vowels("Привет"), 2)


if __name__ == "__main__":
    unittest.main()
