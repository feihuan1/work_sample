import os
# Model manages the application's data and logic.
class Model:
    # make data_file changable for test and won't effect real data after test delete data file in tearDown() 
    def __init__(self, data_file  = "data.txt"):
        self.DATA_FILE = data_file 
        # a temp holder for the data file 
        self.data = {}
        # load the data from the file
        self.load_data()
    
    # get all the keys from data dictionary
    def get_keys(self):
        keys = self.data.keys()
        # notify empty set(dictionary) if not key in dictionary as requirement stated
        if len(keys) == 0:
            return "(empty set)"
        # if there is key, return it as a list 
        return list(keys)

    # get all values in value set by provided key
    def get_members(self, key: str):
        # handle key not exist
        if not self.is_key_exist(key):
            return "ERROR, key does not exist."
        # handle if the values are empty for the provided key
        if not list(self.data[key]):
            return "ERROR: No members found in this key."
        # return back the members set as a list
        return list(self.data[key])
    
    # add a member to value set for provided key or create a key value(set) pair if key not exist 
    def add(self, key: str, value: str):
        # if key not found, create the key and assign a empty set as value
        if not self.is_key_exist(key):
            self.data[key] = set()
        # if input value already in the set, give a error message
        if value in self.data[key]: 
            return "ERROR, member already exists for key"
        
        # add the value to the key
        self.data[key].add(value)
        # update the data.txt file
        self.save_data()
        # return a message notify the result
        return "Added"
    
    # remove a value(member) from value set for a key
    def remove_member(self, key: str, value: str):
        # handle if input key is not exist
        if not self.is_key_exist(key):
            return "ERROR, key does not exist"
        # handle the value user want remove is not existed in the key
        if not self.is_member_exist(key, value):
            return "ERROR, member does not exist"
        
        # remove the member from the value set
        self.data[key].remove(value)

        if not self.data[key]:
            del self.data[key]

        # update the data.txt file
        self.save_data()
        # return a message notify result
        return "Removed"

    # remove all member from value set for a input key, keep the key and set value as empty set
    def remove_key(self, key: str):
        # handle input key not exist in data
        if not self.is_key_exist(key):
            return "ERROR, key does not exist"
        # remove all existing member and the key
        del self.data[key]
        # update the data file
        self.save_data()
        # return a message notify result
        return "Removed"

    # delete everything from data
    def clear_all(self):
        # remove all keys and value from data dictionary
        self.data.clear()
        # clear the data.txt file
        self.save_data()
        # return a message notify result
        return "Cleared"

    # check if inpput key exist in data adn return resultas a boolean
    def is_key_exist(self, key: str):
        if key in self.data:
            return True
        else: 
            return False
    
    # check if a input member is exist in input key
    def is_member_exist(self, key: str, value: str):
        # handle if input key is not exist
        if not self.is_key_exist(key):
            return False
        # return boolean depends on if member is in the value set of input key
        if value not in self.data[key]:
            return False
        else: 
            return True
    
    # get all members in each key return it as a list
    def get_all_members(self):
        # handle if data dictionary is empty
        if not self.data:
            return "(empty set)"
        # initialize output as empty list
        result = []
        # create list of all value set
        values = self.data.values()
        # add each value set as a list append to the result
        for value_set in values:
            result += list(value_set)
        # return the result as a list
        return result

    # return all members in data dictionary with it's key as a list of string 
    def get_items(self):
        # handle if data dictionary is empty
        if not self.data:
            return "(empty set)"
        # initialize output as empty list
        result = []
        # loop through each key in data dictionary
        for key in self.data.keys():
            # loop through each member in that value set
            for value in self.data[key]:
                # append correct format provided in work sample in to output list
                result.append(f"{key}: {value}")
        # return back the list
        return result

    # save data to the data.txt file
    def save_data(self):
        # open the file or create data.txt file if it's not exist
        with open(self.DATA_FILE, "w") as file:
            # loop through each key value pair in data dictionary
            for key, values in self.data.items():
                # write into data.txt seperate key value with ':', seperate each value of key with ','
                file.write(f"{key}:{','.join(values)}\n")

    # load data form data.txt file into data dictionary, create the empty file if file is missing or manually deleted
    def load_data(self):
        # if file missing, create data.txt file
        if not os.path.exists(self.DATA_FILE):
            open(self.DATA_FILE, "w").close()
            return
        # open data.txt with read mode
        with open(self.DATA_FILE, "r") as file:
            # check each line
            for line in file:
                # skip white space
                line = line.strip()
                # handle user manually type in-correct format of data in to file
                if ":" not in line:
                    print(f"WARNING: Ignoring invalid item in data file: {line}")
                    continue
                # seperate key and value with ":"
                key, values = line.split(":", 1) 
                # remove white space for key and value
                key = key.strip()
                values = values.strip()
                # handle if user type a empty key or space as key in data file
                if not key:
                    print(f"WARNING: Ignoring item with missing key: {line}")
                    continue
                # set up data dictionary with key and value as set
                self.data[key] = set(values.split(",")) if values else set()