import pygame
import sys
import os

# rgb color (adapted from nct logo)
SCREENBLUE = (8, 13, 51)
DARKBLUE = (33, 42, 71)
LIGHTBLUE = (72, 150, 172)
WHITE = (245, 245, 245)
YELLOW = (252, 180, 27)

def button(screen, font, rect, text, mouse_pos):
    color = DARKBLUE if rect.collidepoint(mouse_pos) else LIGHTBLUE
    pygame.draw.rect(screen, color, rect, border_radius=12)
    label = font.render(text, True, WHITE)
    screen.blit(label, label.get_rect(center=rect.center))

# show menu   
def run_menu(screen, clock):
    WIDTH, HEIGHT = screen.get_size()
    
    title_font = pygame.font.SysFont(None, 64)
    button_font = pygame.font.SysFont(None, 34)
    info_font = pygame.font.SysFont(None, 28)

    # Load logo if it exists
    logo = None
    logo_path = "src/assets/logo.png"
    if os.path.exists(logo_path):
        try:
            logo = pygame.image.load(logo_path)
            # Scale logo to reasonable size (max width 200px, maintain aspect ratio)
            logo_width = min(200, logo.get_width())
            logo_height = int(logo.get_height() * (logo_width / logo.get_width()))
            logo = pygame.transform.scale(logo, (logo_width, logo_height))
        except pygame.error:
            pass

    button_pvp = pygame.Rect(200, 220, 300, 60)
    button_randomai = pygame.Rect(200, 300, 300, 60)
    button_minimaxai = pygame.Rect(200, 380, 300, 60)
    
    while True:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()
        
        try:
            WIDTH, HEIGHT = screen.get_size()
        except pygame.error:
            return "QUIT"
        
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                return "QUIT"
                
            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_pvp.collidepoint(event.pos):
                    return 1
                if button_randomai.collidepoint(event.pos):
                    return 2
                if button_minimaxai.collidepoint(event.pos):
                    return 3

        # draw menu
        screen.fill(SCREENBLUE)
    
        # Draw logo if available
        y_offset = 0
        if logo:
            logo_rect = logo.get_rect(center=(WIDTH // 2, 80))
            screen.blit(logo, logo_rect)
            y_offset = 60  # Adjust title position if logo is present
        
        title = title_font.render("NEO TIC-TAC-TOE", True, YELLOW)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 120 + y_offset)))
    
        button(screen, button_font, button_pvp, "Player vs Player", mouse_pos)
        button(screen, button_font, button_randomai, "Player vs Bot (Easy)", mouse_pos)
        button(screen, button_font, button_minimaxai, "Player vs Bot (Hard)", mouse_pos)
    
        pygame.display.flip()
                
def run_reset(screen, clock, game_mode, score_x=0, score_o=0):
    WIDTH, HEIGHT = screen.get_size()

    title_font = pygame.font.SysFont(None, 64)
    button_font = pygame.font.SysFont(None, 34)
    info_font = pygame.font.SysFont(None, 28)
    score_font = pygame.font.SysFont(None, 48)

    button_restart = pygame.Rect(180, 340, 340, 60)
    button_menu = pygame.Rect(180, 420, 340, 60)

    mode_text = {1: "PVP", 2: "Bot (Easy)", 3: "Bot (Hard)"}[game_mode]

    # Load X and O images for score display
    x_image = None
    o_image = None
    x_path = "src/assets/X.png"
    o_path = "src/assets/O.png"

    icon_size = 50
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

    while True:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                return "QUIT"

            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_restart.collidepoint(event.pos):
                    return "RESTART"
                if button_menu.collidepoint(event.pos):
                    return "MENU"

        # draw
        screen.fill(SCREENBLUE)

        message1 = title_font.render("Thank you for playing!", True, YELLOW)
        screen.blit(message1, message1.get_rect(center=(WIDTH // 2, 100)))

        message2 = info_font.render(f"Mode: {mode_text}", True, WHITE)
        screen.blit(message2, message2.get_rect(center=(WIDTH // 2, 150)))

        # Draw score section
        score_y = 220
        score_spacing = 120

        # Draw X score (left)
        x_pos = WIDTH // 2 - score_spacing
        if x_image:
            x_icon_rect = x_image.get_rect(center=(x_pos, score_y))
            screen.blit(x_image, x_icon_rect)
        x_score_text = score_font.render(str(score_x), True, WHITE)
        screen.blit(x_score_text, x_score_text.get_rect(center=(x_pos, score_y + 50)))

        # Draw dash separator
        dash_text = score_font.render("-", True, WHITE)
        screen.blit(dash_text, dash_text.get_rect(center=(WIDTH // 2, score_y + 25)))

        # Draw O score (right)
        o_pos = WIDTH // 2 + score_spacing
        if o_image:
            o_icon_rect = o_image.get_rect(center=(o_pos, score_y))
            screen.blit(o_image, o_icon_rect)
        o_score_text = score_font.render(str(score_o), True, WHITE)
        screen.blit(o_score_text, o_score_text.get_rect(center=(o_pos, score_y + 50)))

        button(screen, button_font, button_restart, "Play again?", mouse_pos)
        button(screen, button_font, button_menu, "Back to menu", mouse_pos)

        pygame.display.flip()