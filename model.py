

class Model:
    def __init__(self):
        self.input_str: str = ""

    @property
    def data(self):
        return self.input_str
    
    @data.setter
    def data(self, value):
        self.input_str = value

        