# only include game rules: win, lose, draw

class GameRules:
    win_position = [
            [0,1,2], # Row
            [3,4,5],
            [6,7,8],
            [0,3,6], # Column
            [1,4,7],
            [2,5,8],
            [0,4,8], # Diagonal
            [2,4,6]
        ]
    
    def check_winner(grid):
        for pos in GameRules.win_position:
            if (grid[pos[0]] == grid[pos[1]] == grid[pos[2]] and grid[pos[0]] is not None):
                return grid[pos[0]]
        return None
    
    def is_draw(grid):
        return None not in grid and GameRules.check_winner(grid) is None