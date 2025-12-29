from src.model.board import Board
from src.model.rules import GameRules
from src.model.constants import X, O

class GameController:
    def __init__(self, view, player_x, player_o, board, rules):
        self.view = view
        self.board = board
        self.rules = rules
        self.player_x = player_x
        self.player_o = player_o
        self.current_player = player_x

    def run(self):
        self.view.display_welcome()

        while True:
            # display current board
            self.view.display_board(self.board.grid)
            self.view.display_turn(self.current_player.symbol)

            # Get input based on current player
            # If current player is AI, call get_move(board). If current player is human, call input from view
            move = self.current_player.get_move(self.board)

            # Update module
            if self.board.update_cell(move, self.current_player.symbol):
                winner = GameRules.check_winner(self.board.grid)
                if winner:
                    self.view.display_board(self.board.grid)
                    self.view.display_winner(winner)
                    break

                if GameRules.is_draw(self.board.grid):
                    self.view.display_board(self.board.grid)
                    self.view.display_draw()
                    break

                self.current_player = self.player_o if self.current_player == self.player_x else self.player_x
                self.view.clear_screen()
            else:
                print("The cell has been filled. Please choose again!")
