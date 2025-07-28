# Test file 5
import unittest

class TestFile5(unittest.TestCase):
    def test_feature_5(self):
        self.assertEqual(5 * 2, 10)

    def test_feature_5_squared(self):
        self.assertEqual(5 ** 2, 25)

if __name__ == '__main__':
    unittest.main()