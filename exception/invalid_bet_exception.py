

class InvalidBetException(Exception):
    
    def __init__(self, obj):
        self.message = f"The Bet {obj} is not valid!"
        super().__init__(self.message)