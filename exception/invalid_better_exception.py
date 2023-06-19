

class InvalidBetterException(Exception):

    def __init__(self, obj):
        self.message = f"The Better {obj} is not valid!"
        super().__init__(self.message)