import numpy as n
from API.Board import Board
from API.RuleConway import RuleConway
from API.Rule import Rule
from random import randint

# Size of the board
width = 10
height = 10

board = [[0 for _ in range(width)] for _ in range(height)]

# Random board
for i in range(len(board)):
	for j in range(len(board[i])):
		board[i][j] = randint(0,1)

# Game
b = Board(width, height)
b.board = board
r = RuleConway()

for _ in range(10):
	b.printConsole()
	b.update(r.update)

b.printConsole()