

class InvalidGameException(Exception):

    def __init__(self, obj):
        self.message = f"The game {obj} is not valid!"
        super().__init__(self.message)