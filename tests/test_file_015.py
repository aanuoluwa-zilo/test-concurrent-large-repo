# Test file 15
import unittest

class TestFile15(unittest.TestCase):
    def test_feature_15(self):
        self.assertEqual(15 * 2, 30)

    def test_feature_15_squared(self):
        self.assertEqual(15 ** 2, 225)

if __name__ == '__main__':
    unittest.main()