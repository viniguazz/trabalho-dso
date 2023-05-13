from better_view import BetterView
from better import Better

class BetterControler():
    def __init__(self, system_controller):
        betters = []
        self.__system_controller = system_controller
        self.__better_view = BetterView()
