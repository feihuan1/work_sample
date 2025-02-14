import sys
from model import Model
from view import View

class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()
        self.command_heads = {
            "KEYS": self.keys,
            "MEMBERS": self.members,
            "ADD": self.add, 
            "REMOVE": self.remove, 
            "REMOVEALL": self.remove_all, 
            "EXIT": self.exit_app,
        }
    

    def keys(self, command_params: list):
        if len(command_params) != 0:
            self.view.display_message("\n'KEYS' command don\'t allow paramaters \n")
            return
        result = self.model.get_keys()
        if isinstance(result, list):
            for idx, key in enumerate(result, start=1):
                self.view.display_message(f"{idx}) {key}")
        else:
            self.view.display_message(result)


    def members(self, command_params: list):
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

            
    def add(self, command_params: list):
        if len(command_params) != 2:
            self.view.display_message("\nPlease enter one key and one value after 'ADD' command\n")
            return
        key = command_params[0]
        value = command_params[1]
        result = self.model.add(key, value)
        self.view.display_message(result)


    def remove(self, command_params: list):
        if len(command_params) != 2:
            self.view.display_message("\nPlease specify WHICH value inside Witch key you want to remove\n")
            return
        key = command_params[0]
        value = command_params[1]
        result = self.model.remove_member(key, value)
        self.view.display_message(result)

    def remove_all(self, command_params: list):
        if len(command_params) != 1:
            self.view.display_message("\nPlease specify WHICH key you want to remove\n")
            return
        key = command_params[0]
        result = self.model.remove_key(key)
        self.view.display_message(result)
    
    def clear(self, command_params: list):
        if len(command_params) != 0:
            self.view.display_message("\n'CLEAR' command don\'t allow paramaters \n")
        result = self.model.clear_all()
        self.view.display_message(result)

    def exit_app(self, command_params: list):
        if len(command_params) != 0:
            self.view.display_message("\n'EXIT' command don\'t allow paramaters \n")
            return
        self.view.display_message("\nGoodbye!\n")
        sys.exit(0)

    def run(self, test_input=None):
        while True:
            # hard code test case in test mode
            if test_input:
                user_input = test_input
            else:
                user_input = self.view.get_input("\nPlease enter command\n").strip()

            if not user_input:
                continue

            command = user_input.split(" ")
            command_head = command[0].upper()

            # prevent user enter moultiple spaces
            command_params = [word for word in command[1:] if word]

            if command_head in self.command_heads:
                self.command_heads[command_head](command_params)
                # give test_int a value when testing or it will keep looping!!!
                if test_input:
                    return
            else:
                self.view.display_message("Invalid command...")

