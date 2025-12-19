# Import the 'os' module - this gives access to operating system functions
import os
import random
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

    def clear_screen(self):
        # Check what operating system we're running on
        if os.name == 'nt':  # 'nt' means Windows
            # Run the Windows clear screen command
            os.system('cls')  # This executes "cls" in the terminal
        else:  # Mac, Linux, or other Unix-based systems
            # Run the Unix/Linux/Mac clear screen command
            os.system('clear')  # This executes "clear" in the terminal

    def print_grid(self):
        display_array = [cell if cell in ("X", "O") else '-' for cell in self.game_array]
        
        # Print the grid in 3x3 format
        print(f" {display_array[0]} | {display_array[1]} | {display_array[2]} ")
        print("-----------")
        print(f" {display_array[3]} | {display_array[4]} | {display_array[5]} ")
        print("-----------")
        print(f" {display_array[6]} | {display_array[7]} | {display_array[8]} ")



    def game_process(self):
        while True:
            try:
                self.inp = int(input(f"Player {self.current_player} choose a cell (1 - 9): "))
                index = self.inp - 1
                # Check valid input range
                if self.inp < 1 or self.inp > 9:
                    print("Invalid input. Please enter a number between 1 and 9")
                    continue
                # Check occupied position
                if self.game_array[index] is not None:
                    print("Position already taken. Try again!")
                    continue
                self.game_array[index] = self.current_player
                if self.current_player == "X":
                    self.current_player = "O"
                else: self.current_player = "X"
            except ValueError:
                print("Invalid input. Please enter a number")
                continue
            break

    def check_winner(self, board=None):
        # If no board provided, use the actual game board and update self.winner
        # If board is provided, just check and return the winner without modifying state
        check_board = board if board is not None else self.game_array
        
        # Win combination
        win_positions = [
            [0,1,2], # Row
            [3,4,5],
            [6,7,8],
            [0,3,6], # Column
            [1,4,7],
            [2,5,8],
            [0,4,8], # Diagonal
            [2,4,6]
        ]
        # Checking condition
        for position in win_positions:
            a, b, c = position
            if (check_board[a] == check_board[b] == check_board[c] 
                and check_board[a] is not None):
                winner = check_board[a]
                # Only modify self.winner if we're checking the actual game board
                if board is None:
                    self.winner = winner
                return winner
        return None
   

    # Print caption: Player's turn or WINNER or DRAW
    def print_caption(self):
        if self.winner:
            print(f"\n!!! {self.winner} WINS !!!")
        else:
            print(f"\n{self.current_player}'s turn.")
    

    # Re-define property for new game
    def reset(self):
        self.winner = None
        self.current_player = "X"
        self.game_array = [N, N, N,
                           N, N, N,
                           N, N, N]
        print("\nGame has been reset! Player X goes first.\n")
        
class TicTacToe2(TicTacToe): # Mode 2 (Player vs BotEZ) using random
    def __init__(self, game):
        super().__init__(game)
        self.human_player = "X"
        self.bot_player = "O"
        
    def game_process(self):
        if self.current_player == self.human_player:
            # Use the regular human input flow from the base class
            super().game_process()
        else:
            # Bot plays
            available = [i for i in range(9)
                         if self.game_array[i] is None]
            index = random.choice(available)
            print(f"Bot plays at position {index + 1}")
            self.game_array[index] = self.bot_player
            self.current_player = self.human_player
        
class TicTacToe3(TicTacToe):
    def __init__(self, game):
        super().__init__(game)
        self.human_player = "X"
        self.bot_player = "O"

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
            index = self.get_best_move()
            print(f"Bot plays at position {index + 1}")
            self.game_array[index] = self.bot_player
            self.current_player = self.human_player

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

if __name__ == '__main__':
    # MAIN MENU LOOP: after each game ends, return to main menu (mode selection)
    while True:
        game = Game()  # Choose game mode
        game.run()     # Play one full game with that mode

        # Ask if the player wants to go back to the main menu (choose mode again)
        while True:
            choice = input("\nReturn to main menu and play again? (y/n): ").strip().lower()
            if choice in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if choice != 'y':
            print("\nThanks for playing NEO TIC-TAC-TOE!")
            break