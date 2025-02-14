#displays data and interacts with  user.
class View:

    # prompt a question and get the anser without wwhitespace
    @staticmethod
    def get_input(prompt: str):
        return input(prompt).strip()

    # display a message in console and avoid type error
    @staticmethod
    def display_message(message: str):
        # conver message to string in case theres wrong type
        message = str(message)
        # handle empty string case
        if not message:
            print("No message availiable")
            return
        print(message) 
    
    # display message depends on which type of response get back from model
    @staticmethod
    def display_message_by_type(message: list[str] | bool | str):
        # handle list response type
        if isinstance(message, list):
            # handle empty list or list with all empty string element
            is_no_content = True
            for item in message:
                if str(item.strip()):
                    is_no_content = False
            if is_no_content:
                print("No items found.")
                return
            # if there is any element contant data, display it 
            for idx, item in enumerate(message, start=1):
                item = str(item.strip())
                # skip empty string element
                if not item:
                    continue
                # pring the format as required in work sample
                print(f"{idx}) {item}")
        # handle boolean response
        elif isinstance(message, bool):
            # print lower case string as requirement states
            print(str(message).lower())
        # dis play a string if input is a string
        elif isinstance(message, str):
            print(message)
        # handle edge case if input is a diferent type
        else:
            raise TypeError(f"Invalid type for message: {type(message)}")