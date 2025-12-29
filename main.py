from src.model.board import Board
from src.model.rules import GameRules
from src.model.constants import X, O
from src.UI.console_view import ConsoleView
from src.UI.input_handler import InputHandler
from src.ai.random_ai import RandomAI
from src.ai.minimax_ai import MinimaxAI
from src.controllers.game_controller import GameController

class HumanPlayer:
    def __init__(self, symbol, input_handler):
        self.symbol = symbol
        self.input_handler = input_handler

    def get_move(self, board):
        return self.input_handler.get_move()
    

def main():
    view = ConsoleView()
    input_handler = InputHandler()
    rules = GameRules()

    while True:
        view.clear_screen()
        view.display_welcome()

        game_mode = input_handler.get_game_mode()

        # Initial player based on game_mode
        player_x = HumanPlayer(X, input_handler)

        if game_mode == 1:
            player_o = HumanPlayer(O, input_handler)
        elif game_mode == 2:
            player_o = RandomAI(O)
        else:
            player_o = MinimaxAI(O)

        board = Board()
        game = GameController(view, player_x, player_o, board, rules)

        game.run()

        if input("\nDo you want to play again? (y/n): ").lower() != 'y':
            print("THANK YOU FOR PLAYING!!!")
            break

if __name__ == '__main__':
    main()
