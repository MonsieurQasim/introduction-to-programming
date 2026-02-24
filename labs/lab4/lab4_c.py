# For this task Copilot was used to generate the code with the following prompt:
# now generate another 4x4 board game, just like the previous board game, but a new one, you can chose which is the most famous one you know

from random import randint

# ----------------------------
# PREPARATION PHASE
# ----------------------------

board = []

# create 4x4 board with random 0/1 values
for i in range(4):
    row = []
    for j in range(4):
        row.append(randint(0, 1))
    board.append(row)

# ----------------------------
# GAME LOOP
# ----------------------------

while True:

    # print board
    print()
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=' ')
        print()
    print()

    # check if solved (all zeros)
    solved = True
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                solved = False

    if solved:
        print("All lights are OFF. You solved the puzzle!")
        break

    # ask user for row and column
    r = int(input("Enter row (0-3): "))
    c = int(input("Enter column (0-3): "))

    # toggle chosen cell
    if board[r][c] == 1:
        board[r][c] = 0
    else:
        board[r][c] = 1

    # toggle UP
    if r - 1 >= 0:
        if board[r-1][c] == 1:
            board[r-1][c] = 0
        else:
            board[r-1][c] = 1

    # toggle DOWN
    if r + 1 < 4:
        if board[r+1][c] == 1:
            board[r+1][c] = 0
        else:
            board[r+1][c] = 1

    # toggle LEFT
    if c - 1 >= 0:
        if board[r][c-1] == 1:
            board[r][c-1] = 0
        else:
            board[r][c-1] = 1

    # toggle RIGHT
    if c + 1 < 4:
        if board[r][c+1] == 1:
            board[r][c+1] = 0
        else:
            board[r][c+1] = 1