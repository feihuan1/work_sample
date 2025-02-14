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
            "KEYEXISTS": self.key_exist, 
            "MEMBEREXISTS": self.member_exist, 
            "ALLMEMBERS": self.all_members, 
            "ITEMS": self.all_items, 
            "CLEAR": self.clear_all, 
            "EXIT": self.exit_app,
        }
    
    def keys(self, command_params: list):
        if len(command_params) != 0:
            self.view.display_message("\n'KEYS' command don\'t allow paramaters \n")
            return
        
        result = self.model.get_keys()

        self.view.display_message_by_type(result)

    def members(self, command_params: list):
        if len(command_params) != 1:
            self.view.display_message("\nPlease specify which key's members you want to see.\n")
            return
        
        key = command_params[0]
        result = self.model.get_members(key)

        self.view.display_message_by_type(result)
      
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
            self.view.display_message("\nPlease specify WHICH member inside Witch key you want to remove\n")
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
    
    def clear_all(self, command_params: list):
        if len(command_params) != 0:
            self.view.display_message("\n'CLEAR' command don\'t allow paramaters \n")
            return
        
        result = self.model.clear_all()
        self.view.display_message(result)
    
    def key_exist(self, command_params: list):
        if len(command_params) != 1:
            self.view.display_message("\nPlease specify witch key you want check existence\n")
            return
        
        key = command_params[0]
        result = self.model.is_key_exist(key)
        self.view.display_message_by_type(result)

    def member_exist(self, command_params: list):
        if len(command_params) != 2:
            self.view.display_message("\nPlease specify witch member in witch key you want check existence\n")
            return
        
        key = command_params[0]
        value = command_params[1]
        result = self.model.is_member_exist(key, value)

        self.view.display_message_by_type(result)

    def all_members(self, command_params: list):
        if len(command_params) != 0:
            self.view.display_message("\n'ALLMEMBERS' command don\'t allow paramaters \n")
            return
        
        result = self.model.get_all_members()

        self.view.display_message_by_type(result)

    def all_items(self, command_params: list):
        if len(command_params) != 0:
            self.view.display_message("\n'ALLMEMBERS' command don\'t allow paramaters \n")
            return
        
        result = self.model.get_items()

        self.view.display_message_by_type(result)
        

    def exit_app(self, command_params: list):
        if len(command_params) != 0:
            self.view.display_message("\n'EXIT' command don\'t allow paramaters \n")
            return
        
        self.view.display_message("\n\nExiting application. Goodbye!")
        sys.exit(0)

    def run(self):
        try:
            while True:
                user_input = self.view.get_input("\nPlease enter command\n")

                if not user_input:
                    continue

                command = user_input.split(" ")
                command_head = command[0].upper()
                # prevent user enter moultiple spaces
                command_params = [word for word in command[1:] if word]

                if command_head in self.command_heads:
                    self.command_heads[command_head](command_params)
                else:
                    self.view.display_message("Invalid command...")
        except KeyboardInterrupt:
            self.view.display_message("\n\nExiting application. Goodbye!")
            sys.exit(0)
