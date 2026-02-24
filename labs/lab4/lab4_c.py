# For this task Copilot was used to generate the code with the following prompt:
# now generate another 4x4 board game, just like the previous board game, but a new one, you can chose which is the most famous one you know

import random
import os

SIZE = 4
TARGET = 2048


def create_board():
    board = [[0] * SIZE for _ in range(SIZE)]
    add_tile(board)
    add_tile(board)
    return board


def add_tile(board):
    empty = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = 4 if random.random() < 0.1 else 2


def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==== 2048 ====\n")
    for row in board:
        for val in row:
            print(f"{val or '.':>6}", end="")
        print("\n")
    print("W/A/S/D to move, Q to quit\n")


def compress(row):
    """Slide non-zero values left."""
    new_row = [x for x in row if x != 0]
    new_row += [0] * (SIZE - len(new_row))
    return new_row


def merge(row):
    """Merge equal neighbors."""
    for i in range(SIZE - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    return row


def move_left(board):
    new_board = []
    moved = False

    for row in board:
        compressed = compress(row)
        merged = merge(compressed)
        final = compress(merged)

        if final != row:
            moved = True

        new_board.append(final)

    return new_board, moved


def reverse(board):
    return [row[::-1] for row in board]


def transpose(board):
    return [list(row) for row in zip(*board)]


def move_right(board):
    board = reverse(board)
    board, moved = move_left(board)
    board = reverse(board)
    return board, moved


def move_up(board):
    board = transpose(board)
    board, moved = move_left(board)
    board = transpose(board)
    return board, moved


def move_down(board):
    board = transpose(board)
    board, moved = move_right(board)
    board = transpose(board)
    return board, moved


def has_won(board):
    return any(cell >= TARGET for row in board for cell in row)


def can_move(board):
    # Empty space exists
    if any(0 in row for row in board):
        return True

    # Horizontal merge possible
    for r in range(SIZE):
        for c in range(SIZE - 1):
            if board[r][c] == board[r][c + 1]:
                return True

    # Vertical merge possible
    for c in range(SIZE):
        for r in range(SIZE - 1):
            if board[r][c] == board[r + 1][c]:
                return True

    return False


def main():
    board = create_board()

    while True:
        print_board(board)

        if has_won(board):
            print("🎉 You reached 2048! You win!")
            break

        if not can_move(board):
            print("💀 No moves left. Game over.")
            break

        move = input("Move: ").lower()

        if move == 'q':
            break
        elif move == 'a':
            new_board, moved = move_left(board)
        elif move == 'd':
            new_board, moved = move_right(board)
        elif move == 'w':
            new_board, moved = move_up(board)
        elif move == 's':
            new_board, moved = move_down(board)
        else:
            continue

        if moved:
            board = new_board
            add_tile(board)


if __name__ == "__main__":
    main()