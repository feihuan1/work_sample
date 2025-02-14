class View:
    @staticmethod
    def get_input(prompt: str):
        return input(prompt).strip()

    @staticmethod
    def display_message(message: str):
        print(message)