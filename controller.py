import sys
from model import MultiValueDictionary
from view import View

class Controller:

    def __init__(self):
        self.model = MultiValueDictionary()
        self.view = View()
        self.command_heads = {
            "ADD": self.add,
            "MEMBERS": self.members,
            "EXIT": self.exit_app
        }

    def add(self, command_params):
        if len(command_params) != 2:
            self.view.display_message("\nPlease enter one key and one value after 'ADD' command\n")
            return

        key = command_params[0]
        value = command_params[1]
        result = self.model.add(key, value)
        self.view.display_message(result)

    def members(self, command_params):
        if len(command_params) != 1:
            self.view.display_message("\nPlease specify WHICH KEY you want to check\n")
            return

        key = command_params[0]
        result = self.model.get_members(key)
        if isinstance(result, list):
            for idx, val in enumerate(result, start=1):
                self.view.display_message(f"{idx}) {val}")
        else:
            self.view.display_message(result)

    def exit_app(self, *args):
        self.view.display_message("\nGoodbye!\n")
        sys.exit(0)

    def run(self, test_input=None):
        while True:
            if test_input:
                user_input = test_input
            else:
                user_input = self.view.get_input("\nPlease enter command\n").strip()

            if not user_input:
                continue

            command = user_input.split(" ")
            command_head = command[0].upper()
            command_params = command[1:]

            if command_head in self.command_heads:
                self.command_heads[command_head](command_params)
                
                if test_input:
                    return

            else:
                self.view.display_message("Unknown command...")

