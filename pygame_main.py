import pygame
import sys

from src.UI.pygame_menu import run_menu, run_reset

def main():
    pygame.init()
    
    WIDTH, HEIGHT = 700, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("NEO TIC-TAC-TOE")
    
    clock = pygame.time.Clock()
    
    # outer loop - choose mode
    while True:
        game_mode = run_menu(screen, clock)
        
        # inner loop
        while True:
            # game flow
            
            action = run_reset(screen, clock, game_mode)
            
            if action == "RESTART":
                continue
            if action == "MENU":
                break
    
if __name__ == "__main__":
    main()