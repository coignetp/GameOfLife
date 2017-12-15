import numpy as n
import pygame
from API.Board import Board
from API.RuleConway import RuleConway
from API.Rule import Rule
from random import randint

# Size of the board
width = 100
height = 100

board = [[0 for _ in range(width)] for _ in range(height)]

# Random board
for i in range(len(board)):
	for j in range(len(board[i])):
		board[i][j] = randint(0,1)

# Game
b = Board(width, height, [' ', 'X'], True)
b.board = board
r = RuleConway()

"""for _ in range(10):
	b.printConsole()
	b.update(r.update)

b.printConsole()"""

done = False

pygame.key.set_repeat(400, 200)

b.printWindow()

while not done:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					b.update(r.update)
					b.printWindow()