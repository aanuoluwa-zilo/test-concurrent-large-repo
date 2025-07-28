# Test file 7
import unittest

class TestFile7(unittest.TestCase):
    def test_feature_7(self):
        self.assertEqual(7 * 2, 14)

    def test_feature_7_squared(self):
        self.assertEqual(7 ** 2, 49)

if __name__ == '__main__':
    unittest.main()