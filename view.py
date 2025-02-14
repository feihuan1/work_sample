class View:
    @staticmethod
    def get_input(prompt: str):
        return input(prompt).strip()

    @staticmethod
    def display_message(message: str):
        message = str(message)
        if not message:
            print("No message availiable")
            return
        print(message) 
    
    @staticmethod
    def display_message_by_type(message: list[str] | bool | str):
        if isinstance(message, list):
            is_no_content = True
            for item in message:
                if str(item.strip()):
                    is_no_content = False
            if is_no_content:
                print("No items found.")
                return
            for idx, item in enumerate(message, start=1):
                item = str(item.strip())
                if not item:
                    continue
                print(f"{idx}) {item}")
        elif isinstance(message, bool):
            print(str(message).lower())
        elif isinstance(message, str):
            print(message)
        else:
            raise TypeError(f"Invalid type for message: {type(message)}")