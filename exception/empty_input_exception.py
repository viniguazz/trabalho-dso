
class EmptyInputException(Exception):
    
    def __init__(self, game_name, game_id):
        self.message = f"There is empty fields, please input data."
        super().__init__(self.message)