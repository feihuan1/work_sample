class View:
    @staticmethod
    def get_input(prompt: str):
        return input(prompt).strip()

    @staticmethod
    def display_message(message: str):
        print(message) 
    
    @staticmethod
    def display_message_by_type(msg_type: list[str] | bool | str):
        if isinstance(msg_type, list):
            if not msg_type:
                print("No items found.")
                return
            for idx, item in enumerate(msg_type, start=1):
                print(f"{idx}) {item}")
        elif isinstance(msg_type, bool):
            print(str(msg_type).lower())
        elif isinstance(msg_type, str):
            print(msg_type)
        else:
            raise TypeError(f"Invalid type for message: {type(msg_type)}")