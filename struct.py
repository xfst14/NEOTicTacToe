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
        print("To play, enter the number of the cell (0-8):")
        print(" 0 | 1 | 2 ")
        print("-----------")
        print(" 3 | 4 | 5 ")
        print("-----------")
        print(" 6 | 7 | 8 ")
        print("\nLet's start! Player X goes first.\n")

    def check_winner(self):
        pass

    # Player input and check valid
    def game_process(self):
        # TEMPORARY: Just to stop the infinite loop 
        input(f"Simulating Player {self.current_player}'s turn... Press Enter to continue.")
        
        # Simulating a turn switch 
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    # Print caption: Player's turn or WINNER or DRAW
    def print_caption(self):
        if self.winner:
            print(f"\n!!! {self.winner} WINS !!!")
        else:
            print(f"\nPlayer {self.current_player}'s turn.")


    def print_grid(self):
        # Convert None values to '-' for display
        display_array = [cell if cell is not None else '-' for cell in self.game_array]
        
        # Print the grid in 3x3 format
        print(f" {display_array[0]} | {display_array[1]} | {display_array[2]} ")
        print("-----------")
        print(f" {display_array[3]} | {display_array[4]} | {display_array[5]} ")
        print("-----------")
        print(f" {display_array[6]} | {display_array[7]} | {display_array[8]} ")



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