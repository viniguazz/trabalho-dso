

class InvalidPlayerException(Exception):

    def __init__(self, obj):
        self.message = f"The player {obj} is not valid!"
        super().__init__(self.message)