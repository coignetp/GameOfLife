class Board:
	"""
	Board game with the different cells
	"""

	def __init__(self, width=10, height=10, state=[' ', 'X']):
		self.width = width
		self.height = height
		self.state = state