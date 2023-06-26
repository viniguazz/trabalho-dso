
class NoMenuSelected(Exception):
    
    def __init__(self):
        self.message = f"No Menu Selected"
        super().__init__(self.message)