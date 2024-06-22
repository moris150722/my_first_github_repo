import random

def create_board(size, num_mines):
    board = {(row, col): 0 for row in range(size) for col in range(size)}
    mines = random.sample(board.keys(), num_mines)
    for mine in mines:
        board[mine] = -1
        for r in range(mine[0] - 1, mine[0] + 2):
            for c in range(mine[1] - 1, mine[1] + 2):
                if (r, c) in board and board[(r, c)] != -1:
                    board[(r, c)] += 1
    return board

def print_board(board, size):
    for row in range(size):
        for col in range(size):
            cell = board[(row, col)]
            print(f'{cell if cell >= 0 else "X"}', end=' ')
        print()

def play_minesweeper(size, num_mines):
    board = create_board(size, num_mines)
    print("Welcome to Minesweeper!")
    print_board(board, size)

size = 5  # Board size
num_mines = 5  # Number of mines
play_minesweeper(size, num_mines)
