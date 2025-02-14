import unittest
import os
from model import Model 

class TestModel(unittest.TestCase):

    # initialize the class and temp txt file path for testing
    def setUp(self):
        self.test_file = "test_data.txt"
        self.model = Model(self.test_file)

    # delete the temp test_data.txt file after testing
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

#_________________________________________test get_keys_____________________________
    # test get_key when there is no key in data dictionary
    def test_get_keys_when_empty(self):
        result = self.model.get_keys()
        self.assertEqual(result, "(empty set)")

    # test get_key when there is key in data dictionary
    def test_get_keys_after_adding_data(self):
        self.model.add("fruits", "apple")
        self.model.add("vehicles", "car")
        result = self.model.get_keys()
        self.assertListEqual(sorted(result), ["fruits", "vehicles"])

    # test get_key when there is key but removed later
    def test_get_keys_after_removing_all(self):
        self.model.add("fruits", "apple")
        self.model.clear_all()
        result = self.model.get_keys()
        self.assertEqual(result, "(empty set)")

#_________________________________________test get_members_____________________________
    # test get_members when key and menber exists
    def test_get_members_existing_key(self):
        self.model.add("fruits", "apple")
        self.model.add("fruits", "banana")
        result = self.model.get_members("fruits")
        self.assertListEqual(sorted(result), ["apple", "banana"])

    # test get_members when key not exists
    def test_get_members_nonexistent_key(self):
        result = self.model.get_members("fruits")
        self.assertEqual(result, "ERROR, key does not exist.")


#_________________________________________test add_____________________________
    # test when add key member normally
    def test_add_new_key(self):
        result = self.model.add("fruits", "apple")
        self.assertEqual(result, "Added")
        self.assertTrue(self.model.is_key_exist("fruits"))
        self.assertTrue(self.model.is_member_exist("fruits", "apple"))

    # test try add existing member
    def test_add_duplicate_member(self):
        self.model.add("fruits", "apple")
        result = self.model.add("fruits", "apple")
        self.assertEqual(result, "ERROR, member already exists for key")

    # test add member to a existing key with some existing member
    def test_add_multiple_members_same_key(self):
        self.model.add("fruits", "apple")
        self.model.add("fruits", "banana")
        result = self.model.get_members("fruits")
        self.assertListEqual(sorted(result), ["apple", "banana"])

#_________________________________________test remove_member_____________________________
    # test when user remove a existing member
    def test_remove_member_existing(self):
        self.model.add("fruits", "apple")
        self.model.add("fruits", "orange")
        result = self.model.remove_member("fruits", "apple")
        self.assertEqual(result, "Removed")
        self.assertFalse(self.model.is_member_exist("fruits", "apple"))

    # test when user try remove a non-exist member
    def test_remove_member_nonexistent(self):
        self.model.add("fruits", "apple")
        result = self.model.remove_member("fruits", "banana")
        self.assertEqual(result, "ERROR, member does not exist")

    # test when user try to remove a member twice
    def test_remove_member_from_empty_key(self):
        self.model.add("fruits", "apple")
        self.model.add("fruits", "orange")
        self.model.remove_member("fruits", "apple")
        result = self.model.remove_member("fruits", "apple")
        self.assertEqual(result, "ERROR, member does not exist")

#_________________________________________test remove_key_____________________________
    # test when remove a existing key
    def test_remove_key_existing(self):
        self.model.add("fruits", "apple")
        result = self.model.remove_key("fruits")
        self.assertEqual(result, "Removed")
        self.assertFalse(self.model.is_key_exist("fruits"))

    # test when try to remove a non existing key
    def test_remove_key_nonexistent(self):
        result = self.model.remove_key("fruits")
        self.assertEqual(result, "ERROR, key does not exist")

    # test remove the key when it has multiple values
    def test_remove_key_with_multiple_members(self):
        self.model.add("fruits", "apple")
        self.model.add("fruits", "banana")
        result = self.model.remove_key("fruits")
        self.assertEqual(result, "Removed")
        self.assertEqual(self.model.get_keys(), "(empty set)")

#_________________________________________test clear_all_____________________________
    # test when there is key member to be clear
    def test_clear_all(self):
        self.model.add("fruits", "apple")
        self.model.add("vehicles", "car")
        result = self.model.clear_all()
        self.assertEqual(result, "Cleared")
        self.assertEqual(self.model.get_keys(), "(empty set)")

    # test when the data dictionary is already empty
    def test_clear_already_empty(self):
        result = self.model.clear_all()
        self.assertEqual(result, "Cleared")

#_________________________________________test get_all_members_____________________________
    # test when there is member in data dictionary
    def test_get_all_members(self):
        self.model.add("fruits", "apple")
        self.model.add("fruits", "banana")
        self.model.add("vehicles", "car")
        result = self.model.get_all_members()
        self.assertListEqual(sorted(result), ["apple", "banana", "car"])

    # test when there is no member in data dictionary
    def test_get_all_members_empty(self):
        result = self.model.get_all_members()
        self.assertEqual(result, "(empty set)")

#_________________________________________test get_items_____________________________
    # test when there is item in data dictionary
    def test_get_items(self):
        self.model.add("fruits", "apple")
        self.model.add("vehicles", "car")
        result = self.model.get_items()
        self.assertIn("fruits: apple", result)
        self.assertIn("vehicles: car", result)

    # test when there is no item in data dictionary
    def test_get_items_empty(self):
        result = self.model.get_items()
        self.assertEqual(result, "(empty set)")

#_________________________________________test save_data & load_data_____________________________
    # test if save work as intended
    def test_save_and_load_data(self):
        self.model.add("fruits", "apple")
        self.model.save_data()
        new_model = Model(self.test_file)
        self.assertTrue(new_model.is_key_exist("fruits"))
        self.assertTrue(new_model.is_member_exist("fruits", "apple"))

    # test when there is no data to save
    def test_save_and_load_empty_data(self):
        self.model.save_data()
        new_model = Model(self.test_file)
        self.assertEqual(new_model.get_keys(), "(empty set)")

    # test save data when there is more than one key in data dictionary
    def test_save_and_load_multiple_keys(self):
        self.model.add("fruits", "apple")
        self.model.add("vehicles", "car")
        self.model.save_data()
        new_model = Model(self.test_file)
        self.assertListEqual(sorted(new_model.get_keys()), ["fruits", "vehicles"])

    # test load data when there is invalid data format in txt file
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
