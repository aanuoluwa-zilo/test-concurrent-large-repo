# Test file 4
import unittest

class TestFile4(unittest.TestCase):
    def test_feature_4(self):
        self.assertEqual(4 * 2, 8)

    def test_feature_4_squared(self):
        self.assertEqual(4 ** 2, 16)

if __name__ == '__main__':
    unittest.main()