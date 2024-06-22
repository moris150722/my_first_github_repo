def read_board_from_file(filename):
    with open(filename, 'r') as file:
        board = []
        for line in file:
            row = list(map(int, line.strip().split(',')))
            board.append(row)
    return board

def write_board_to_file(board, filename):
    with open(filename, 'w') as file:
        for row in board:
            file.write(','.join(map(str, row)) + '\n')

def candy_crush(board):
    rows, cols = len(board), len(board[0])

    def mark_for_crush():
        crush = False
        # Mark the candies to be crushed horizontally
        for r in range(rows):
            for c in range(cols - 2):
                if board[r][c] and board[r][c] == board[r][c + 1] == board[r][c + 2]:
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
                    crush = True
        
        # Mark the candies to be crushed vertically
        for r in range(rows - 2):
            for c in range(cols):
                if board[r][c] and board[r][c] == board[r + 1][c] == board[r + 2][c]:
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
                    crush = True
        
        return crush

    def apply_gravity():
        for c in range(cols):
            idx = rows - 1
            for r in range(rows - 1, -1, -1):
                if board[r][c] > 0:
                    board[idx][c] = board[r][c]
                    if idx != r:
                        board[r][c] = 0
                    idx -= 1

    while True:
        if not mark_for_crush():
            break
        apply_gravity()

    return board

def main():
    input_filename = 'candy_input.txt'
    output_filename = 'candy_output.txt'
    
    board = read_board_from_file(input_filename)
    stable_board = candy_crush(board)
    write_board_to_file(stable_board, output_filename)

if __name__ == "__main__":
    main()
