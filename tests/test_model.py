import unittest
import os
from model import Model 

class TestModel(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_data.txt"
        self.model = Model(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

#_________________________________________test get_keys_____________________________
    def test_get_keys_when_empty(self):
        result = self.model.get_keys()
        self.assertEqual(result, "(empty set)")

    def test_get_keys_after_adding_data(self):
        self.model.add("fruits", "apple")
        self.model.add("vehicles", "car")
        result = self.model.get_keys()
        self.assertListEqual(sorted(result), ["fruits", "vehicles"])

    def test_get_keys_after_removing_all(self):
        self.model.add("fruits", "apple")
        self.model.clear_all()
        result = self.model.get_keys()
        self.assertEqual(result, "(empty set)")

#_________________________________________test get_members_____________________________
    def test_get_members_existing_key(self):
        self.model.add("fruits", "apple")
        self.model.add("fruits", "banana")
        result = self.model.get_members("fruits")
        self.assertListEqual(sorted(result), ["apple", "banana"])

    def test_get_members_nonexistent_key(self):
        result = self.model.get_members("fruits")
        self.assertEqual(result, "ERROR, key does not exist.")

    def test_get_members_empty_key(self):
        self.model.add("fruits", "apple")
        self.model.remove_member("fruits", "apple")
        result = self.model.get_members("fruits")
        self.assertEqual(result, "ERROR: No members found in this key.")

#_________________________________________test add_____________________________
    def test_add_new_key(self):
        result = self.model.add("fruits", "apple")
        self.assertEqual(result, "Added")
        self.assertTrue(self.model.is_key_exist("fruits"))
        self.assertTrue(self.model.is_member_exist("fruits", "apple"))

    def test_add_duplicate_member(self):
        self.model.add("fruits", "apple")
        result = self.model.add("fruits", "apple")
        self.assertEqual(result, "ERROR, member already exists for key")

    def test_add_empty_key(self):
        result = self.model.add("", "value")
        self.assertEqual(result, "Added")
        self.assertTrue(self.model.is_key_exist(""))
        self.assertTrue(self.model.is_member_exist("", "value"))

    def test_add_empty_value(self):
        result = self.model.add("key", "")
        self.assertEqual(result, "Added")
        self.assertTrue(self.model.is_key_exist("key"))
        self.assertTrue(self.model.is_member_exist("key", ""))

    def test_add_multiple_members_same_key(self):
        self.model.add("fruits", "apple")
        self.model.add("fruits", "banana")
        result = self.model.get_members("fruits")
        self.assertListEqual(sorted(result), ["apple", "banana"])

#_________________________________________test remove_member_____________________________
    def test_remove_member_existing(self):
        self.model.add("fruits", "apple")
        result = self.model.remove_member("fruits", "apple")
        self.assertEqual(result, "Removed")
        self.assertFalse(self.model.is_member_exist("fruits", "apple"))

    def test_remove_member_nonexistent(self):
        self.model.add("fruits", "apple")
        result = self.model.remove_member("fruits", "banana")
        self.assertEqual(result, "ERROR, member does not exist")

    def test_remove_member_from_empty_key(self):
        self.model.add("fruits", "apple")
        self.model.remove_member("fruits", "apple")
        result = self.model.remove_member("fruits", "apple")
        self.assertEqual(result, "ERROR, member does not exist")

    def test_remove_member_with_empty_value(self):
        self.model.add("key", "")
        result = self.model.remove_member("key", "")
        self.assertEqual(result, "Removed")
        self.assertFalse(self.model.is_member_exist("key", ""))

#_________________________________________test remove_key_____________________________
    def test_remove_key_existing(self):
        self.model.add("fruits", "apple")
        result = self.model.remove_key("fruits")
        self.assertEqual(result, "Removed")
        self.assertFalse(self.model.is_key_exist("fruits"))

    def test_remove_key_nonexistent(self):
        result = self.model.remove_key("fruits")
        self.assertEqual(result, "ERROR, key does not exist")

    def test_remove_key_with_multiple_members(self):
        self.model.add("fruits", "apple")
        self.model.add("fruits", "banana")
        result = self.model.remove_key("fruits")
        self.assertEqual(result, "Removed")
        self.assertEqual(self.model.get_keys(), "(empty set)")

#_________________________________________test clear_all_____________________________
    def test_clear_all(self):
        self.model.add("fruits", "apple")
        self.model.add("vehicles", "car")
        result = self.model.clear_all()
        self.assertEqual(result, "Cleared")
        self.assertEqual(self.model.get_keys(), "(empty set)")

    def test_clear_already_empty(self):
        result = self.model.clear_all()
        self.assertEqual(result, "ERROR, The dictionary is already empty.")

#_________________________________________test get_all_members_____________________________
    def test_get_all_members(self):
        self.model.add("fruits", "apple")
        self.model.add("fruits", "banana")
        self.model.add("vehicles", "car")
        result = self.model.get_all_members()
        self.assertListEqual(sorted(result), ["apple", "banana", "car"])

    def test_get_all_members_empty(self):
        result = self.model.get_all_members()
        self.assertEqual(result, "ERROR: No members found.")

#_________________________________________test get_items_____________________________
    def test_get_items(self):
        self.model.add("fruits", "apple")
        self.model.add("vehicles", "car")
        result = self.model.get_items()
        self.assertIn("fruits: apple", result)
        self.assertIn("vehicles: car", result)

    def test_get_items_empty(self):
        result = self.model.get_items()
        self.assertEqual(result, "ERROR: No items found.")

#_________________________________________test save_data & load_data_____________________________
    def test_save_and_load_data(self):
        self.model.add("fruits", "apple")
        self.model.save_data()
        new_model = Model(self.test_file)
        self.assertTrue(new_model.is_key_exist("fruits"))
        self.assertTrue(new_model.is_member_exist("fruits", "apple"))

    def test_save_and_load_empty_data(self):
        self.model.save_data()
        new_model = Model(self.test_file)
        self.assertEqual(new_model.get_keys(), "(empty set)")

    def test_save_and_load_multiple_keys(self):
        self.model.add("fruits", "apple")
        self.model.add("vehicles", "car")
        self.model.save_data()
        new_model = Model(self.test_file)
        self.assertListEqual(sorted(new_model.get_keys()), ["fruits", "vehicles"])

    def test_load_data_with_invalid_lines(self):
        with open(self.test_file, "w") as f:
            f.write("invalid data without colon\n")
            f.write(":value_without_key\n")
            f.write("valid:apple,banana\n")
        new_model = Model(self.test_file)
        self.assertTrue(new_model.is_key_exist("valid"))
        self.assertListEqual(sorted(new_model.get_members("valid")), ["apple", "banana"])

if __name__ == '__main__':
    unittest.main()
