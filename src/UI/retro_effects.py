"""
Retro Effects Module for NEO Tic-Tac-Toe
Contains optimized retro visual effects: scanlines, background effects, 
screen shake, hover effects, and retro text rendering.
"""

import pygame
import math
import random

# Retro color palette (neon cyberpunk theme)
NEON_CYAN = (0, 255, 255)
NEON_YELLOW = (255, 255, 0)
RETRO_PURPLE = (138, 43, 226)
RETRO_PINK = (255, 20, 147)


class RetroBackground:
    """Optimized retro background with scanlines and grid effects."""
    

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.time = 0
        
        # Floating particles
        self.particles = []
        self._init_particles(15)
        
    def _create_scanline_surface(self):
        """Generate scanlines (optimization removed)."""
        scanline_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        for y in range(0, self.height, 4):  # Every 4 pixels
            pygame.draw.line(scanline_surface, (0, 0, 0, 30), (0, y), (self.width, y), 1)
        return scanline_surface
    
    def _create_grid_surface(self):
        """Generate grid pattern (optimization removed)."""
        grid_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        grid_color = (NEON_CYAN[0], NEON_CYAN[1], NEON_CYAN[2], 15)
        
        # Vertical lines
        for x in range(0, self.width, 40):
            pygame.draw.line(grid_surface, grid_color, (x, 0), (x, self.height), 1)
        
        # Horizontal lines  
        for y in range(0, self.height, 40):
            pygame.draw.line(grid_surface, grid_color, (0, y), (self.width, y), 1)
        return grid_surface
    
    def _init_particles(self, count):
        """Initialize floating particles."""
        for _ in range(count):
            self.particles.append({
                'x': random.randint(0, self.width),
                'y': random.randint(0, self.height),
                'size': random.randint(1, 3),
                'speed': random.uniform(0.3, 1.0),
                'color': random.choice([NEON_CYAN, NEON_YELLOW, RETRO_PURPLE]),
                'alpha': random.randint(50, 150)
            })
    
    def update(self, dt):
        """Update particle positions."""
        self.time += dt
        
        for p in self.particles:
            p['y'] -= p['speed']
            p['x'] += math.sin(self.time * 0.5 + p['y'] * 0.02) * 0.5
            
            # Wrap around
            if p['y'] < -10:
                p['y'] = self.height + 10
                p['x'] = random.randint(0, self.width)
    
    def draw(self, screen):
        """Draw all background effects."""
        # Draw grid pattern (generated every frame)
        screen.blit(self._create_grid_surface(), (0, 0))
        
        # Draw particles
        for p in self.particles:
            color_with_alpha = (*p['color'], p['alpha'])
            particle_surface = pygame.Surface((p['size'] * 2, p['size'] * 2), pygame.SRCALPHA)
            pygame.draw.circle(particle_surface, color_with_alpha, (p['size'], p['size']), p['size'])
            screen.blit(particle_surface, (int(p['x']) - p['size'], int(p['y']) - p['size']))
        
        # Draw scanlines on top (generated every frame)
        screen.blit(self._create_scanline_surface(), (0, 0))


class ScreenShake:
    """Optimized screen shake effect for game-end moments."""
    
    def __init__(self):
        self.shake_amount = 0
        self.shake_decay = 0.9
        self.offset_x = 0
        self.offset_y = 0
        self.is_shaking = False
    
    def trigger(self, intensity=15):
        """Trigger a screen shake."""
        self.shake_amount = intensity
        self.is_shaking = True
    
    def update(self):
        """Update shake offset."""
        if self.shake_amount > 0.5:
            self.offset_x = random.uniform(-self.shake_amount, self.shake_amount)
            self.offset_y = random.uniform(-self.shake_amount, self.shake_amount)
            self.shake_amount *= self.shake_decay
        else:
            self.offset_x = 0
            self.offset_y = 0
            self.shake_amount = 0
            self.is_shaking = False
    
    def get_offset(self):
        """Get current shake offset."""
        return (int(self.offset_x), int(self.offset_y))



