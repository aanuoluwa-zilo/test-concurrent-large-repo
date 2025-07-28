# Test file 6
import unittest

class TestFile6(unittest.TestCase):
    def test_feature_6(self):
        self.assertEqual(6 * 2, 12)

    def test_feature_6_squared(self):
        self.assertEqual(6 ** 2, 36)

if __name__ == '__main__':
    unittest.main()