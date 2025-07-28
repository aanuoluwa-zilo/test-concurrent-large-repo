# Test file 13
import unittest

class TestFile13(unittest.TestCase):
    def test_feature_13(self):
        self.assertEqual(13 * 2, 26)

    def test_feature_13_squared(self):
        self.assertEqual(13 ** 2, 169)

if __name__ == '__main__':
    unittest.main()