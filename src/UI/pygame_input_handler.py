import pygame

class PygameInputHandler:
    """
    Handle mouse input for pygame version of Tic-Tac-Toe.
    Converts mouse clicks on the board to cell indices (0-8).
    """

    def __init__(self, screen):
        """
        Initialize the pygame input handler.

        Args:
            screen: pygame screen object to get dimensions
        """
        self.screen = screen
        self.WIDTH, self.HEIGHT = screen.get_size()

        # Board dimensions (must match pygame_board.py)
        self.board_size = 300
        self.cell_size = self.board_size // 3
        self.board_x = (self.WIDTH - self.board_size) // 2
        self.board_y = (self.HEIGHT - self.board_size) // 2

    def get_cell_from_pos(self, pos):
        """
        Convert mouse position to cell index (0-8).

        Args:
            pos: tuple (x, y) - mouse position

        Returns:
            int: cell index (0-8) if click is on board, None otherwise
        """
        mouse_x, mouse_y = pos

        # Check if click is within board bounds
        if (self.board_x <= mouse_x <= self.board_x + self.board_size and
            self.board_y <= mouse_y <= self.board_y + self.board_size):

            # Calculate which cell was clicked
            col = (mouse_x - self.board_x) // self.cell_size
            row = (mouse_y - self.board_y) // self.cell_size

            # Convert row, col to index (0-8)
            # Board layout:
            # 0 1 2
            # 3 4 5
            # 6 7 8
            index = row * 3 + col

            return index

        return None


