from .base_ai import BaseAI
from src.model.rules import GameRules
from src.model.constants import X, O, N

class MinimaxAI(BaseAI):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.opponent = X if symbol == O else O
    
    def minimax(self, board, depth, is_max):
        # Check for winner on the current board state (pass mini_grid to avoid modifying game state)
        winner = GameRules.check_winner(board.grid)
        # If bot (O) wins, return positive score (adjusted by depth for faster wins)
        if winner == "O":
            return 1000 - depth
        # If human (X) wins, return negative score (adjusted by depth)
        elif winner == "X":
            return -1000 + depth
        # If board is full and no winner, it's a draw
        elif GameRules.is_draw(board.grid):
            return 0

        if is_max:
            best_score = -1000
            for move in board.get_free_indices():
                board.update_cell(move, self.symbol)
                score = self.minimax(board, depth+1, False)
                board.grid[move] = N
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = 1000
            for move in board.get_free_indices():
                board.update_cell(move, self.opponent)
                score = self.minimax(board, depth+1, True)
                board.grid[move] = N
                best_score = min(score, best_score)
            return best_score
        
    # Get Bot input
    def get_move(self, board):
        best_score = -1000
        best_move = None
        
        for move in board.get_free_indices():
            board.grid[move] = self.symbol
            score = self.minimax(board, 0, False)
            board.grid[move] = N

            if score > best_score:
                best_score = score
                best_move = move
        return best_move