from pvp import TicTacToe, N
from pve import TicTacToe2, TicTacToe3

class Game:
    def __init__(self):
        while True:
            print("Game modes:")
            print("1. Human vs Human ")
            print("2. Human vs Bot (Easy) ")
            print("3. Human vs Bot (Hard).")
            
            try:
                game_mode = int(input("Choose game mode: "))
                if 1 <= game_mode <= 3:
                    break
                else:
                    print("\nInvalid input. Please enter a number between 1 and 3.")
            except ValueError:
                print("\nInvalid input. Please enter a number between 1 and 3.")

        if game_mode == 1:
            self.game_mode = 1
            self.tic_tac_toe = TicTacToe(self)
        elif game_mode == 2:
            self.game_mode = 2
            self.tic_tac_toe = TicTacToe2(self)
        elif game_mode == 3:
            self.game_mode = 3
            self.tic_tac_toe = TicTacToe3(self)

    def run(self):
        self.tic_tac_toe.clear_screen()  # Clear screen at start
        self.tic_tac_toe.welcome()
        # SINGLE-GAME LOOP: Handles one complete game (all turns until win/draw)
        # This loop continues until someone wins or it's a draw
        while True:

            self.tic_tac_toe.print_grid()
            self.tic_tac_toe.print_caption()

            # If someone won, break out of the loop (end this game)
            if self.tic_tac_toe.winner:
                break
        
            # If board is full and no winner, it's a draw - break out of loop
            if N not in self.tic_tac_toe.game_array and not self.tic_tac_toe.winner:
                print("\nIt's a DRAW!")
                break

            # Process one turn: get input, update board, switch players
            self.tic_tac_toe.game_process()
            # Check if this move created a winner
            self.tic_tac_toe.check_winner()
            # Clear screen after move is made, so next iteration shows clean display
            self.tic_tac_toe.clear_screen()
            # Loop back to top to show updated board and get next turn