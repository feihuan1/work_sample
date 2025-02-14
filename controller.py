import sys
from model import Model
from view import View

# Controller handles user input and updates the Model
class Controller:

    def __init__(self):
        # get instance of View and Model class
        self.model = Model()
        self.view = View()
        # define witch function to run for each valid command_head
        # first word in the user command is the command_head, 
        # exp: ADD foo bar, 'ADD' is the command_head, "foo bar" is command_params
        # command_head is not case sensitive, allow user enter upper or lower case
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
    
    # display all keys in the data dictionary
    # the command is 'keys' in any case,with no more params
    def keys(self, command_params: list):
        # handle if user enter incorrect command exp: "KEYS dsada asd"
        if len(command_params) != 0:
            self.view.display_message("'KEYS' command don\'t allow paramaters")
            return
        # call the get_key method in modle
        result = self.model.get_keys()

        # display diferent message depends on the current data dictionary
        self.view.display_message_by_type(result)

    # dis play all the members of a input key
    # the command format is "members key"in any case, with no more or less params
    def members(self, command_params: list):
        # handle incorect input format, exp: "members" or "mambers foo 123"
        if len(command_params) != 1:
            self.view.display_message("Please specify which key's members you want to see.")
            return
        # get the key user want check for members
        key = command_params[0]
        # call the method in model get members of provided key
        result = self.model.get_members(key)
        # display message depends on what response get back from model
        self.view.display_message_by_type(result)
    
    # add input member to the value set of the input key
    # the command format is "add key value"in any case, with no more or less params
    def add(self, command_params: list):
        # handle incorrect input exp:"add 1" "add" "add 2 3 344"
        if len(command_params) != 2:
            self.view.display_message("Please enter one key and one value after 'ADD' command")
            return
        # get the key and value from the params
        key = command_params[0]
        value = command_params[1]
        # call the add method in the model
        result = self.model.add(key, value)
        # notify the user if it is added for failed depends on response from model
        self.view.display_message(result)

    # remove a member from the provided key
    # the command format is "remove key value" in any case, with no more or less params
    def remove(self, command_params: list):
        # handle incorrect input exp:"remove 1" "remove" "remove 2 3 344"
        if len(command_params) != 2:
            self.view.display_message("Please specify WHICH member inside Witch key you want to remove")
            return
        # get key and value from params
        key = command_params[0]
        value = command_params[1]
        # call remove_member method from model
        result = self.model.remove_member(key, value)
        # display message depends on model response
        self.view.display_message(result)

    # remove all members from a provided key
    # the command format is "removeall key" in any case, with no more or less params
    def remove_all(self, command_params: list):
        # handle incorrect input exp:"removeall" "removeall foo ,"
        if len(command_params) != 1:
            self.view.display_message("Please specify WHICH key you want to remove")
            return
        # get key from the params
        key = command_params[0]
        # call remove_key method from model
        result = self.model.remove_key(key)
        # display message depends on model response
        self.view.display_message(result)
    
    # remove all key and members in the model data dictionary
    # the command format is "clear" in any case, with no more or less params
    def clear_all(self, command_params: list):
         # handle incorrect input exp:"clear foo" 
        if len(command_params) != 0:
            self.view.display_message("'CLEAR' command don\'t allow paramaters")
            return
        # call the clear_all method from model
        result = self.model.clear_all()
        # display message depends on the model response
        self.view.display_message(result)
    
    # display if a key is exist in data dictionary
    # the command format is "keyexists" in any case, with no more or less params
    def key_exist(self, command_params: list):
        # handle incorrect input exp:"keyexists foo" 
        if len(command_params) != 1:
            self.view.display_message("Please specify witch key you want check existence")
            return
        # get the key from params
        key = command_params[0]
        # call the is_key_exist method from model
        result = self.model.is_key_exist(key)
        # display message depends on the model response
        self.view.display_message_by_type(result)

    # display if input member is exist in the input key
    # the command format is "memberexists foo bar" in any case, with no more or less params
    def member_exist(self, command_params: list):
        # handle incorrect input exp:"memberexists foo" "memberexists foo bar baz"
        if len(command_params) != 2:
            self.view.display_message("Please specify witch member in witch key you want check existence")
            return
        # gey the key and member user want check from params
        key = command_params[0]
        value = command_params[1]
        # call is_member_exist from model
        result = self.model.is_member_exist(key, value)
        # display message depends on the model response
        self.view.display_message_by_type(result)

    # display all members in data dictionary
    # the command format is "allmembers" in any case, with no more or less params
    def all_members(self, command_params: list):
        # handle incorrect input exp:"allmembers 123,"
        if len(command_params) != 0:
            self.view.display_message("'ALLMEMBERS' command don\'t allow paramaters ")
            return
        # call get_all_members method from model
        result = self.model.get_all_members()
        # display message depends on the model response
        self.view.display_message_by_type(result)

    # display all members with it's key in data dictionary
    # the command format is "items" in any case, with no more or less params
    def all_items(self, command_params: list):
        # handle incorrect input exp:"items 123,"
        if len(command_params) != 0:
            self.view.display_message("'ALLMEMBERS' command don\'t allow paramaters")
            return
        # call get_items method from model
        result = self.model.get_items()
        # display message depends on the model response
        self.view.display_message_by_type(result)
        
    # Exit the program 
    # the command format is "exit" in any case, with no more or less params
    def exit_app(self, command_params: list):
        # handle incorrect input exp:"exit 123,"
        if len(command_params) != 0:
            self.view.display_message("'EXIT' command don\'t allow paramaters ")
            return
        # display a good bye message
        self.view.display_message("\n\nExiting application. Goodbye!")
        # quit the program
        sys.exit(0)

    # main program loop, keep running until user enter exit command or press ctrl+C
    def run(self):
        # try keep running the app as long as ctrl+c not pressed 
        try:
            # keep running the loop until "exist" command enterd
            while True:
                # get input from user by get_input method from view class
                user_input = self.view.get_input("\nPlease enter command\n")
                # if user didn't enter anything or white space(view handle it),skip current loop and prompt quesiton again
                if not user_input:
                    continue
                # conver user input in to a list to separate each command detail
                # if user enter multiple space , this list will contain empty element
                command = user_input.split(" ")
                # treat first word(element) from input as command_head
                command_head = command[0].upper()
                # the rest of words are command_params 
                # remove emtpy element(user enter multyple space between words)
                command_params = [word for word in command[1:] if word]

                # check if the command_head is a valid command in program
                if command_head in self.command_heads:
                    # if command_head is valid, call the corresponding method defined in command_heads dictionary
                    # pass the rest of user input as command_params into the method for next step 
                    self.command_heads[command_head](command_params)
                else:
                    # if the command is not in command_heads dictionary, display massage notify user invalid command
                    self.view.display_message("Invalid command...")
        # handle user press ctrl+c force program quit
        except KeyboardInterrupt:
            # this will triger when user user keyboard force quit program
            self.view.display_message("\n\nExiting application. Goodbye!")
            sys.exit(0)
