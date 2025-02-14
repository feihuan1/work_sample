import unittest
from io import StringIO
import sys
from unittest.mock import patch
from view import View

class TestView(unittest.TestCase):
    # initialize the class for testing
    def setUp(self):
        self.view = View()

    # Captures and returns the output of a function call.
    def capture_output(self, func, *args):
        # Create a StringIO object to store output and Redirect standard output to the StringIO object
        output = StringIO()
        sys.stdout = output  
        # Call the function with the provided arguments
        func(*args)  
        # Restore the original stdout
        sys.stdout = sys.__stdout__ 
        # Return the captured output as a string
        return output.getvalue().strip() 

#______________________________________________test get_input________________________________________________________________
    # test input with white space
    def test_get_input_trims_whitespace(self):
        with patch('builtins.input', return_value="   test input   "):
            result = self.view.get_input("Prompt: ")
            self.assertEqual(result, "test input")
    
#______________________________________________test display_message________________________________________________________________
    # test display normal message
    def test_display_message(self):
        output = self.capture_output(self.view.display_message, "Hello, World!")
        self.assertEqual(output, "Hello, World!")

    # test when message is empty string
    def test_display_message_with_empty(self):
        output = self.capture_output(self.view.display_message, "")
        self.assertEqual(output, "No message availiable")

    # test when message has leading and trailing white space
    def test_display_message_with_space(self):
        output = self.capture_output(self.view.display_message, "   Hello, World!   ")
        self.assertEqual(output, "Hello, World!") 

    # test if input in other type and see if it will convert to string
    def test_display_message_with_type_error(self):
        output = self.capture_output(self.view.display_message, None)
        self.assertEqual(output, "None") 

    # test when message has multiple line
    def test_display_message_with_newlines(self):
        output = self.capture_output(self.view.display_message, "\nHello,\nWorld!\n")
        self.assertEqual(output, "Hello,\nWorld!")

#______________________________________________test display_message_by_type_____________________________________________________________
    # test when input is a string
    def test_display_message_by_type_string(self):
        output = self.capture_output(self.view.display_message_by_type, "This is a test")
        self.assertEqual(output, "This is a test")
    
    # test when input is a string with space around
    def test_display_message_by_type_string_with_spaces(self):
        output = self.capture_output(self.view.display_message_by_type, "    hello   ")
        self.assertEqual(output, "hello") 

    # test if input is a boolean True
    def test_display_message_by_type_boolean_true(self):
        output = self.capture_output(self.view.display_message_by_type, True)
        self.assertEqual(output, "true")  

    # test if input is a boolean False
    def test_display_message_by_type_boolean_false(self):
        output = self.capture_output(self.view.display_message_by_type, False)
        self.assertEqual(output, "false")

    # test when input is a list
    def test_display_message_by_type_list(self):
        output = self.capture_output(self.view.display_message_by_type, ["Apple", "Banana", "Cherry"])
        expected_output = "1) Apple\n2) Banana\n3) Cherry"
        self.assertEqual(output, expected_output)

    # test when input list has empty element
    def test_display_message_by_type_list_empty_value(self):
        output = self.capture_output(self.view.display_message_by_type, ["Apple", "Banana", "Cherry", "", "  "])
        expected_output = "1) Apple\n2) Banana\n3) Cherry"
        self.assertEqual(output, expected_output)

    # test when input list has no actual content
    def test_display_message_by_type_list_all_empty(self):
        output = self.capture_output(self.view.display_message_by_type, ["", "   "])
        self.assertEqual(output, "No items found.")

    # test when input is a empty list
    def test_display_message_by_type_empty_list(self):
        output = self.capture_output(self.view.display_message_by_type, [])
        self.assertEqual(output, "No items found.")

    # test when input is a unexpected type
    def test_display_message_by_type_invalid_type(self):
        with self.assertRaises(TypeError):
            self.view.display_message_by_type(123)

if __name__ == '__main__':
    unittest.main()
