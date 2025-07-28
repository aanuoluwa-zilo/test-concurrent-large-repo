# Test file 11
import unittest

class TestFile11(unittest.TestCase):
    def test_feature_11(self):
        self.assertEqual(11 * 2, 22)

    def test_feature_11_squared(self):
        self.assertEqual(11 ** 2, 121)

if __name__ == '__main__':
    unittest.main()