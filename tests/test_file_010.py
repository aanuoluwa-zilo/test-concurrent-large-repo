# Test file 10
import unittest

class TestFile10(unittest.TestCase):
    def test_feature_10(self):
        self.assertEqual(10 * 2, 20)

    def test_feature_10_squared(self):
        self.assertEqual(10 ** 2, 100)

if __name__ == '__main__':
    unittest.main()