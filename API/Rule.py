class Rule:
	"""
	Define the rules of the game thanks to
	dimension or next turn condition.
	"""

	def __init__(self, dimension):
		""" Initiate the rules """

		self.dimension = dimension

	def getNeighbours(self, position, size):
		""" Get the different neighbours """
		def allNeighbours(position, size, dimension):
			""" Return every neighbours relative position """
			if dimension <= 1:
				if dimension == self.dimension:
					return [[-1], [1]]
				return [[-1], [0], [1]]

			l = [-1, 0, 1]
			ret = allNeighbours(position, size, dimension-1)
			neigh = [0 for _ in range(0, len(l)*len(ret))]
			for i in range(len(l)):
				for j in range(len(ret)):
					neigh[i*len(ret) + j] = [l[i]] +  ret[j]

			return neigh

		def filterNeighbours(neigh, size, position):
			""" Filter all neighbours available """
			l = []

			for n in neigh:
				ok = True
				for i in range(len(n)):
					if not (0 <= n[i] < size[i]):
						ok = False
				if ok:
					l.append(n)

			if position in l:
				l.remove(position)
			return l

		neigh = allNeighbours(position, size, self.dimension)

		for i in range(0, len(neigh)):
			for j in range(0, len(neigh[i])):
				neigh[i][j] += position[j]

		return filterNeighbours(neigh, size, list(position))

	def update(self, board, size, numberOfState):
		""" Update a board according to the rules """
		return board