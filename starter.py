#!/usr/bin/env python

print("Hello world")

print("This is a 2 player gmae cause I cant be bothered to make an ai")

# The board
w, h = 3, 3
board = [ [0] * w for _ in range(h)]

# 0 = empty
# 1 = player 1
# 2 = player 2

# Print board
def print_board():
    print(str(board[0][0]) + " | " + str(board[0][1]) + " | " + str(board[0][1]))
    print("---------")
    print(str(board[1][0]) + " | " + str(board[1][1]) + " | " + str(board[1][1]))
    print("---------")
    print(str(board[2][0]) + " | " + str(board[2][1]) + " | " + str(board[2][1]))

print_board()

ended = bool(False)

player_turn = int(1)
# 0 = 0
# 1 = X
