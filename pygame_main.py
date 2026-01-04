import pygame
import sys

from src.UI.pygame_menu import run_menu, run_reset
from src.UI.pygame_board import draw_board
from src.UI.pygame_input_handler import PygameInputHandler
from src.model.board import Board
from src.model.constants import X, O, N

def main():
    pygame.init()
    
    WIDTH, HEIGHT = 700, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("NEO TIC-TAC-TOE")
    
    clock = pygame.time.Clock()
    
    # outer loop - choose mode
    while True:
        game_mode = run_menu(screen, clock)

        # Initialize board and input handler for the game
        board = Board()
        input_handler = PygameInputHandler(screen)

        # Track current player (X starts first)
        current_symbol = X
        game_over = False

        # inner loop - game loop
        while not game_over:
            clock.tick(60)

            # Handle events - now with mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Handle mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    cell_index = input_handler.get_cell_from_pos(pos)

                    if cell_index is not None:
                        # Try to update the cell
                        if board.update_cell(cell_index, current_symbol):
                            # Successfully placed symbol, switch player
                            current_symbol = O if current_symbol == X else X

                            # Check if board is full (simple game over condition)
                            if all(cell is not None for cell in board.grid):
                                game_over = True

            # Draw the board
            screen.fill((8, 13, 51))  # SCREENBLUE background
            draw_board(screen, board.grid)

            # Display current player turn
            font = pygame.font.Font(None, 36)
            turn_text = font.render(f"Current Player: {current_symbol}", True, (252, 180, 27))
            screen.blit(turn_text, (WIDTH // 2 - 120, 30))

            pygame.display.flip()

        # Show reset screen after game ends
        action = run_reset(screen, clock, game_mode)

        if action == "RESTART":
            continue
        if action == "MENU":
            continue
    
if __name__ == "__main__":
    main()