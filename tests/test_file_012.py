# Test file 12
import unittest

class TestFile12(unittest.TestCase):
    def test_feature_12(self):
        self.assertEqual(12 * 2, 24)

    def test_feature_12_squared(self):
        self.assertEqual(12 ** 2, 144)

if __name__ == '__main__':
    unittest.main()