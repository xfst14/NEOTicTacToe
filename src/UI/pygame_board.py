import pygame
from src.model.constants import X, O, N

# rgb color (adapted from nct logo)
SCREENBLUE = (8, 13, 51)
DARKBLUE = (33, 42, 71)
LIGHTBLUE = (72, 150, 172)
WHITE = (245, 245, 245)
YELLOW = (252, 180, 27)
# Grid line color (slightly whiter)
GRID_COLOR = (180, 200, 220)

def draw_board(screen, board_state):
    """
    Draw the tic-tac-toe board on the screen.
    """
    WIDTH, HEIGHT = screen.get_size()
    
    # Board dimensions (increased size)
    board_size = 420
    cell_size = board_size // 3
    board_x = (WIDTH - board_size) // 2
    board_y = (HEIGHT - board_size) // 2
    
    # Draw board background
    pygame.draw.rect(screen, DARKBLUE, 
                    (board_x - 10, board_y - 10, board_size + 20, board_size + 20), 
                    border_radius=15)
    
    # Draw grid lines
    line_width = 4
    # Vertical lines
    for i in range(1, 3):
        x = board_x + i * cell_size
        pygame.draw.line(screen, GRID_COLOR, (x, board_y), (x, board_y + board_size), line_width)
    
    # Horizontal lines
    for i in range(1, 3):
        y = board_y + i * cell_size
        pygame.draw.line(screen, GRID_COLOR, (board_x, y), (board_x + board_size, y), line_width)

    
    # Draw X and O symbols (increased font size for bigger board)
    symbol_font = pygame.font.SysFont(None, 120)
    
    for row in range(3):
        for col in range(3):
            index = row * 3 + col
            cell_value = board_state[index] if index < len(board_state) else N
            
            if cell_value == X:
                # Draw X in yellow
                x_pos = board_x + col * cell_size + cell_size // 2
                y_pos = board_y + row * cell_size + cell_size // 2
                symbol = symbol_font.render("X", True, YELLOW)
                screen.blit(symbol, symbol.get_rect(center=(x_pos, y_pos)))
            elif cell_value == O:
                # Draw O in white
                x_pos = board_x + col * cell_size + cell_size // 2
                y_pos = board_y + row * cell_size + cell_size // 2
                symbol = symbol_font.render("O", True, WHITE)
                screen.blit(symbol, symbol.get_rect(center=(x_pos, y_pos)))

