

class InvalidNativeTypeException(Exception):

    def __init__(self, obj, desired):
        self.message = f"The object {obj} is of the desired native type {desired}!"
        super().__init__(self.message)