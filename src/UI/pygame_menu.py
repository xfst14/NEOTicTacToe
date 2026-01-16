import pygame
import os
from src.UI.retro_effects import (
    RetroBackground,
    NEON_CYAN, NEON_YELLOW
)

# rgb color (adapted from nct logo with retro enhancement)
SCREENBLUE = (8, 13, 51)
LIGHTBLUE = (72, 150, 172)
WHITE = (245, 245, 245)
FONT_PATH = "src/assets/prstartk.ttf"

def _get_logo():
    """Load logo (caching removed)."""
    logo_path = "src/assets/logo.png"
    if os.path.exists(logo_path):
        try:
            logo = pygame.image.load(logo_path)
            logo_width = min(200, logo.get_width())
            logo_height = int(logo.get_height() * (logo_width / logo.get_width()))
            return pygame.transform.scale(logo, (logo_width, logo_height))
        except pygame.error:
            return None
    return None


class RetroButton:
    """Retro-styled button."""
    
    def __init__(self, rect, text, base_color=LIGHTBLUE):
        self.rect = rect
        self.text = text
        self.base_color = base_color
        # Calculate hover color (lighter version of base color)
        self.hover_color = tuple(min(255, c + 30) for c in base_color)
        
    def draw(self, screen):
        """Draw the button."""
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)
        
        color = self.hover_color if is_hovered else self.base_color
        
        # Draw button background
        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        
        # Draw border
        pygame.draw.rect(screen, color, self.rect, width=2, border_radius=12)
        
        # Draw text
        font = pygame.font.SysFont('consolas', 24, bold=True)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, event):
        """Check if button was clicked."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False


def run_menu(screen, clock, sound_manager=None):
    """Run the main menu with retro effects."""
    WIDTH, HEIGHT = screen.get_size()
    
    # Initialize retro background
    retro_bg = RetroBackground(WIDTH, HEIGHT)
    
    # Create retro buttons
    button_pvp = RetroButton(pygame.Rect(200, 220, 300, 60), "Player vs Player", LIGHTBLUE)
    button_randomai = RetroButton(pygame.Rect(200, 300, 300, 60), "Player vs Bot (Easy)", LIGHTBLUE)
    button_minimaxai = RetroButton(pygame.Rect(200, 380, 300, 60), "Player vs Bot (Hard)", LIGHTBLUE)
    
    buttons = [button_pvp, button_randomai, button_minimaxai]
    
    # Animation timer
    title_pulse = 0
    
    while True:
        dt = clock.tick(60) / 1000.0  # Delta time in seconds
        mouse_pos = pygame.mouse.get_pos()
        
        try:
            WIDTH, HEIGHT = screen.get_size()
        except pygame.error:
            return "QUIT"
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            
            if button_pvp.is_clicked(event):
                if sound_manager: sound_manager.play_button_click()
                return 1
            if button_randomai.is_clicked(event):
                if sound_manager: sound_manager.play_button_click()
                return 2
            if button_minimaxai.is_clicked(event):
                if sound_manager: sound_manager.play_button_click()
                return 3
        
        # Update
        retro_bg.update(dt)
        title_pulse += dt * 3
        
        # Draw
        screen.fill(SCREENBLUE)
        retro_bg.draw(screen)
        
        # Draw logo if available
        logo = _get_logo()
        y_offset = 0
        if logo:
            logo_rect = logo.get_rect(center=(WIDTH // 2, 80))
            screen.blit(logo, logo_rect)
            y_offset = 60
        
        # Draw title
        title_font = pygame.font.Font(FONT_PATH, 36)
        title_surface = title_font.render("NEO TIC-TAC-TOE", True, NEON_YELLOW)
        screen.blit(title_surface, title_surface.get_rect(center=(WIDTH // 2, 120 + y_offset)))
        
        # Draw buttons
        for btn in buttons:
            btn.draw(screen)
        
        pygame.display.flip()


def run_reset(screen, clock, game_mode, score_x=0, score_o=0, sound_manager=None):
    """Run the reset/game over screen with retro effects."""
    WIDTH, HEIGHT = screen.get_size()
    
    # Initialize retro background
    retro_bg = RetroBackground(WIDTH, HEIGHT)
    
    # Create retro buttons
    button_restart = RetroButton(pygame.Rect(200, 340, 300, 60), "PLAY AGAIN?", LIGHTBLUE)
    button_menu = RetroButton(pygame.Rect(200, 420, 300, 60), "BACK TO MENU", LIGHTBLUE)
    
    buttons = [button_restart, button_menu]
    
    mode_text = {1: "PVP", 2: "Bot (Easy)", 3: "Bot (Hard)"}[game_mode]
    
    # Load X and O images
    icon_size = 50
    x_image = None
    o_image = None
    x_path = "src/assets/X.png"
    o_path = "src/assets/O.png"
    
    if os.path.exists(x_path):
        try:
            x_image = pygame.image.load(x_path)
            x_image = pygame.transform.scale(x_image, (icon_size, icon_size))
        except pygame.error:
            pass
    
    if os.path.exists(o_path):
        try:
            o_image = pygame.image.load(o_path)
            o_image = pygame.transform.scale(o_image, (icon_size, icon_size))
        except pygame.error:
            pass
    
    animation_time = 0
    
    while True:
        dt = clock.tick(60) / 1000.0
        mouse_pos = pygame.mouse.get_pos()
        animation_time += dt
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            
            if button_restart.is_clicked(event):
                if sound_manager: sound_manager.play_button_click()
                return "RESTART"
            if button_menu.is_clicked(event):
                if sound_manager: sound_manager.play_button_click()
                return "MENU"
        
        # Update
        retro_bg.update(dt)
        
        # Draw
        screen.fill(SCREENBLUE)
        retro_bg.draw(screen)
        
        # Draw game over message
        title_font = pygame.font.SysFont('consolas', 56, bold=True)
        message1 = title_font.render("GAME OVER", True, NEON_YELLOW)
        screen.blit(message1, message1.get_rect(center=(WIDTH // 2, 80)))
        
        info_font = pygame.font.SysFont('consolas', 24, bold=True)
        message2 = info_font.render(f"Mode: {mode_text}", True, WHITE)
        screen.blit(message2, message2.get_rect(center=(WIDTH // 2, 130)))
        
        # Draw score section 
        score_y = 200
        score_spacing = 120
        
        # Draw "VS" text
        vs_font = pygame.font.SysFont('consolas', 32, bold=True)
        vs_text = vs_font.render("VS", True, NEON_CYAN)
        screen.blit(vs_text, vs_text.get_rect(center=(WIDTH // 2, score_y + 25)))
        
        # Draw X score (left)
        score_font = pygame.font.SysFont('consolas', 48, bold=True)
        x_pos = WIDTH // 2 - score_spacing
        if x_image:
            x_icon_rect = x_image.get_rect(center=(x_pos, score_y))
            screen.blit(x_image, x_icon_rect)
        x_score_text = score_font.render(str(score_x), True, WHITE)
        screen.blit(x_score_text, x_score_text.get_rect(center=(x_pos, score_y + 55)))
        
        # Draw O score (right)
        o_pos = WIDTH // 2 + score_spacing
        if o_image:
            o_icon_rect = o_image.get_rect(center=(o_pos, score_y))
            screen.blit(o_image, o_icon_rect)
        o_score_text = score_font.render(str(score_o), True, WHITE)
        screen.blit(o_score_text, o_score_text.get_rect(center=(o_pos, score_y + 55)))
        
        # Draw buttons
        for btn in buttons:
            btn.draw(screen)
        
        pygame.display.flip()