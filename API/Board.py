class Board:
	"""
	Board game with the different cells
	"""

	def __init__(self, width=10, height=10, state=[' ', 'X']):
		""" Init the class """
		self.width = width
		self.height = height
		self.state = state

		# Simple board
		self.board = [[0 for _ in range(width)] for _ in range(height)]

	def printConsole(self):
		""" Print the board to the console """

		print("+" + "-"*self.width + "+")

		for i in range(0, self.height):
			print('|', end='')
			for j in range(0, self.width):
				print(self.state[self.board[i][j]], end='')
			print('|')

		print("+" + "-"*self.width + "+")