N = None

class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.winner = None
        self.current_player = "X" 
        self.game_array = [N, N, N,
                           N, N, N,
                           N, N, N]

    # Print Welcome and Instruction grid
    def welcome(self):
        print("\n=== NEO TIC-TAC-TOE ===")
        print("To play, enter the number of the cell (1-9):")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("\nLet's start! Player X goes first.\n")

    def print_grid(self):
        display_array = [cell if cell in ("X", "O") else '-' for cell in self.game_array]
        
        # Print the grid in 3x3 format
        print(f" {display_array[0]} | {display_array[1]} | {display_array[2]} ")
        print("-----------")
        print(f" {display_array[3]} | {display_array[4]} | {display_array[5]} ")
        print("-----------")
        print(f" {display_array[6]} | {display_array[7]} | {display_array[8]} ")



    # UPDATE GRID: Updates the array and switches turns
    def update_grid(self, position):
        # 1. Update the array with the current player's symbol (X or O)
        self.game_array[position] = self.current_player
        # 2. Switch the turn automatically
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

   

    def game_process(self):
       while True:
            try:
                self.inp = int(input(f"Player {self.current_player} choose a cell (1 - 9): "))
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
                continue
            break

    def check_winner(self):
      pass

   
   

    # Print caption: Player's turn or WINNER or DRAW
    def print_caption(self):
        if self.winner:
            print(f"\n!!! {self.winner} WINS !!!")
        else:
            print(f"\nPlayer {self.current_player}'s turn.")
    


class Game:
    def __init__(self):
        self.tic_tac_toe = TicTacToe(self)

    def run(self):
        self.tic_tac_toe.welcome()
        while True:
            self.tic_tac_toe.print_grid()
            self.tic_tac_toe.print_caption()

            if self.tic_tac_toe.winner:

                break
            
            # Check for draw (board full and no winner)
            if N not in self.tic_tac_toe.game_array and not self.tic_tac_toe.winner:
                print("\nIt's a DRAW!")
                break

            self.tic_tac_toe.game_process()
            self.tic_tac_toe.check_winner()


if __name__ == '__main__':
    game = Game()
    game.run()