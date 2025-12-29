from abc import ABC, abstractmethod

class BaseAI(ABC):
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def get_move(self, board):
        pass