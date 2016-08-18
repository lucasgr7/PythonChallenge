from source.models import Board, Piece, Position

board = Board(3,3)
board.add_piece('rook')
board.add_piece('king')
board.add_piece('king')

board.set_play(0)
board.clear()
