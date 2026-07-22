import pygame
import os
from src.UI.retro_effects import (
    RetroBackground,
    NEON_CYAN, NEON_YELLOW
)
from src.utils.resource_handler import get_resource_path

# rgb color (adapted from nct logo with retro enhancement)
SCREENBLUE = (8, 13, 51)
LIGHTBLUE = (72, 150, 172)
WHITE = (245, 245, 245)
FONT_PATH = get_resource_path("assets/prstartk.ttf")

WINDOWED_SIZE = (700, 500)
DISPLAY_FLAGS = pygame.RESIZABLE

def _get_logo():
    """Load logo """
    logo_path = get_resource_path("assets/logo.png")
    if os.path.exists(logo_path):
        try:
            logo = pygame.image.load(logo_path)
            logo_width = min(200, logo.get_width())
            logo_height = int(logo.get_height() * (logo_width / logo.get_width()))
            return pygame.transform.scale(logo, (logo_width, logo_height))
        except pygame.error:
            return None
    return None

def ui_scale(screen_width, screen_height, base_width=700, base_height=500):
    scale_x = screen_width / base_width
    scale_y = screen_height / base_height
    scale = min(scale_x, scale_y)
    return scale_x, scale_y, scale

def font_scale(path, size, scale, bold=False, sys_name="consolas"):
    px = max(12, int(size * scale)) # px = pixels (font size)
    if path:
        return pygame.font.Font(path, px)
    return pygame.font.SysFont(sys_name, px, bold=bold)

