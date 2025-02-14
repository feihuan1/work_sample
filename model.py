import os

class Model:

    def __init__(self, data_file  = "data.txt"):
        self.DATA_FILE = data_file 
        self.data = {}
        self.load_data()

    def get_keys(self):
        keys = self.data.keys()

        if len(keys) == 0:
            return "(empty set)"
        return list(keys)

    def get_members(self, key: str):
        if not self.is_key_exist(key):
            return "ERROR, key does not exist."
        if not list(self.data[key]):
            return "ERROR: No members found in this key."
        
        return list(self.data[key])
    
    def add(self, key: str, value: str):
        if not self.is_key_exist(key):
            self.data[key] = set()

        if value in self.data[key]: 
            return "ERROR, member already exists for key"
        
        self.data[key].add(value)
        self.save_data()
        return "Added"
    
    def remove_member(self, key: str, value: str):
        if not self.is_key_exist(key):
            return "ERROR, key does not exist"
        
        if not self.is_member_exist(key, value):
            return "ERROR, member does not exist"
        
        self.data[key].remove(value)
        self.save_data()
        return "Removed"

    def remove_key(self, key: str):
        if not self.is_key_exist(key):
            return "ERROR, key does not exist"
        
        del self.data[key]
        self.save_data()
        return "Removed"

    def clear_all(self):
        if not self.data:
            return "ERROR, The dictionary is already empty."
        
        self.data.clear()
        self.save_data()
        return "Cleared"

    def is_key_exist(self, key: str):
        if key in self.data:
            return True
        else: 
            return False
    
    def is_member_exist(self, key: str, value: str):
        if not self.is_key_exist(key):
            return "ERROR, key does not exist."
        
        if value not in self.data[key]:
            return False
        else: 
            return True
        
    def get_all_members(self):
        if len(self.data.keys()) == 0:
            return "ERROR: No members found."
        
        result = []
        values = self.data.values()

        for value_set in values:
            result += list(value_set)
        return result

    def get_items(self):
        if not self.data:
            return "ERROR: No items found."
        
        result = []

        for key in self.data.keys():
            for value in self.data[key]:
                result.append(f"{key}: {value}")

        return result

    def save_data(self):
        with open(self.DATA_FILE, "w") as file:
            for key, values in self.data.items():
                file.write(f"{key}:{','.join(values)}\n")

    def load_data(self):
        if not os.path.exists(self.DATA_FILE):
            open(self.DATA_FILE, "w").close()
            return

        with open(self.DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                
                if ":" not in line:
                    print(f"WARNING: Ignoring invalid item in data file: {line}")
                    continue
                
                key, values = line.split(":", 1) 
                key = key.strip()
                values = values.strip()

                if not key:
                    print(f"WARNING: Ignoring item with missing key: {line}")
                    continue

                self.data[key] = set(values.split(",")) if values else set()