class Stringer(str):
    def __init__(self):
        super().__init__()
        self.raw_data = None

    def load_raw_data(self, address):
        """opens txt file of date details in not formated string from base file, address is file path"""
        with open(address, mode='r') as file:
            return file.read()
