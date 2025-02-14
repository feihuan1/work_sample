import unittest
from io import StringIO
import sys
import os
from unittest.mock import patch
from controller import Controller

class TestController(unittest.TestCase):
    # initialize the class and create temp txt file and data dictionary for test
    def setUp(self):
        self.controller = Controller()
        self.controller.model.DATA_FILE = "test_data_controller.txt"
        self.controller.model.data = {}
    # remove the file after test
    def tearDown(self):
        if os.path.exists("test_data_controller.txt"):
            os.remove("test_data_controller.txt")

    # Captures and returns the output of a function call.
    def capture_output(self, func, *args):
        # Create a StringIO object to store output and Redirect standard output to the StringIO object
        output = StringIO() 
        sys.stdout = output

        try:
            # Call the function with the provided arguments
            func(*args)
        except SystemExit:
            # Prevents sys.exit() from stopping the test execution
            pass
        # Restore the original stdout
        sys.stdout = sys.__stdout__
        # Return the captured output as a string
        return output.getvalue().strip()

#_________________________________________test keys_____________________________
    # test if user input additional params for this command
    def test_keys_with_extra_parameters(self):
        output = self.capture_output(self.controller.keys, ["asd"])
        self.assertEqual(output, "'KEYS' command don't allow paramaters")

    # test if there's no key in data dictionary
    def test_keys_when_empty(self):
        output = self.capture_output(self.controller.keys, [])
        self.assertEqual(output, "(empty set)")

    # test if key command will display all existing keys 
    def test_keys_after_adding_data(self):
        self.controller.model.add("fruits", "apple")
        self.controller.model.add("vehicles", "car")
        output = self.capture_output(self.controller.keys, [])
        expected1 = "1) fruits\n2) vehicles"
        expected2 = "1) vehicles\n2) fruits"
        self.assertIn(output, [expected1, expected2])

#_________________________________________test members_____________________________
    # test if user entered less or more params than program expected
    def test_members_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.members, []) 
        self.assertEqual(output, "Please specify which key's members you want to see.")
        output = self.capture_output(self.controller.members, ["key", "asd"])
        self.assertEqual(output, "Please specify which key's members you want to see.")

    # test if method can get all members for key provided correctly
    def test_members_existing_key(self):
        self.controller.model.add("fruits", "apple")
        self.controller.model.add("fruits", "banana")
        output = self.capture_output(self.controller.members, ["fruits"])
        possible = ["1) apple\n2) banana", "1) banana\n2) apple"]
        self.assertIn(output, possible)

    # test key not exist
    def test_members_nonexistent_key(self):
        output = self.capture_output(self.controller.members, ["fruits"])
        self.assertEqual(output, "ERROR, key does not exist.")

#_________________________________________test add_____________________________
    # test how app handle user enter less or more params after add command
    def test_add_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.add, [])
        self.assertEqual(output, "Please enter one key and one value after 'ADD' command")
        output = self.capture_output(self.controller.add, ["key"])
        self.assertEqual(output, "Please enter one key and one value after 'ADD' command")
        output = self.capture_output(self.controller.add, ["key", "value", "asd"])
        self.assertEqual(output, "Please enter one key and one value after 'ADD' command")

    # test if key is properly stored after user add it correctly
    def test_add_new_key(self):
        output = self.capture_output(self.controller.add, ["fruits", "apple"])
        self.assertEqual(output, "Added")
        self.assertTrue(self.controller.model.is_key_exist("fruits"))
        self.assertTrue(self.controller.model.is_member_exist("fruits", "apple"))

#_________________________________________test remove_____________________________
    # test how app handle user enter less or more params after remove command
    def test_remove_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.remove, [])
        self.assertEqual(output, "Please specify WHICH member inside Witch key you want to remove")
        output = self.capture_output(self.controller.remove, ["key"])
        self.assertEqual(output, "Please specify WHICH member inside Witch key you want to remove")
        output = self.capture_output(self.controller.remove, ["key", "value", "asd"])
        self.assertEqual(output, "Please specify WHICH member inside Witch key you want to remove")

    # test if the member is actually removed after user enter correct command
    def test_remove_member_existing(self):
        self.controller.model.add("fruits", "apple")
        self.controller.model.add("fruits", "orange")
        output = self.capture_output(self.controller.remove, ["fruits", "apple"])
        self.assertEqual(output, "Removed") 
        self.assertFalse(self.controller.model.is_member_exist("fruits", "apple"))

    # test if user try to remove a non-existing member
    def test_remove_member_nonexistent(self):
        self.controller.model.add("fruits", "apple")
        output = self.capture_output(self.controller.remove, ["fruits", "banana"])
        self.assertEqual(output, "ERROR, member does not exist")

#_________________________________________test remove_all_____________________________
    # test how app handle user enter less or more params after removeall command
    def test_remove_all_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.remove_all, [])
        self.assertEqual(output, "Please specify WHICH key you want to remove")
        output = self.capture_output(self.controller.remove_all, ["key", "asd"])
        self.assertEqual(output, "Please specify WHICH key you want to remove")

    # test if key value removed if user enter correct command
    def test_remove_all_existing_key(self):
        self.controller.model.add("fruits", "apple")
        output = self.capture_output(self.controller.remove_all, ["fruits"])
        self.assertEqual(output, "Removed")
        self.assertFalse(self.controller.model.is_key_exist("fruits"))

