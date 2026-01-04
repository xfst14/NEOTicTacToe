import pygame
from src.model.constants import X, O
from src.UI.pygame_board import draw_board
from src.model.rules import GameRules

class PygameController:
    def __init__(self, screen, board, rules, player_x, player_o, input_handler):
        self.screen = screen
        self.board = board
        self.rules = rules
        self.player_x = player_x
        self.player_o = player_o
        self.input_handler = input_handler
        self.current_player = player_x
        self.game_over = False
        self.winner = None

    def handle_turn(self):
        move = None
        if self.game_over:
            return
        
        else:
            move = self.current_player.get_move(self.board)

        if move is not None:
            self.execute_move(move)

    def execute_move(self, move):
        # update board.grid and check game event
        if self.board.update_cell(move, self.current_player.symbol):
            self.winner = GameRules.check_winner(self.board.grid)
            if self.winner or GameRules.is_draw(self.board.grid):
                self.game_over = True
            else:
                # Switch turn
                self.current_player = self.player_o if self.current_player == self.player_x else self.player_x

    def run_game(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            # Draw UI
            self.screen.fill((8, 13, 51))
            draw_board(self.screen, self.board.grid)

            # Execute game events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "QUIT"
                
                # Execute player mouse click
                if not self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
                    if not hasattr(self.current_player, 'get_move'):
                        pos = pygame.mouse.get_pos()
                        move = self.input_handler.get_cell_from_pos(pos)
                        if move is not None:
                            self.execute_move(move)

            # AI's turn (if game mode is AI)
            if not self.game_over and hasattr(self.current_player, 'get_move'):
                self.handle_turn()

            # Check to end game loop
            if self.game_over:
                pygame.display.flip()
                pygame.time.delay(1000)
                return "GAME OVER"
            
            pygame.display.flip()
            clock.tick(60)
