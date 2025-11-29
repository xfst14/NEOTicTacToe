N = None

class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.winner = None

        self.game_array = [N, N, N,
                           N, N, N,
                           N, N, N]

    # Print Welcome and Instruction grid
    def welcome(self):
        pass

    def check_winner(self):
        pass

    # Player input and check valid
    def game_process(self):
        pass

    # Print caption: Player's turn or WINNER or DRAW
    def print_caption(self):
        pass

    def print_grid(self):
        pass



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

            self.tic_tac_toe.game_process()
            self.tic_tac_toe.check_winner()


if __name__ == '__main__':
    game = Game()
    game.run()