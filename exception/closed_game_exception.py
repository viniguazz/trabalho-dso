

class ClosedGameException(Exception):
    
    def __init__(self, game_name, game_id):
        self.message = f"The game {game_name} (id: {game_id}) has already been closed."
        super().__init__(self.message)