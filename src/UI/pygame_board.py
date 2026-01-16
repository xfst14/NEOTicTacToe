import pygame
import os
from src.model.constants import X, O, N
from src.UI.retro_effects import (
    NEON_CYAN, NEON_YELLOW
)

# rgb color (adapted from nct logo with retro enhancement)
SCREENBLUE = (8, 13, 51)
DARKBLUE = (33, 42, 71)
LIGHTBLUE = (72, 150, 172)
WHITE = (245, 245, 245)
YELLOW = (252, 180, 27)



def load_image(path, size):
    """Load scaled images """
    if os.path.exists(path):
        try:
            image = pygame.image.load(path)
            return pygame.transform.scale(image, (size, size))
        except pygame.error:
            return None
    return None


def get_board_dimensions(screen):
    """Get board position and size (centralized for consistency)."""
    WIDTH, HEIGHT = screen.get_size()
    board_size = 300
    cell_size = board_size // 3
    board_x = (WIDTH - board_size) // 2
    board_y = (HEIGHT - board_size) // 2
    return board_x, board_y, board_size, cell_size

def draw_board(screen, board_state, shake_offset=(0, 0)):
    """
    Draw the tic-tac-toe board on the screen with retro effects.
    """
    board_x, board_y, board_size, cell_size = get_board_dimensions(screen)
    
    # Apply screen shake offset
    board_x += shake_offset[0]
    board_y += shake_offset[1]
    
    # Load X and O images (cached)
    image_size = int(cell_size * 0.8)
    x_image = load_image("src/assets/X.png", image_size)
    o_image = load_image("src/assets/O.png", image_size)
    
    # Draw board background with slight transparency for glow effect
    bg_surface = pygame.Surface((board_size + 20, board_size + 20), pygame.SRCALPHA)
    pygame.draw.rect(bg_surface, (*DARKBLUE, 220), 
                    (0, 0, board_size + 20, board_size + 20), 
                    border_radius=15)
    screen.blit(bg_surface, (board_x - 10, board_y - 10))
        
    # Draw grid lines with neon glow effect
    line_width = 3
    
    # Create glow effect for grid lines
    for glow_offset in range(3, 0, -1):
        glow_alpha = int(60 / glow_offset)
        glow_color = (*NEON_CYAN[:3], glow_alpha)
        
        # Vertical lines
        for i in range(1, 3):
            x = board_x + i * cell_size
            glow_surface = pygame.Surface((line_width + glow_offset * 2, board_size), pygame.SRCALPHA)
            pygame.draw.line(glow_surface, glow_color, 
                           (glow_offset + line_width // 2, 0), 
                           (glow_offset + line_width // 2, board_size), 
                           line_width + glow_offset)
            screen.blit(glow_surface, (x - glow_offset - line_width // 2, board_y))
        
        # Horizontal lines
        for i in range(1, 3):
            y = board_y + i * cell_size
            glow_surface = pygame.Surface((board_size, line_width + glow_offset * 2), pygame.SRCALPHA)
            pygame.draw.line(glow_surface, glow_color, 
                           (0, glow_offset + line_width // 2), 
                           (board_size, glow_offset + line_width // 2), 
                           line_width + glow_offset)
            screen.blit(glow_surface, (board_x, y - glow_offset - line_width // 2))
    
    # Draw main grid lines
    for i in range(1, 3):
        x = board_x + i * cell_size
        pygame.draw.line(screen, NEON_CYAN, (x, board_y), (x, board_y + board_size), line_width)
    
    for i in range(1, 3):
        y = board_y + i * cell_size
        pygame.draw.line(screen, NEON_CYAN, (board_x, y), (board_x + board_size, y), line_width)
    
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

def draw_status(screen, message, color=NEON_YELLOW):
    """Draw status message."""
    WIDTH, HEIGHT = screen.get_size()
    
    font = pygame.font.SysFont('consolas', 36, bold=True)
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 40))
    screen.blit(text_surface, text_rect)

def draw_click_to_continue(screen):
    """Draw 'Click to continue' text."""
    WIDTH, HEIGHT = screen.get_size()
    board_size = 300
    board_y = (HEIGHT - board_size) // 2
    prompt_y = board_y + board_size + 35

    font = pygame.font.SysFont('consolas', 24, bold=True)
    text_surface = font.render("[ CLICK TO CONTINUE ]", True, NEON_CYAN)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, prompt_y))
    screen.blit(text_surface, text_rect)

def draw_score(screen, score_x, score_o, shake_offset=(0, 0)):
    """Draw player scores on both sides of the board with retro styling."""
    WIDTH, HEIGHT = screen.get_size()
    board_size = 300
    board_x = (WIDTH - board_size) // 2 + shake_offset[0]
    board_y = (HEIGHT - board_size) // 2 + shake_offset[1]

    # Load X and O images for score display (cached)
    icon_size = 40
    x_image = load_image("src/assets/X.png", icon_size)
    o_image = load_image("src/assets/O.png", icon_size)

    # Draw X score (left side)
    x_score_x = board_x - 120
    x_score_y = board_y + board_size // 2 - 30

    if x_image:
        x_icon_rect = x_image.get_rect(center=(x_score_x, x_score_y))
        screen.blit(x_image, x_icon_rect)

    font = pygame.font.SysFont('consolas', 48, bold=True)
    x_score_text = font.render(str(score_x), True, WHITE)
    x_score_rect = x_score_text.get_rect(center=(x_score_x, x_score_y + 55))
    screen.blit(x_score_text, x_score_rect)

    # Draw O score (right side)
    o_score_x = board_x + board_size + 120
    o_score_y = board_y + board_size // 2 - 30

    if o_image:
        o_icon_rect = o_image.get_rect(center=(o_score_x, o_score_y))
        screen.blit(o_image, o_icon_rect)

    o_score_text = font.render(str(score_o), True, WHITE)
    o_score_rect = o_score_text.get_rect(center=(o_score_x, o_score_y + 55))
    screen.blit(o_score_text, o_score_rect)
