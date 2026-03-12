import pygame
import os
from src.model.constants import X, O, N
from src.UI.retro_effects import (
    NEON_CYAN, NEON_YELLOW
)
from utils.resource_handler import get_resource_path

# rgb color (adapted from nct logo with retro enhancement)
SCREENBLUE = (8, 13, 51)
DARKBLUE = (33, 42, 71)
LIGHTBLUE = (72, 150, 172)
WHITE = (245, 245, 245)
YELLOW = (252, 180, 27)

_image_cache = {}

def load_image(path, size):
    """Load scaled images """
    path = get_resource_path(path)
    key = (path, size)
    if key in _image_cache:
        return _image_cache[key]
    
    if os.path.exists(path):
        try:
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.smoothscale(image, (size, size))
            _image_cache[key] = image
            return image
        except pygame.error:
            return None
    return None

def get_board_dimensions(screen):
    """Get board position and size (centralized for consistency)."""
    WIDTH, HEIGHT = screen.get_size()
    
    board_size = int(min(WIDTH, HEIGHT) * 0.6)
    board_size = max(280, min(board_size, 720))
    
    cell_size = board_size // 3
    board_x = (WIDTH - board_size) // 2
    board_y = (HEIGHT - board_size) // 2 + int(HEIGHT * 0.05)
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
    x_image = load_image("assets/X.png", image_size)
    o_image = load_image("assets/O.png", image_size)
    
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
    
    font_size = int(HEIGHT * 0.08)
    font_size = max(24, min(font_size, 64))
    
    font = pygame.font.SysFont('consolas', font_size, bold=True)
    text_surface = font.render(message, True, color)
    y = int(HEIGHT * 0.1)
    screen.blit(text_surface, text_surface.get_rect(center=(WIDTH // 2, y)))

def draw_click_to_continue(screen):
    """Draw 'Click to continue' text."""
    WIDTH, HEIGHT = screen.get_size()
    board_x,board_y, board_size, cell_size = get_board_dimensions(screen)
    
    font_size = int(HEIGHT * 0.06)
    font_size = max(18, min(font_size, 48))
    font = pygame.font.SysFont('consolas', font_size, bold=True)
    
    gap = int(board_size * 0.12)
    gap = max(22, min(gap, 70))
    prompt_y = board_y + board_size + gap
    bottom_margin = int(HEIGHT * 0.06)
    prompt_y = min(prompt_y, HEIGHT - bottom_margin)
    
    text_surface = font.render("[ CLICK TO CONTINUE ]", True, NEON_CYAN)
    screen.blit(text_surface, text_surface.get_rect(center=(WIDTH // 2, prompt_y)))

def draw_score(screen, score_x, score_o, shake_offset=(0, 0)):
    """Draw player scores on both sides of the board with retro styling."""
    WIDTH, HEIGHT = screen.get_size()
    board_x, board_y, board_size, cell_size = get_board_dimensions(screen)
    board_x += shake_offset[0]
    board_y += shake_offset[1]
    
    # Load X and O images for score display (cached)
    icon_size = int(cell_size * 0.85)
    icon_size = max(40, min(icon_size, 90))
    x_image = load_image("assets/X.png", icon_size)
    o_image = load_image("assets/O.png", icon_size)

    # Resize based on window height
    font_size = int(HEIGHT * 0.09)
    font_size = max(24, min(font_size, 56))
    font = pygame.font.SysFont('consolas', font_size, bold=True)
    
    icon_num_gap = int(icon_size * 0.9)
    icon_num_gap = max(42, min(icon_num_gap, 72))
    
    side_gap = int(board_size * 0.22)
    side_gap = max(85, min(side_gap, 155))
    
    left_x = board_x - side_gap
    right_x = board_x + board_size + side_gap
    center_y = board_y + board_size // 2
    
    if x_image:
        screen.blit(x_image, x_image.get_rect(center=(left_x, center_y)))
    x_text = font.render(str(score_x), True, WHITE)
    screen.blit(x_text, x_text.get_rect(center=(left_x, center_y + icon_num_gap)))

    if o_image:
        screen.blit(o_image, o_image.get_rect(center=(right_x, center_y)))
    o_text = font.render(str(score_o), True, WHITE)
    screen.blit(o_text, o_text.get_rect(center=(right_x, center_y + icon_num_gap)))
