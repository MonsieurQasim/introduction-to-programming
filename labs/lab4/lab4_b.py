from random import randint, random
import random
original = tuple([num for num in range(1, 16)]) 

indexes = [i for i in range(len(original))]

while True:
    random.shuffle(indexes)

    inversions = 0
    for i in range(len(indexes)):
        for j in range(i + 1, len(indexes)):
            if indexes[i] > indexes[j]:
                inversions += 1

    if inversions % 2 == 0:
        break

# create board shuffled indexes
board = []
for i in range(len(indexes)):
    board.append(original[indexes[i]])
 
board.append('_')

# SOLVING

while True:

    print()
    for i in range(len(board)):
        print(f'{board[i]:>3}', end=' ')
        if (i + 1) % 4 == 0:
            print()
    print()

    solved = True
    for i in range(len(original)):
        if board[i] != original[i]:
            solved = False
            break
    if solved:
        print("Puzzle solved!")
        break

    chosen_index = int(input("Enter the slot number to move: "))

    blank_index = board.index('_')

    # check
    same_row = (chosen_index // 4 == blank_index // 4 and
                abs(chosen_index - blank_index) == 1)

    same_column = abs(chosen_index - blank_index) == 4

    if same_row or same_column:
        # swap
        board[blank_index], board[chosen_index] = board[chosen_index], board[blank_index]