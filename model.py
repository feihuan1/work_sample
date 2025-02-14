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
        if key not in self.data:
            return "ERROR, key does not exist."
        # give the set a order by convert it to a list
        return list(self.data[key])
    
    def add(self, key: str, value: str):
        if key not in self.data:
            self.data[key] = set()
        if value in self.data[key]: 
            return "ERROR, member already exists for key"
        self.data[key].add(value)
        self.save_data()
        return "Added"
    

    def remove_member(self, key: str, value: str):
        if key not in self.data:
            return "ERROR, key does not exist"
        if value not in self.data[key]:
            return "ERROR, member does not exist"
        self.data[key].remove(value)
        self.save_data()
        return "Removed"

    def remove_key(self, key: str):
        if key not in self.data:
            return "ERROR, key does not exist"
        del self.data[key]
        self.save_data()
        return "Removed"

    def clear_all(self):
        self.data.clear()
        self.save_data()
        return "Cleared"

    def save_data(self):
        with open(self.DATA_FILE, "w") as file:
            for key, values in self.data.items():
                file.write(f"{key}:{','.join(values)}\n")

    def load_data(self):
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "r") as file:
                for line in file:
                    key, values = line.strip().split(":")
                    self.data[key] = set(values.split(",")) if values else set()