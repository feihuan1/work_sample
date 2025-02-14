import unittest
from io import StringIO
import sys
import os
from unittest.mock import patch
from controller import Controller

class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()
        self.controller.model.DATA_FILE = "test_data_controller.txt"
        self.controller.model.data = {}

    def tearDown(self):
        if os.path.exists("test_data_controller.txt"):
            os.remove("test_data_controller.txt")

    def capture_output(self, func, *args):
        output = StringIO()
        sys.stdout = output
        try:
            func(*args)
        except SystemExit:
            #preventing sys.exit() from stopping tests
            pass
        sys.stdout = sys.__stdout__
        return output.getvalue().strip()

#_________________________________________test keys_____________________________
    def test_keys_with_extra_parameters(self):
        output = self.capture_output(self.controller.keys, ["unexpected"])
        self.assertEqual(output, "'KEYS' command don't allow paramaters")

    def test_keys_when_empty(self):
        output = self.capture_output(self.controller.keys, [])
        self.assertEqual(output, "(empty set)")

    def test_keys_after_adding_data(self):
        self.controller.model.add("fruits", "apple")
        self.controller.model.add("vehicles", "car")
        output = self.capture_output(self.controller.keys, [])
        expected1 = "1) fruits\n2) vehicles"
        expected2 = "1) vehicles\n2) fruits"
        self.assertIn(output, [expected1, expected2])

#_________________________________________test members_____________________________
    def test_members_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.members, [])
        self.assertEqual(output, "Please specify which key's members you want to see.")
        output = self.capture_output(self.controller.members, ["key", "extra"])
        self.assertEqual(output, "Please specify which key's members you want to see.")

    def test_members_existing_key(self):
        self.controller.model.add("fruits", "apple")
        self.controller.model.add("fruits", "banana")
        output = self.capture_output(self.controller.members, ["fruits"])
        possible = ["1) apple\n2) banana", "1) banana\n2) apple"]
        self.assertIn(output, possible)

    def test_members_nonexistent_key(self):
        output = self.capture_output(self.controller.members, ["fruits"])
        self.assertEqual(output, "ERROR, key does not exist.")

#_________________________________________test add_____________________________
    def test_add_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.add, [])
        self.assertEqual(output, "Please enter one key and one value after 'ADD' command")
        output = self.capture_output(self.controller.add, ["key"])
        self.assertEqual(output, "Please enter one key and one value after 'ADD' command")
        output = self.capture_output(self.controller.add, ["key", "value", "extra"])
        self.assertEqual(output, "Please enter one key and one value after 'ADD' command")

    def test_add_new_key(self):
        output = self.capture_output(self.controller.add, ["fruits", "apple"])
        self.assertEqual(output, "Added")
        self.assertTrue(self.controller.model.is_key_exist("fruits"))
        self.assertTrue(self.controller.model.is_member_exist("fruits", "apple"))

#_________________________________________test remove_____________________________
    def test_remove_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.remove, [])
        self.assertEqual(output, "Please specify WHICH member inside Witch key you want to remove")
        output = self.capture_output(self.controller.remove, ["key"])
        self.assertEqual(output, "Please specify WHICH member inside Witch key you want to remove")
        output = self.capture_output(self.controller.remove, ["key", "value", "extra"])
        self.assertEqual(output, "Please specify WHICH member inside Witch key you want to remove")

    def test_remove_member_existing(self):
        self.controller.model.add("fruits", "apple")
        output = self.capture_output(self.controller.remove, ["fruits", "apple"])
        self.assertEqual(output, "Removed")
        self.assertFalse(self.controller.model.is_member_exist("fruits", "apple"))

    def test_remove_member_nonexistent(self):
        self.controller.model.add("fruits", "apple")
        output = self.capture_output(self.controller.remove, ["fruits", "banana"])
        self.assertEqual(output, "ERROR, member does not exist")

