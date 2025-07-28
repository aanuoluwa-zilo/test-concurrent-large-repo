# Test file 1
import unittest

class TestFile1(unittest.TestCase):
    def test_feature_1(self):
        self.assertEqual(1 * 2, 2)

    def test_feature_1_squared(self):
        self.assertEqual(1 ** 2, 1)

if __name__ == '__main__':
    unittest.main()