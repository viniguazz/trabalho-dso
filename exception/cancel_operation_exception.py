

class CancelOperationException(Exception):
    
    def __init__(self):
        self.message = f"The Operation is cancelled!"
        super().__init__(self.message)