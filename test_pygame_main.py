import pygame
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

    while True:
        # Appear main menu
        mode = run_menu(screen, clock)
        if mode == "QUIT":
            break

        board = Board()
        rules = GameRules()
        input_handler = PygameInputHandler(screen)

        p1 = PygameHumanPlayer("X")
        if mode == 1: 
            p2 = PygameHumanPlayer("O")
        elif mode == 2:
            p2 = RandomAI("O")
        else:
            p2 = MinimaxAI("O")

        # Run the match
        controller = PygameController(screen, board, rules, p1, p2, input_handler)
        result = controller.run_game()
        reset_choice = run_reset(screen, clock, mode)
        if result == "QUIT": 
            break
        elif reset_choice == "MENU":
            continue
        
        pygame.quit()

if __name__ == "__main__":
    main()