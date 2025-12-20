from pvp import TicTacToe, N
import random
        
class TicTacToeBot(TicTacToe):
    def __init__(self, game, game_mode):
        super().__init__(game)
        self.human_player = "X"
        self.bot_player = "O"
        self.game_mode = game_mode

    def minimax(self, mini_grid, depth, is_max):
        # Check for winner on the current board state (pass mini_grid to avoid modifying game state)
        winner = self.check_winner(mini_grid)
        # If bot (O) wins, return positive score (adjusted by depth for faster wins)
        if winner == "O":
            return 1000 - depth
        # If human (X) wins, return negative score (adjusted by depth)
        elif winner == "X":
            return -1000 + depth
        # If board is full and no winner, it's a draw
        elif N not in mini_grid:
            return 0

        if is_max:
            best_score = -1000
            for i in range(9):
                if mini_grid[i] == N:
                    mini_grid[i] = self.bot_player
                    score = self.minimax(mini_grid, depth + 1, False)
                    mini_grid[i] = N
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = 1000
            for i in range(9):
                if mini_grid[i] == N:
                    mini_grid[i] = self.human_player
                    score = self.minimax(mini_grid, depth + 1, True)
                    mini_grid[i] = N
                    best_score = min(score, best_score)
            return best_score
    
    # Get Bot input
    def get_best_move(self):
        best_score = -1000
        best_move = None
        
        for i in range(9):
            if self.game_array[i] == N:
                # Create a copy of main board
                mini_grid = self.game_array.copy()
                # Bot simulate the move
                mini_grid[i] = self.bot_player
                # Evaluate the move
                score = self.minimax(mini_grid, 0, False)
                # Choose the best move
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def game_process(self):
        if self.current_player == self.human_player:
            # Use the regular human input flow from the base class
            super().game_process()
        else:
            # Bot plays
            if self.game_mode == 2:
                available = [i for i in range(9)
                         if self.game_array[i] is None]
                index = random.choice(available)
            else:
                index = self.get_best_move()

            print(f"Bot plays at position {index + 1}")
            self.game_array[index] = self.bot_player
            self.current_player = self.human_player