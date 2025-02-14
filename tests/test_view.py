import unittest
from io import StringIO
import sys
from view import View

class TestView(unittest.TestCase):
    
    def setUp(self):
        self.view = View()

    def capture_output(self, func, *args):
        output = StringIO()
        sys.stdout = output  
        func(*args)  
        sys.stdout = sys.__stdout__ 
        return output.getvalue().strip() 
#______________________________________________test display_message________________________________________________________________
    def test_display_message(self):
        output = self.capture_output(self.view.display_message, "Hello, World!")
        self.assertEqual(output, "Hello, World!")

    def test_display_message_with_empty(self):
        output = self.capture_output(self.view.display_message, "")
        self.assertEqual(output, "No message availiable")

    def test_display_message_with_space(self):
        output = self.capture_output(self.view.display_message, "   Hello, World!   ")
        self.assertEqual(output, "Hello, World!") 

    def test_display_message_with_type_error(self):
        output = self.capture_output(self.view.display_message, None)
        self.assertEqual(output, "None") 
#_________________________________________________test display_message_by_type_____________________________________________________________

    def test_display_message_by_type_string(self):
        output = self.capture_output(self.view.display_message_by_type, "This is a test")
        self.assertEqual(output, "This is a test")
    
    def test_display_message_by_type_string_with_spaces(self):
        output = self.capture_output(self.view.display_message_by_type, "    hello   ")
        self.assertEqual(output, "hello") 

    def test_display_message_by_type_boolean_true(self):
        output = self.capture_output(self.view.display_message_by_type, True)
        self.assertEqual(output, "true")  

    def test_display_message_by_type_boolean_false(self):
        output = self.capture_output(self.view.display_message_by_type, False)
        self.assertEqual(output, "false")

    def test_display_message_by_type_list(self):
        output = self.capture_output(self.view.display_message_by_type, ["Apple", "Banana", "Cherry"])
        expected_output = "1) Apple\n2) Banana\n3) Cherry"
        self.assertEqual(output, expected_output)

    def test_display_message_by_type_list_empty_value(self):
        output = self.capture_output(self.view.display_message_by_type, ["Apple", "Banana", "Cherry", "", "  "])
        expected_output = "1) Apple\n2) Banana\n3) Cherry"
        self.assertEqual(output, expected_output)

    def test_display_message_by_type_empty_list(self):
        output = self.capture_output(self.view.display_message_by_type, [])
        self.assertEqual(output, "No items found.")

    def test_display_message_by_type_invalid_type(self):
        with self.assertRaises(TypeError): 
            self.view.display_message_by_type(123)  
#______________________________________________________________________________________________________________


if __name__ == '__main__':
    unittest.main()