from game_logic import check_winner  

def test_empty_board_no_winner():
    board = [['' for _ in range(3)] for _ in range(3)]
    assert check_winner(board) is None

def test_x_wins_row():
    board = [['X', 'X', 'X'],
             ['', 'O', ''],
             ['O', '', '']]
    assert check_winner(board) == 'X'
