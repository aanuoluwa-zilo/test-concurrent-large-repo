# Test file 2
import unittest

class TestFile2(unittest.TestCase):
    def test_feature_2(self):
        self.assertEqual(2 * 2, 4)

    def test_feature_2_squared(self):
        self.assertEqual(2 ** 2, 4)

if __name__ == '__main__':
    unittest.main()