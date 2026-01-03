import pygame
import sys

from src.UI.pygame_menu import run_menu, run_reset
from src.UI.pygame_board import draw_board
from src.model.board import Board
from src.model.constants import N

def main():
    pygame.init()
    
    WIDTH, HEIGHT = 700, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("NEO TIC-TAC-TOE")
    
    clock = pygame.time.Clock()
    
    # outer loop - choose mode
    while True:
        game_mode = run_menu(screen, clock)
        
        # Initialize board for the game
        board = Board()
        
        # inner loop - game loop
        while True:
            clock.tick(60)
            
            # Handle events (quit only - mouse input will be handled by another person)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Draw the board
            screen.fill((8, 13, 51))  # SCREENBLUE background
            draw_board(screen, board.grid)
            pygame.display.flip()
            
            # TODO: Game logic and mouse input will be handled by another person
            # For now, the board is displayed with empty state
            
            # Placeholder: This will be replaced with actual game logic
            # When game ends, break to show reset screen
            # break
            
            # Temporary: Press ESC to go to reset screen (for testing)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                break
        
        # Show reset screen after game ends
        action = run_reset(screen, clock, game_mode)
        
        if action == "RESTART":
            continue
        if action == "MENU":
            continue
    
if __name__ == "__main__":
    main()