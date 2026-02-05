import pygame
from src.UI.pygame_board import get_board_dimensions

class PygameInputHandler:
    """
    Handle mouse input for pygame version of Tic-Tac-Toe.
    Converts mouse clicks on the board to cell indices (0-8).
    """

    def __init__(self, screen):
        self.screen = screen

    def get_cell_from_pos(self, pos):
        mouse_x, mouse_y = pos
        
        board_x, board_y, board_size, cell_size = get_board_dimensions(self.screen)

        # Check if click is within board bounds
        if (board_x <= mouse_x <= board_x + board_size and
            board_y <= mouse_y <= board_y + board_size):

            # Calculate which cell was clicked
            col = (mouse_x - board_x) // cell_size
            row = (mouse_y - board_y) // cell_size
            
            # Convert row, col to index (0-8)
            # Board layout:
            # 0 1 2
            # 3 4 5
            # 6 7 8
            index = row * 3 + col
            
            # Safety check
            if 0 <= index <= 8:
                return index

        return None


