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
    logo_paths = ["logo.png", "assets/logo.png", "images/logo.png", "src/assets/logo.png"]
    for path in logo_paths:
        if os.path.exists(path):
            try:
                logo = pygame.image.load(path)
                # Scale logo to reasonable size (max width 200px, maintain aspect ratio)
                logo_width = min(200, logo.get_width())
                logo_height = int(logo.get_height() * (logo_width / logo.get_width()))
                logo = pygame.transform.scale(logo, (logo_width, logo_height))
                break
            except pygame.error:
                continue

    button_pvp = pygame.Rect(200, 170, 300, 60)
    button_randomai = pygame.Rect(200, 250, 300, 60)
    button_minimaxai = pygame.Rect(200, 330, 300, 60)
    
    while True:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
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
            logo_rect = logo.get_rect(center=(WIDTH // 2, 50))
            screen.blit(logo, logo_rect)
            y_offset = 60  # Adjust title position if logo is present
        
        title = title_font.render("NEO TIC-TAC-TOE", True, YELLOW)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 90 + y_offset)))
    
        subtitle = info_font.render("Choose a game mode!", True, YELLOW)
        screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 135 + y_offset)))
    
        button(screen, button_font, button_pvp, "Player vs Player", mouse_pos)
        button(screen, button_font, button_randomai, "Player vs Easy AI", mouse_pos)
        button(screen, button_font, button_minimaxai, "Player vs Hard AI", mouse_pos)
    
        pygame.display.flip()
                
def run_reset(screen, clock, game_mode):
    WIDTH, HEIGHT = screen.get_size()
    
    title_font = pygame.font.SysFont(None, 64)
    button_font = pygame.font.SysFont(None, 34)
    info_font = pygame.font.SysFont(None, 28)
    
    button_restart = pygame.Rect(180, 300, 340, 60)
    button_menu = pygame.Rect(180, 380, 340, 60)
    
    mode_text = {1: "PVP", 2: "EASY AI", 3: "HARD AI"}[game_mode]
    
    while True:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # mouse click  
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_restart.collidepoint(event.pos):
                    return "RESTART"
                if button_menu.collidepoint(event.pos):
                    return "MENU"
    
        # draw
        screen.fill(SCREENBLUE)
        
        message1 = title_font.render("Thank you for playing!", True, YELLOW)
        screen.blit(message1, message1.get_rect(center=(WIDTH // 2, 120)))
        
        message2 = info_font.render(f"Mode: {mode_text}", True, WHITE)
        screen.blit(message2, message2.get_rect(center=(WIDTH // 2, 170)))
        
        button(screen, button_font, button_restart, "Play again?", mouse_pos)
        button(screen, button_font, button_menu, "Back to menu", mouse_pos)
        
        pygame.display.flip()