#_________________________________________test clear_all_____________________________
    # test how app handle user enter less or more params after clear command
    def test_clear_all_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.clear_all, ["asd"])
        self.assertEqual(output, "'CLEAR' command don't allow paramaters")

    # test if dictionary is cleared after user enter clear command
    def test_clear_all_when_not_empty(self):
        self.controller.model.add("fruits", "apple")
        self.controller.model.add("vehicles", "car")
        output = self.capture_output(self.controller.clear_all, [])
        self.assertEqual(output, "Cleared")
        self.assertEqual(self.controller.model.get_keys(), "(empty set)")

#_________________________________________test key_exist_____________________________
    # test how app handle user enter less or more params after keyexists command
    def test_key_exist_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.key_exist, [])
        self.assertEqual(output, "Please specify witch key you want check existence")
        output = self.capture_output(self.controller.key_exist, ["key", "asd"])
        self.assertEqual(output, "Please specify witch key you want check existence")

    # test if it will display true when key exists
    def test_key_exist_true(self):
        self.controller.model.add("fruits", "apple")
        output = self.capture_output(self.controller.key_exist, ["fruits"])
        self.assertEqual(output, "true")

    # test if it will display false when key not exist
    def test_key_exist_false(self):
        output = self.capture_output(self.controller.key_exist, ["fruits"])
        self.assertEqual(output, "false")

#_________________________________________test member_exist_____________________________
    # test how app handle user enter less or more params after memberexists command
    def test_member_exist_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.member_exist, [])
        self.assertEqual(output, "Please specify witch member in witch key you want check existence")
        output = self.capture_output(self.controller.member_exist, ["key"])
        self.assertEqual(output, "Please specify witch member in witch key you want check existence")
        output = self.capture_output(self.controller.member_exist, ["key", "value", "asd"])
        self.assertEqual(output, "Please specify witch member in witch key you want check existence")

    # test if it will display true when member exists
    def test_member_exist_true(self):
        self.controller.model.add("fruits", "apple")
        output = self.capture_output(self.controller.member_exist, ["fruits", "apple"])
        self.assertEqual(output, "true")

    # test if it will display false when member not exist
    def test_member_exist_false(self):
        self.controller.model.add("fruits", "apple")
        output = self.capture_output(self.controller.member_exist, ["fruits", "banana"])
        self.assertEqual(output, "false")

#_________________________________________test all_members_____________________________
    # test how app handle user enter less or more params after allmembers command
    def test_all_members_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.all_members, ["unexpected"])
        self.assertEqual(output, "'ALLMEMBERS' command don't allow paramaters")

    # test when there is no member in the data dictionary
    def test_all_members_when_empty(self):
        output = self.capture_output(self.controller.all_members, [])
        self.assertEqual(output, "(empty set)")

    # test when there is member in data dictioary and user entered correct command
    def test_all_members_with_data(self):
        self.controller.model.add("fruits", "apple")
        self.controller.model.add("fruits", "banana")
        self.controller.model.add("vehicles", "car")
        output = self.capture_output(self.controller.all_members, [])
        possible = ["1) apple\n2) banana\n3) car", "1) apple\n2) car\n3) banana",
                    "1) banana\n2) apple\n3) car", "1) banana\n2) car\n3) apple",
                    "1) car\n2) apple\n3) banana", "1) car\n2) banana\n3) apple"]
        self.assertIn(output, possible)

#_________________________________________test all_items_____________________________
    # test how app handle user enter less or more params after items command
    def test_all_items_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.all_items, ["asd"])
        self.assertEqual(output, "'ALLMEMBERS' command don't allow paramaters")

    # test when data dictionary is emtpy
    def test_all_items_when_empty(self):
        output = self.capture_output(self.controller.all_items, [])
        self.assertEqual(output, "(empty set)")

    # test when there is data in data dictioary and user entered correct command
    def test_all_items_with_data(self):
        self.controller.model.add("fruits", "apple")
        self.controller.model.add("vehicles", "car")
        output = self.capture_output(self.controller.all_items, [])
        self.assertTrue("fruits: apple" in output or "vehicles: car" in output)

#_________________________________________test exit_app_____________________________
    # test how app handle user enter less or more params after exit command
    def test_exit_app_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.exit_app, ["asd"])
        self.assertEqual(output, "'EXIT' command don't allow paramaters")

    # test if exit command works properly
    def test_exit_app(self):
        with self.assertRaises(SystemExit):
            self.controller.exit_app([])

#_________________________________________test run_____________________________
    # test if user entered a invalid command
    def test_run_invalid_command(self):
        with patch.object(self.controller.view, 'get_input', side_effect=["INVALID", "EXIT"]):
            output = self.capture_output(self.controller.run)
            self.assertIn("Invalid command...", output)

    # test when user press ctrl+C force quit
    def test_run_keyboard_interrupt(self):
        with patch.object(self.controller.view, 'get_input', side_effect=KeyboardInterrupt):
            output = self.capture_output(self.controller.run)
            self.assertIn("Exiting application. Goodbye!", output)

if __name__ == '__main__':
    unittest.main()
