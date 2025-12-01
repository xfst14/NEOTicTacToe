from random import randint
N = None

class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.winner = None
        self.player = "X"

        self.game_array = [N, N, N, N, N, N, N, N, N]

    def game_process(self):
     while True:
            try:
                self.inp = int(input(f"Player {self.player} choose a cell (1 - 9): "))
                index = self.inp - 1
                # Check valid input range
                if self.int < 1 and self.inp > 9:
                    print("Invalid input. Please enter a number between 1 and 9")
                    continue
                # Check occupied position
                if self.game_array[index] is not None:
                    print("Position already taken. Try again!")
                    continue
                self.game_array[index] = self.player
                self.player = "O" if self.player == "X" else "X"
            except ValueError:
                print("Invalid input. Please enter a number")
