import os
from src.model.constants import X, O

class ConsoleView:

  
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


    def display_welcome():
        print("\n=== NEO TIC-TAC-TOE ===")
        print("To play, enter the number of the cell (1-9):")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("\nLet's start! Player X goes first.\n")
    
    
    def display_board(game_array):
        display_array = [cell if cell in ("X", "O") else '-' for cell in game_array]
        
        # Print the grid in 3x3 format
        print(f" {display_array[0]} | {display_array[1]} | {display_array[2]} ")
        print("-----------")
        print(f" {display_array[3]} | {display_array[4]} | {display_array[5]} ")
        print("-----------")
        print(f" {display_array[6]} | {display_array[7]} | {display_array[8]} ")

    
    def display_turn(player_symbol):
        print(f"\nPlayer {player_symbol}'s turn.")

    
    def display_winner(winner):
        print(f"\n{winner} WINS !!!")

    
    def display_draw():
        print("It's a DRAW!")

    
    def display_message(message):
        print(message)