#_________________________________________test remove_all_____________________________
    def test_remove_all_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.remove_all, [])
        self.assertEqual(output, "Please specify WHICH key you want to remove")
        output = self.capture_output(self.controller.remove_all, ["key", "extra"])
        self.assertEqual(output, "Please specify WHICH key you want to remove")

    def test_remove_all_existing_key(self):
        self.controller.model.add("fruits", "apple")
        output = self.capture_output(self.controller.remove_all, ["fruits"])
        self.assertEqual(output, "Removed")
        self.assertFalse(self.controller.model.is_key_exist("fruits"))

#_________________________________________test clear_all_____________________________
    def test_clear_all_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.clear_all, ["unexpected"])
        self.assertEqual(output, "'CLEAR' command don't allow paramaters")

    def test_clear_all_when_not_empty(self):
        self.controller.model.add("fruits", "apple")
        self.controller.model.add("vehicles", "car")
        output = self.capture_output(self.controller.clear_all, [])
        self.assertEqual(output, "Cleared")
        self.assertEqual(self.controller.model.get_keys(), "(empty set)")

#_________________________________________test key_exist_____________________________
    def test_key_exist_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.key_exist, [])
        self.assertEqual(output, "Please specify witch key you want check existence")
        output = self.capture_output(self.controller.key_exist, ["key", "extra"])
        self.assertEqual(output, "Please specify witch key you want check existence")

    def test_key_exist_true(self):
        self.controller.model.add("fruits", "apple")
        output = self.capture_output(self.controller.key_exist, ["fruits"])
        self.assertEqual(output, "true")

    def test_key_exist_false(self):
        output = self.capture_output(self.controller.key_exist, ["fruits"])
        self.assertEqual(output, "false")

#_________________________________________test member_exist_____________________________
    def test_member_exist_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.member_exist, [])
        self.assertEqual(output, "Please specify witch member in witch key you want check existence")
        output = self.capture_output(self.controller.member_exist, ["key"])
        self.assertEqual(output, "Please specify witch member in witch key you want check existence")
        output = self.capture_output(self.controller.member_exist, ["key", "value", "extra"])
        self.assertEqual(output, "Please specify witch member in witch key you want check existence")

    def test_member_exist_true(self):
        self.controller.model.add("fruits", "apple")
        output = self.capture_output(self.controller.member_exist, ["fruits", "apple"])
        self.assertEqual(output, "true")

    def test_member_exist_false(self):
        self.controller.model.add("fruits", "apple")
        output = self.capture_output(self.controller.member_exist, ["fruits", "banana"])
        self.assertEqual(output, "false")

#_________________________________________test all_members_____________________________
    def test_all_members_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.all_members, ["unexpected"])
        self.assertEqual(output, "'ALLMEMBERS' command don't allow paramaters")

    def test_all_members_when_empty(self):
        output = self.capture_output(self.controller.all_members, [])
        self.assertEqual(output, "ERROR: No members found.")

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
    def test_all_items_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.all_items, ["unexpected"])
        self.assertEqual(output, "'ALLMEMBERS' command don't allow paramaters")

    def test_all_items_when_empty(self):
        output = self.capture_output(self.controller.all_items, [])
        self.assertEqual(output, "ERROR: No items found.")

    def test_all_items_with_data(self):
        self.controller.model.add("fruits", "apple")
        self.controller.model.add("vehicles", "car")
        output = self.capture_output(self.controller.all_items, [])
        self.assertTrue("fruits: apple" in output or "vehicles: car" in output)

#_________________________________________test exit_app_____________________________
    def test_exit_app_with_wrong_parameter_count(self):
        output = self.capture_output(self.controller.exit_app, ["unexpected"])
        self.assertEqual(output, "'EXIT' command don't allow paramaters")

    def test_exit_app(self):
        with self.assertRaises(SystemExit):
            self.controller.exit_app([])

#_________________________________________test run_____________________________
    def test_run_invalid_command(self):
        with patch.object(self.controller.view, 'get_input', side_effect=["INVALID", "EXIT"]):
            output = self.capture_output(self.controller.run)
            self.assertIn("Invalid command...", output)

    def test_run_keyboard_interrupt(self):
        with patch.object(self.controller.view, 'get_input', side_effect=KeyboardInterrupt):
            output = self.capture_output(self.controller.run)
            self.assertIn("Exiting application. Goodbye!", output)

if __name__ == '__main__':
    unittest.main()
