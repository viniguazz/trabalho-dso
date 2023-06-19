

class InvalidResultException(Exception):

    def __init__(self, obj):
        self.message = f"The result {obj} is not valid!"
        super().__init__(self.message)