class RetroButton:
    """Retro-styled button."""
    
    def __init__(self, rect_function, text, base_color=LIGHTBLUE):
        self.rect_function = rect_function
        self.text = text
        self.base_color = base_color
        # Calculate hover color (lighter version of base color)
        self.hover_color = tuple(min(255, c + 30) for c in base_color)
    
    def rect(self, W, H, scale):
        return self.rect_function(W, H, scale)
    
    def draw(self, screen, W, H, scale):
        """Draw the button."""
        rect = self.rect(W, H, scale)
        
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = rect.collidepoint(mouse_pos)
        color = self.hover_color if is_hovered else self.base_color
        
        radius = max(6, int(12 * scale))
        border_width = max(2, int(2 * scale))
        
        # Draw button background
        pygame.draw.rect(screen, color, rect, border_radius=radius)
        
        # Draw border
        pygame.draw.rect(screen, WHITE, rect, width=border_width, border_radius=radius)
        
        # Draw text
        font = pygame.font.SysFont('consolas', max(12, int(24 * scale)), bold=True)
        text_surface = font.render(self.text, True, WHITE)
        screen.blit(text_surface, text_surface.get_rect(center=rect.center))
    
    def is_clicked(self, event, W, H, scale):
        """Check if button was clicked."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            rect = self.rect(W, H, scale)
            return rect.collidepoint(event.pos)
        return False


def run_menu(screen, clock, sound_manager=None):
    """Run the main menu """
    WIDTH, HEIGHT = screen.get_size()
    
    # Initialize retro background
    retro_bg = RetroBackground(WIDTH, HEIGHT)
    
    logo = _get_logo()
    
    def make_button_stack(texts, center_y_ratio=0.7):
        def make_rect_function(index, total):
            def rect_function(W, H, scale):
                button_width = int(320 * scale)
                button_height = int(70 * scale)
                gap = int(20 * scale) 

                total_height = total * button_height + (total - 1) * gap
                top_y = int(H * center_y_ratio) - total_height // 2

                x = W // 2 - button_width // 2
                y = top_y + index * (button_height + gap)
                return pygame.Rect(x, y, button_width, button_height)
            return rect_function

        btns = []
        for i, t in enumerate(texts):
            btns.append(RetroButton(make_rect_function(i, len(texts)), t, LIGHTBLUE))
        return btns

    buttons = make_button_stack(
        ["Player vs Player", "Player vs Bot (Easy)", "Player vs Bot (Hard)"],
        center_y_ratio=0.7
    )

    button_pvp, button_randomai, button_minimaxai, button_alibabaqwenai = buttons

    
    # Animation timer
    title_pulse = 0
    
    while True:
        dt = clock.tick(60) / 1000.0  # Delta time in seconds
        
        try:
            WIDTH, HEIGHT = screen.get_size()
        except pygame.error:
            return "QUIT"
        
        scale_x, scale_y, scale = ui_scale(WIDTH, HEIGHT, base_width=700, base_height=500)
        
        for event in pygame.event.get():
            # Handle resize events
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, DISPLAY_FLAGS)
                WIDTH, HEIGHT = screen.get_size()
                retro_bg = RetroBackground(WIDTH, HEIGHT)
                            
            if event.type == pygame.QUIT:
                return "QUIT", screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "QUIT", screen
            
            if button_pvp.is_clicked(event, WIDTH, HEIGHT, scale):
                if sound_manager: sound_manager.play_button_click()
                return 1, screen
            if button_randomai.is_clicked(event, WIDTH, HEIGHT, scale):
                if sound_manager: sound_manager.play_button_click()
                return 2, screen
            if button_minimaxai.is_clicked(event, WIDTH, HEIGHT, scale):
                if sound_manager: sound_manager.play_button_click()
                return 3, screen
            if button_alibabaqwenai.is_clicked(event, WIDTH, HEIGHT, scale):
                if sound_manager: sound_manager.play_button_click()
                return 4, screen
        
        # Update
        if (retro_bg.width, retro_bg.height) != (WIDTH, HEIGHT):
            retro_bg = RetroBackground(WIDTH, HEIGHT)
        
        retro_bg.update(dt)
        title_pulse += dt * 3
        
        # Draw
        screen.fill(SCREENBLUE)
        retro_bg.draw(screen)
        
        # Draw logo if available
        y_offset = 0
        if logo:
            max_logo_width = int(min(0.25 * WIDTH, 300))
            logo_width = min(max_logo_width, logo.get_width())
            logo_height = int(logo.get_height() * (logo_width / logo.get_width()))
            logo_scaled = pygame.transform.smoothscale(logo, (logo_width, logo_height))
            logo_rect = logo_scaled.get_rect(center=(WIDTH // 2, int(HEIGHT * 0.18)))
            screen.blit(logo_scaled, logo_rect)
            y_offset = int(HEIGHT * 0.05)
        
        # Draw title
        title_font = font_scale(FONT_PATH, 36, scale)
        title_surface = title_font.render("NEO TIC-TAC-TOE", True, NEON_YELLOW)
        screen.blit(title_surface, title_surface.get_rect(center=(WIDTH // 2, int(HEIGHT * 0.3) + y_offset)))
        
        # Draw buttons
        for btn in buttons:
            btn.draw(screen, WIDTH, HEIGHT, scale)
        
        pygame.display.flip()


def run_reset(screen, clock, game_mode, score_x=0, score_o=0, sound_manager=None):
    """Run the reset/game over screen """
    WIDTH, HEIGHT = screen.get_size()
    
    # Initialize retro background
    retro_bg = RetroBackground(WIDTH, HEIGHT)
    
    # Mode text
    mode_text = {1: "PVP", 2: "Bot (Easy)", 3: "Bot (Hard)"}.get(game_mode, "Unknown")
    
    # Load X and O images
    x_image_raw = None
    o_image_raw = None
    x_path = get_resource_path("assets/X.png")
    o_path = get_resource_path("assets/O.png")
    
    if os.path.exists(x_path):
        try:
            x_image_raw = pygame.image.load(x_path).convert_alpha()
        except pygame.error:
            x_image_raw = None
    
    if os.path.exists(o_path):
        try:
            o_image_raw = pygame.image.load(o_path).convert_alpha()
        except pygame.error:
            o_image_raw = None
    
    # Create buttons
    def make_button_stack(texts, center_y_ratio=0.78):
        def make_rect_function(index, total):
            def rect_function(W, H, scale):
                button_width = int(320 * scale)
                button_height = int(70 * scale)
                gap = int(16 * scale)

                total_height = total * button_height + (total - 1) * gap
                top_y = int(H * center_y_ratio) - total_height // 2

                x = W // 2 - button_width // 2
                y = top_y + index * (button_height + gap)
                return pygame.Rect(x, y, button_width, button_height)
            return rect_function

        btns = []
        for i, t in enumerate(texts):
            btns.append(RetroButton(make_rect_function(i, len(texts)), t, LIGHTBLUE))
        return btns

    buttons = make_button_stack(["PLAY AGAIN?", "BACK TO MENU"], center_y_ratio=0.78)
    button_restart, button_menu = buttons
    
    animation_time = 0
    
    while True:
        dt = clock.tick(60) / 1000.0
        animation_time += dt
        
        try:
            WIDTH, HEIGHT = screen.get_size()
        except pygame.error:
            return "QUIT"
        
        _, _, scale = ui_scale(WIDTH, HEIGHT, base_width=700, base_height=500)
        
        if (retro_bg.width, retro_bg.height) != (WIDTH, HEIGHT):
            retro_bg = RetroBackground(WIDTH, HEIGHT)
        
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, DISPLAY_FLAGS)
                WIDTH, HEIGHT = screen.get_size()
                retro_bg = RetroBackground(WIDTH, HEIGHT)
                
            if event.type == pygame.QUIT:
                return "QUIT", screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "QUIT", screen
            
            if button_restart.is_clicked(event, WIDTH, HEIGHT, scale):
                if sound_manager: sound_manager.play_button_click()
                return "RESTART", screen
            if button_menu.is_clicked(event, WIDTH, HEIGHT, scale):
                if sound_manager: sound_manager.play_button_click()
                return "MENU", screen
        
        # Update
        retro_bg.update(dt)
        
        # Draw
        screen.fill(SCREENBLUE)
        retro_bg.draw(screen)
        
        # Draw "thank you for playing" message
        title_font = font_scale(None, 46, scale, bold=True)
        message1 = title_font.render("THANK YOU FOR PLAYING!", True, NEON_YELLOW)
        screen.blit(message1, message1.get_rect(center=(WIDTH // 2, int(HEIGHT * 0.16))))
        
        info_font = font_scale(None, 24, scale, bold=True)
        message2 = info_font.render(f"Mode: {mode_text}", True, WHITE)
        screen.blit(message2, message2.get_rect(center=(WIDTH // 2, int(HEIGHT * 0.26))))
        
        # Draw score section 
        score_y = int(HEIGHT * 0.45)
        score_spacing = int(120 * scale)
        
        # Draw "VS" text
        vs_font = font_scale(None, 32, scale, bold=True)
        vs_text = vs_font.render("VS", True, NEON_CYAN)
        screen.blit(vs_text, vs_text.get_rect(center=(WIDTH // 2, score_y + int(25 * scale))))
        
        # Icon size
        icon_size = max(40, int(80 * scale))
        x_image = (
            pygame.transform.smoothscale(x_image_raw, (icon_size, icon_size))
            if x_image_raw else None
        )
        o_image = (
            pygame.transform.smoothscale(o_image_raw, (icon_size, icon_size))
            if o_image_raw else None
        )
        
        # Draw X score (left)
        score_font = font_scale(None, 48, scale, bold=True)
        x_pos = WIDTH // 2 - score_spacing
        if x_image:
            x_icon_rect = x_image.get_rect(center=(x_pos, score_y - int(20 * scale)))
            screen.blit(x_image, x_icon_rect)
        x_score_text = score_font.render(str(score_x), True, WHITE)
        screen.blit(x_score_text, x_score_text.get_rect(center=(x_pos, score_y + int(55 * scale))))
        
        # Draw O score (right)
        o_pos = WIDTH // 2 + score_spacing
        if o_image:
            o_icon_rect = o_image.get_rect(center=(o_pos, score_y - int(20 * scale)))
            screen.blit(o_image, o_icon_rect)
        o_score_text = score_font.render(str(score_o), True, WHITE)
        screen.blit(o_score_text, o_score_text.get_rect(center=(o_pos, score_y + int(55 * scale))))
        
        # Draw buttons
        for btn in buttons:
            btn.draw(screen, WIDTH, HEIGHT, scale)
        
        pygame.display.flip()
