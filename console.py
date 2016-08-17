from source.models import Board, Piece, Position

board = Board(4,4)
piece = Piece('queen', board, 2,2)

for position in piece.attack_positions:
	print(position)