import unittest
from unittest.mock import MagicMock
from controller import Controller

class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()
        self.controller.model = MagicMock()
        self.controller.view = MagicMock()

    def test_add_command(self):
        self.controller.model.add.return_value = ") Added"

        self.controller.run(test_input="ADD foo bar")

        self.controller.model.add.assert_called_with("foo", "bar")
        self.controller.view.display_message.assert_called_with(") Added")

    def test_members_command(self):
        self.controller.model.get_members.return_value = ["bar"]

        self.controller.run(test_input="MEMBERS foo")

        self.controller.model.get_members.assert_called_with("foo")
        self.controller.view.display_message.assert_called_with("1) bar")

    def test_exit_command(self):
        with self.assertRaises(SystemExit):
            self.controller.run(test_input="EXIT")

        self.controller.view.display_message.assert_called_with("\nGoodbye!\n")

if __name__ == "__main__":
    unittest.main()
