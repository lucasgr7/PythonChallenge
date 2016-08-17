

class Piece(object):
	'''Abstract object to define the pieces used in the algorithm'''

	attack_positions = []
	position = None
	board = None

	def __init__(self, piece_name=None, board=None, start_x=0, start_y=0):
		self.board = board
		self.position = Position(start_x, start_y)
		self.attack_positions = []
		if piece_name != None:
			self.set_attack_positions(piece_name)


	def set_attack_positions(self, piece_name):
		'''Return the positions that the piece attacks'''
		if self.board is None:
			raise ValueError('Board must be defined so can generate the attack positions')

		if piece_name.lower() == 'rook':
			self.rook_moves()

		if piece_name.lower() == 'knight':
			self.knight_moves()

		if piece_name.lower() == 'bishop':
			self.bishop_moves()

		if piece_name.lower() == 'king':
			self.king_moves()

		if piece_name.lower() == 'queen':
			self.rook_moves()
			self.bishop_moves()

	def rook_moves(self):
		for x in range(0, self.board.x):
			self.push(Position(x, self.position.y))
			for y in range(0, self.board.y):
				self.push(Position(self.position.x, y))

	def knight_moves(self):
		self.push(Position(self.position.x + 2, self.position.y - 1))
		self.push(Position(self.position.x + 2, self.position.y + 1))
		self.push(Position(self.position.x - 2, self.position.y + 1))
		self.push(Position(self.position.x - 2, self.position.y - 1))

		self.push(Position(self.position.x + 1, self.position.y - 2))
		self.push(Position(self.position.x + 1, self.position.y + 2))
		self.push(Position(self.position.x - 1, self.position.y + 2))
		self.push(Position(self.position.x - 1, self.position.y - 2))

	def bishop_moves(self):
		lux = self.position.x
		luy = self.position.y
		rux = self.position.x
		ruy = self.position.y
		ldx = self.position.x
		ldy = self.position.y
		rdx = self.position.x
		rdy = self.position.y
		for x in range(0, self.board.x + self.board.y):
			lux -= 1
			luy -= 1
			self.push(Position(lux, luy))
			rux -= 1
			ruy += 1
			self.push(Position(rux, ruy))
			ldx += 1
			ldy += 1
			self.push(Position(ldx, ldy))
			rdx += 1
			rdy -= 1
			self.push(Position(rdx, rdy))

	def king_moves(self):
		self.push(Position(self.position.x - 1, self.position.y - 1))
		self.push(Position(self.position.x - 1, self.position.y))
		self.push(Position(self.position.x - 1, self.position.y + 1))
		self.push(Position(self.position.x - 1, self.position.y - 1))
		self.push(Position(self.position.x, self.position.y - 1))
		self.push(Position(self.position.x, self.position.y + 1))
		self.push(Position(self.position.x + 1, self.position.y - 1))
		self.push(Position(self.position.x + 1, self.position.y))
		self.push(Position(self.position.x + 1, self.position.y + 1))


	def push(self, target):
		if len(self.attack_positions) > 0:
			for at_positions in self.attack_positions:
				if at_positions == target:
					return
		if target != self.position and target.x < self.board.x and target.y < self.board.y:
			if target.x >= 0 and target.y >= 0:
				self.attack_positions.append(target)

class Board(object):
	'''Abstract object to define the board where the pieces will be played'''
	x = 0
	y = 0

	def __init__(self, x, y):
		'''Constructor already set the length (y) and the width (x) of the board'''
		self.x = x
		self.y = y

class Position(object):
	'''Abstract object to define positions in the board'''
	x = 0
	y = 0

	def __init__(self, x, y):
		'''Constructor already set the postion vertical (y) and the horizontal (x)'''
		self.x = x
		self.y = y

	def __str__(self):
		return ' x : {0} y : {1}'.format(self.x, self.y)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__
