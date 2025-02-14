import unittest
import os
from model import MultiValueDictionary

class TestMultiValueDictionary(unittest.TestCase):

    def setUp(self):
        self.mvd = MultiValueDictionary("test_data.txt")
        if os.path.exists("test_data.txt"):
            os.remove("test_data.txt")

    def tearDown(self):
        if os.path.exists("test_data.txt"):
            os.remove("test_data.txt")

    def test_add_value(self):
        result = self.mvd.add("foo", "bar")
        self.assertEqual(result, ") Added")
        self.assertEqual(self.mvd.get_members("foo"), ["bar"])

    def test_add_duplicate_value(self):
        self.mvd.add("foo", "bar")
        result = self.mvd.add("foo", "bar")
        self.assertEqual(result, ") ERROR, member already exists for key")

    def test_get_nonexistent_key(self):
        result = self.mvd.get_members("unknown")
        self.assertEqual(result, ") ERROR, key does not exist.")

if __name__ == "__main__":
    unittest.main()