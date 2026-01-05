import pygame
import os
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
    
    # Board dimensions
    board_size = 300
    cell_size = board_size // 3
    board_x = (WIDTH - board_size) // 2
    board_y = (HEIGHT - board_size) // 2
    
    # Load X and O images
    x_image = None
    o_image = None
    x_path = "src/assets/X.png"
    o_path = "src/assets/O.png"
    
    if os.path.exists(x_path):
        try:
            x_image = pygame.image.load(x_path)
            # Scale image to fit in cell (leave some padding)
            image_size = int(cell_size * 0.8)
            x_image = pygame.transform.scale(x_image, (image_size, image_size))
        except pygame.error:
            pass
    
    if os.path.exists(o_path):
        try:
            o_image = pygame.image.load(o_path)
            # Scale image to fit in cell (leave some padding)
            image_size = int(cell_size * 0.8)
            o_image = pygame.transform.scale(o_image, (image_size, image_size))
        except pygame.error:
            pass
    
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
    
    # Draw X and O images
    for row in range(3):
        for col in range(3):
            index = row * 3 + col
            cell_value = board_state[index] if index < len(board_state) else N
            
            if cell_value == X and x_image:
                # Draw X image centered in cell
                x_pos = board_x + col * cell_size + cell_size // 2
                y_pos = board_y + row * cell_size + cell_size // 2
                image_rect = x_image.get_rect(center=(x_pos, y_pos))
                screen.blit(x_image, image_rect)
            elif cell_value == O and o_image:
                # Draw O image centered in cell
                x_pos = board_x + col * cell_size + cell_size // 2
                y_pos = board_y + row * cell_size + cell_size // 2
                image_rect = o_image.get_rect(center=(x_pos, y_pos))
                screen.blit(o_image, image_rect)

def draw_status(screen, message, color=YELLOW):
    WIDTH, HEIGHT = screen.get_size()
    font = pygame.font.Font(None, 36)
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 40))
    screen.blit(text_surface, text_rect)

def draw_click_to_continue(screen):
    """Draw 'Click to continue' text under the board"""
    WIDTH, HEIGHT = screen.get_size()
    board_size = 300
    board_y = (HEIGHT - board_size) // 2
    prompt_y = board_y + board_size + 30
    
    font = pygame.font.Font(None, 28)
    text_surface = font.render("Click to continue", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, prompt_y))
    screen.blit(text_surface, text_rect)
