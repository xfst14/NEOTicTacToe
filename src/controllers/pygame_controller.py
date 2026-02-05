import pygame
import random
from src.model.constants import X, O
from src.UI.pygame_board import draw_board, draw_status, draw_click_to_continue, draw_score, get_board_dimensions
from src.model.rules import GameRules
from src.UI.retro_effects import (
    RetroBackground, ScreenShake, 
    NEON_CYAN, NEON_YELLOW
)

# Background color
SCREENBLUE = (8, 13, 51)


class PygameController:
    def __init__(self, screen, board, rules, player_x, player_o, input_handler, score_x, score_o, sound_manager=None):
        self.screen = screen
        self.board = board
        self.rules = rules
        self.player_x = player_x
        self.player_o = player_o
        self.score_x = score_x
        self.score_o = score_o
        self.sound_manager = sound_manager
        self.input_handler = input_handler
        self.current_player = player_x
        self.game_over = False
        self.winner = None
        self.ai_move_pending = None
        
        # Initialize retro effects
        width, height = screen.get_size()
        self.retro_bg = RetroBackground(width, height)
        self.screen_shake = ScreenShake()
        
        # Game end animation state
        self.end_animation_done = False
        self.end_flash_timer = 0
        
        # AI move delay
        self.ai_delay = random.uniform(0.3, 0.8)  # Delay in seconds before AI moves
        self.ai_delay_timer = 0
        self.ai_waiting = False

    def handle_turn(self, dt):
        if self.game_over:
            return
        
        # Start waiting if not already
        if not self.ai_waiting:
            self.ai_waiting = True
            self.ai_delay_timer = 0
            # Pre-calculate AI move while waiting
            if self.ai_move_pending is None:
                self.ai_move_pending = self.current_player.get_move(self.board)
            return
        
        # Update delay timer
        self.ai_delay_timer += dt
        
        # Execute move after delay
        if self.ai_delay_timer >= self.ai_delay and self.ai_move_pending is not None:
            self.execute_move(self.ai_move_pending)
            self.ai_move_pending = None
            self.ai_waiting = False

    def execute_move(self, move):
        # Update board.grid and check game event
        if self.board.update_cell(move, self.current_player.symbol):
            if self.sound_manager: self.sound_manager.play_place_sound()
            self.winner = GameRules.check_winner(self.board.grid)
            if self.winner or GameRules.is_draw(self.board.grid):
                self.game_over = True
                if self.sound_manager: self.sound_manager.play_game_end_sound()
                # Trigger screen shake on game end!
                self.screen_shake.trigger(intensity=18)
            else:
                # Switch turn
                self.current_player = self.player_o if self.current_player == self.player_x else self.player_x
                self.ai_move_pending = None

    def run_game(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            dt = clock.tick(60) / 1000.0  # Delta time in seconds
            
            # Update effects
            self.retro_bg.update(dt)
            self.screen_shake.update()
            
            # Get board dimensions for hover effect
            board_x, board_y, board_size, cell_size = get_board_dimensions(self.screen)
            
            if self.game_over:
                # Update end animation
                self.end_flash_timer += dt
            
            # Get screen shake offset
            shake_offset = self.screen_shake.get_offset()
            
            # Draw UI
            self.screen.fill(SCREENBLUE)
            
            # Draw background effects
            self.retro_bg.draw(self.screen)
            
            # Draw board with effects
            draw_board(
                self.screen, 
                self.board.grid, 
                shake_offset=shake_offset
            )
            
            # Draw scores with shake
            draw_score(self.screen, self.score_x, self.score_o, shake_offset)

            # Display player's turn or game result
            if not self.game_over:
                status_msg = f">> {self.current_player.symbol}'s TURN <<"
                draw_status(self.screen, status_msg, NEON_CYAN)
            else:
                # Game over message with emphasis
                if self.winner:
                    end_msg = f">>> {self.winner} WINS! <<<"
                else:
                    end_msg = ">>> DRAW! <<<"
                draw_status(self.screen, end_msg, NEON_YELLOW)
                draw_click_to_continue(self.screen)

            # Execute game events
            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    if hasattr(self, "input_handler") and hasattr(self.input_handler, "screen"):
                        self.input_handler.screen = self.screen
                    
                    width, height = self.screen.get_size()
                    self.retro_bg = RetroBackground(width, height)
                
                if event.type == pygame.QUIT:
                    return "QUIT"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "QUIT"
                
                if self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
                    if self.sound_manager: self.sound_manager.play_button_click()
                    return "GAME_OVER"
                
                # Execute player mouse click
                if not self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
                    if not hasattr(self.current_player, 'get_move'):
                        pos = pygame.mouse.get_pos()
                        move = self.input_handler.get_cell_from_pos(pos)
                        if move is not None:
                            self.execute_move(move)

            # AI's turn (if game mode is AI)
            if not self.game_over and hasattr(self.current_player, 'get_move'):
                self.handle_turn(dt)
            
            pygame.display.flip()
