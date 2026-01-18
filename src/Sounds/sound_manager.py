
import pygame
import os

class SoundManager:

    def __init__(self):
        self.sound_paths = {}
        self.init_sounds()
        
    def init_sounds(self):
        try:
            # Check if mixer is initialized, if not, init it
            if not pygame.mixer.get_init():
                pygame.mixer.init()
                
            base_path = os.path.join("src", "Sounds")
            
            # Store sound paths
            self.sound_paths["bg_music"] = os.path.join(base_path, "bg_music.mp3")
            self.sound_paths["button"] = os.path.join(base_path, "button_sfx.mp3")
            self.sound_paths["place"] = os.path.join(base_path, "place_sound.mp3")
            self.sound_paths["game_end"] = os.path.join(base_path, "game_end_sfx.mp3")
            
            # Start bg music immediately
            if os.path.exists(self.sound_paths["bg_music"]):
                self.play_bg_music()
            
        except Exception as e:
            print(f"Error initializing sounds: {e}")

    def play_bg_music(self):
        path = self.sound_paths.get("bg_music")
        if path and os.path.exists(path):
            try:
                pygame.mixer.music.load(path)
                pygame.mixer.music.set_volume(0.01) 
                pygame.mixer.music.play(-1) # Loop indefinitely
            except Exception as e:
                print(f"Error playing background music: {e}")

    def play_button_click(self):
        path = self.sound_paths.get("button")
        if path and os.path.exists(path):
            try:
                sound = pygame.mixer.Sound(path)
                sound.play()
            except: pass

    def play_place_sound(self):
        path = self.sound_paths.get("place")
        if path and os.path.exists(path):
            try:
                sound = pygame.mixer.Sound(path)
                sound.play()
            except: pass
            
    def play_game_end_sound(self):
        path = self.sound_paths.get("game_end")
        if path and os.path.exists(path):
            try:
                sound = pygame.mixer.Sound(path)
                sound.play()
            except: pass
