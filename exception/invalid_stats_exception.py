

class InvalidStatsException(Exception):

    def __init__(self, obj):
        self.message = f"The Stats {obj} is not valid!"
        super().__init__()