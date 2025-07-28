# Test file 8
import unittest

class TestFile8(unittest.TestCase):
    def test_feature_8(self):
        self.assertEqual(8 * 2, 16)

    def test_feature_8_squared(self):
        self.assertEqual(8 ** 2, 64)

if __name__ == '__main__':
    unittest.main()