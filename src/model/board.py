from src.model.constants import N

class Board:
    def __init__(self, size = 3):
        self.size = size
        self.grid = [N] * (self.size * self.size)

    def update_cell(self, index, symbol):
        if 0 <= index < len(self.grid) and self.grid[index] == N:
            self.grid[index] = symbol
            return True
        return False
    
    def get_free_indices(self):
        return [i for i, val in enumerate(self.grid) if val == N]
    
    def reset(self):
        self.grid = [N] * (self.size * self.size)