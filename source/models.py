

class Piece(object):
	'''Abstract object to define the pieces used in the algorithm'''
	name = ''
	attack_positions = []
	position = None
	board = None

	def __init__(self, piece_name, board):
		self.name = piece_name.title()
		self.board = board
		self.attack_positions = []
	
	def set_position(self, position):
		self.position = position
		self.set_attack_positions()

	def set_attack_positions(self):
		'''Return the attacks positions from the piece '''
		if self.board is None:
			raise ValueError('Board must be defined so can generate the attack positions')

		if self.name.lower() == 'rook':
			self.rook_moves()

		if self.name.lower() == 'horse':
			self.knight_moves()

		if self.name.lower() == 'bishop':
			self.bishop_moves()

		if self.name.lower() == 'king':
			self.king_moves()

		if self.name.lower() == 'queen':
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

	def clear(self):
		self.attack_positions = []

	def __str__(self):
		return self.name

class Board(object):
	'''Abstract object to define the board where the pieces will be played'''
	x = 0
	y = 0
	pieces = []
	board_positions = []
	empty_spaces = []
	pieces_in_board = []

	COUNT = 0

	def __init__(self, x, y):
		'''Constructor already set the length (y) and the width (x) of the board'''
		self.x = x
		self.y = y

		for x in range(0, self.x):
			for y in range(0,self.y):
				self.board_positions.append(Position(x,y))

	def add_piece(self, piece_name):
		'''Add one piece to the game'''
		self.pieces.append(Piece(piece_name,self))

	def set_piece(self,piece, position):
		'''Set a location for one piece'''
		piece.set_position(position)
		self.pieces_in_board.append(piece)

	def get_piece_name(self, position):
		'''Returns the piece name from the location'''
		for piece in self.pieces:
			if piece.position == position:
				return piece.name

	def show(self):
		'''Show on the console the board result'''
		for x in range(0, self.x):
			line = ''
			for y in range(0, self.y):
				occupied = self.is_occupied(Position(x,y))
				if occupied == 1:
					line = line + ' ' + self.get_piece_name(Position(x,y))[0:1] + ' |'
				elif occupied == 2:
					line = line + ' x |'
				else:
					line = line + ' _ |'
			print(line)

	def is_occupied(self, position):
		'''
		Validates if a position is occupied or not
		:param position: The position that will be validate
		:return: 1 if there is another piece in there
				 2 if the position is in the area of attack of another piece
				 0 if it's empty
		'''
		value = 0
		for oc in self.pieces_in_board:
			if oc.position == position:
				return 1

		if not value:
			for oc in self.pieces_in_board:
				for at_space in oc.attack_positions:
					if at_space == position:
						return 2
		return 0

	def will_harm(self, piece, pos):
		'''
		Validate if place a piece in the position will harm another piece already on the board
		:param piece: The piece will be placed
		:param pos: The position
		:return: 1 if will harm
				 0 if will not
		'''
		piece.set_position(pos)
		for piece_on_board in self.pieces_in_board:
			for pos_att in piece.attack_positions:
				if piece_on_board.position == pos_att:
					return 1
		return 0

	def set_play(self, count):
		'''Simulates the rotation of pieces in the board'''
		piece = self.pieces[count]
		for pos in self.board_positions:
			if self.is_occupied(pos) == 0:
				if self.will_harm(piece, pos):
					piece.clear()
				else:
					self.set_piece(piece, pos)
					if count + 1 < len(self.pieces):
						self.set_play(count+1)
					else:
						self.show()
					piece.clear()
					print('-------------')

			if count == 0:
				self.clear()
		print('NEXT ROUND')



	def clear(self):
		'''Clear data from the board object'''
		self.pieces_in_board = []
		for piece in self.pieces:
			piece.attack_positions = []

	def push(self, target):
		'''Pushes the target to the empty spaces avoiding duplication'''
		if len(self.empty_spaces) > 0:
			for pos in self.empty_spaces:
				if pos == target:
					return
		if target.x < self.x and target.y < self.y:
			if target.x >= 0 and target.y >= 0:
				self.empty_spaces.append(target)

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
