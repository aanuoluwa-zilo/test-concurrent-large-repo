# Test file 9
import unittest

class TestFile9(unittest.TestCase):
    def test_feature_9(self):
        self.assertEqual(9 * 2, 18)

    def test_feature_9_squared(self):
        self.assertEqual(9 ** 2, 81)

if __name__ == '__main__':
    unittest.main()