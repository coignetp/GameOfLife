from API.Rule import Rule
from copy import deepcopy

class RuleConway(Rule):
	"""
	The Game of Life with Conway's Rule
	"""

	def __init__(self):
		""" Initiate Conway's rules """
		Rule.__init__(self, 2)

	def update(self, board, size, numberOfState):
		""" Update the board """
		newBoard = deepcopy(board)

		getState = lambda N, board: board[N[0]][N[1]]

		position = (1,1)

		for i in range(0, len(board)):
			for j in range(0, len(board[i])):
				neigh = self.getNeighbours((i,j), size)
				s = 0
				for n in neigh:
					s += getState(n, board)

				if s == 3:
					newBoard[i][j] = 1
				elif s == 2 and board[i][j] == 1:
					newBoard[i][j] = 1
				else:
					newBoard[i][j] = 0

		return newBoard