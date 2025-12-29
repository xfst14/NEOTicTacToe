import random
from .base_ai import BaseAI

class RandomAI(BaseAI):
    def get_move(self, board):
        available = board.get_free_indices()
        if not available:
            return None
        return random.choice(available)