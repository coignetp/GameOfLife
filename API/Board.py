import pygame

class Board:
	"""
	Board game with the different cells
	"""

	def __init__(self, width=10, height=10, state=[' ', 'X'], window=False):
		""" Init the class """
		self.width = width
		self.height = height
		self.state = state
		self.dimension = 2

		self.cellWidth = 5
		self.cellHeight = 5

		if window:
			self.initWindow()

		# Simple board
		self.board = [[0 for _ in range(width)] for _ in range(height)]

	def update(self, f, turn=1):
		""" Update the board of n turns """

		while turn > 0:
			self.board = f(self.board, (self.height,self.width), len(self.state))
			turn -= 1

	def printConsole(self):
		""" Print the board to the console """

		print("+" + "-"*self.width + "+")

		for i in range(0, self.height):
			print('|', end='')
			for j in range(0, self.width):
				print(self.state[self.board[i][j]], end='')
			print('|')

		print("+" + "-"*self.width + "+")

	def initWindow(self):
		pygame.init()
		self.screen = pygame.display.set_mode((self.width*self.cellWidth, self.height*self.cellHeight))

	def printWindow(self):
		""" Print the board to the window
		thanks to pygame. Only with 2D """

		if self.dimension != 2:
			return

		self.screen.fill((255, 255, 255))

		for i in range(0, len(self.board)):
			for j in range(0, len(self.board[i])):
				if self.board[i][j] == 1:
					pygame.draw.rect(self.screen, (0, 0, 0), ((j*self.cellWidth, i*self.cellHeight), (self.cellWidth, self.cellHeight)), 0)

		#pygame.display.update()
		pygame.display.flip()
		#clock.tick(20)