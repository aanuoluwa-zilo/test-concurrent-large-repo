# Test file 14
import unittest

class TestFile14(unittest.TestCase):
    def test_feature_14(self):
        self.assertEqual(14 * 2, 28)

    def test_feature_14_squared(self):
        self.assertEqual(14 ** 2, 196)

if __name__ == '__main__':
    unittest.main()