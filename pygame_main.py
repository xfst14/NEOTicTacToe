import pygame
import sys
from src.model.board import Board
from src.model.rules import GameRules
from src.UI.pygame_menu import run_menu, run_reset
from src.UI.pygame_input_handler import PygameInputHandler
from src.controllers.pygame_controller import PygameController
from src.AI.random_ai import RandomAI
from src.AI.minimax_ai import MinimaxAI

class PygameHumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption("NEO TIC-TAC-TOE")
    clock = pygame.time.Clock()

    input_handler = PygameInputHandler(screen)
    
    current_mode = None
    
    while True:
        # Appear main menu
        if current_mode is None:
            score_x = 0
            score_y = 0
            current_mode = run_menu(screen, clock)
            if current_mode == "QUIT":
                break

        board = Board()
        rules = GameRules()
        

        p1 = PygameHumanPlayer("X")
        if current_mode == 1: 
            p2 = PygameHumanPlayer("O")
        elif current_mode == 2:
            p2 = RandomAI("O")
        else:
            p2 = MinimaxAI("O")

        # Run the match
        controller = PygameController(screen, board, rules, p1, p2, input_handler, score_x, score_y)
        result = controller.run_game()
        if result == "QUIT": break

        # Update player score after the match
        if controller.winner == "X":
            score_x += 1
        elif controller.winner == "Y":
            score_y += 1 
            
        # Reset menu after finishing the game
        reset_choice = run_reset(screen, clock, current_mode)
        if reset_choice == "RESTART":
            continue
        elif reset_choice == "MENU":
            current_mode = None
        elif reset_choice == "QUIT":
            break
        
    pygame.quit()

if __name__ == "__main__":
    main()