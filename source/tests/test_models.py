import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import unittest

from models import Board, Piece, Position

class TestPieces(unittest.TestCase):

	def test_push_duplicate_values(self):
		piece = Piece(None, Board(2,2))
		a = Position(1,1)
		b = Position(1,0)
		c = Position(1,0)
		piece.push(a)
		piece.push(b)
		piece.push(c)
		self.assertEqual(2,len(piece.attack_positions))

	def test_rook_attack_positions(self):
		board = Board(4,4)
		piece = Piece('Rook', board, 1,1)
		self.assertEqual(6,len(piece.attack_positions))

	def test_knight_attack_positions(self):
		board = Board(3,3)
		piece = Piece('Knight', board, 1,1)
		self.assertEqual(0, len(piece.attack_positions))
		piece = Piece('Knight' , board, 0,2)
		self.assertEqual(2, len(piece.attack_positions))

	def test_bishop_attack_positions(self):
		board = Board(4,4)
		piece = Piece('Bishop', board, 1,1)
		self.assertEqual(5,len(piece.attack_positions))

	def test_king_attack_positions(self):
		board = Board(4,4)
		piece = Piece('King', board, 1,1)
		self.assertEqual(8,len(piece.attack_positions))
		piece = Piece('King', board, 0,0)
		self.assertEqual(3,len(piece.attack_positions))



suite = unittest.TestLoader().loadTestsFromTestCase(TestPieces)
unittest.TextTestRunner(verbosity=2).run(suite)