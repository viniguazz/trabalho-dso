from abc import ABC, abstractmethod
import PySimpleGUI as sg

class AbstractView(ABC):
    
    @abstractmethod
    def __init__(self):
        self.__window = None
        self.init_components()

    def display_options(self):
        pass

    def close(self):
        pass
    
    def open(self):
        pass

    def display_message(self, message):
        sg.popup("",message)

    def init_components(self):
        pass