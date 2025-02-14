import unittest
from unittest.mock import patch
import io
from view import View

class TestView(unittest.TestCase):

    @patch("builtins.input", return_value="test input")
    def test_get_input(self, mock_input):
        """Tests if user input is correctly received."""
        result = View.get_input("Enter something:")
        self.assertEqual(result, "test input")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_message(self, mock_stdout):
        """Tests if messages are correctly printed."""
        View.display_message("Hello, World!")
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()