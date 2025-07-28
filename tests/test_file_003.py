# Test file 3
import unittest

class TestFile3(unittest.TestCase):
    def test_feature_3(self):
        self.assertEqual(3 * 2, 6)

    def test_feature_3_squared(self):
        self.assertEqual(3 ** 2, 9)

if __name__ == '__main__':
    unittest.main()