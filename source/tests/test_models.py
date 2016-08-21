'''
Module for tests in the algorithm in the Python Challenge
'''
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import unittest

from models import Board, Piece, Position

class TestModels(unittest.TestCase):
    '''Unit test classes'''
    def test_push_duplicate_values(self):
        '''Test if duplicate values on pieces attack positions'''
        board = Board(3, 3)
        piece = Piece(None, Board(2, 2))
        piece.position = Position(2, 2)
        a = Position(1, 1)
        b = Position(1, 0)
        c = Position(1, 0)
        piece.push(a)
        piece.push(b)
        piece.push(c)
        self.assertEqual(2, len(piece.attack_positions))

    def test_rook_attack_positions(self):
        '''Test the attack positions of the Rook'''
        board = Board(4, 4)
        board.pieces = []
        board.add_piece('Rook')
        piece = board.pieces[0]
        board.set_piece(piece, Position(1, 1))
        self.assertEqual(6, len(piece.attack_positions))

    def test_knight_attack_positions(self):
        '''Test the attack positions of the Knight'''
        board = Board(3, 3)
        board.add_piece('Knight')
        piece = board.pieces[0]
        board.set_piece(piece, Position(1, 1))
        self.assertEqual(0, len(piece.attack_positions))

        board.clear()
        board.set_piece(piece, Position(0, 2))
        self.assertEqual(2, len(piece.attack_positions))

    def test_bishop_attack_positions(self):
        '''Test the attack positions of the Bishop'''
        board = Board(4, 4)
        board.add_piece('Bishop')
        piece = board.pieces[0]
        board.set_piece(piece, Position(1, 1))
        self.assertEqual(5, len(piece.attack_positions))

    def test_king_attack_positions(self):
        '''Test the attack positions of the King'''
        board = Board(4, 4)
        board.add_piece('King')
        piece = board.pieces[0]
        board.set_piece(piece, Position(1, 1))
        self.assertEqual(8, len(piece.attack_positions))

        board = Board(4, 4)
        board.add_piece('King')
        piece = board.pieces[0]
        board.set_piece(piece, Position(0, 0))
        self.assertEqual(3, len(piece.attack_positions))

    def test_queen_attack_positions(self):
        '''Test the attack positions of the Queen'''
        board = Board(3, 3)
        board.add_piece('Queen')
        piece = board.pieces[0]
        board.set_piece(piece, Position(1, 1))
        self.assertEqual(8, len(piece.attack_positions))

        board = Board(5, 5)
        board.add_piece('Queen')
        piece = board.pieces[0]
        board.set_piece(piece, Position(2, 2))
        self.assertEqual(16, len(piece.attack_positions))

    def test_get_piece_name(self):
        '''Test method to read the piece positions'''
        board = Board(3, 3)
        board.add_piece('Rook')
        board.add_piece('King')
        board.add_piece('Queen')
        rook = board.pieces[0]
        king = board.pieces[1]
        queen = board.pieces[2]
        board.set_piece(rook, Position(0, 0))
        board.set_piece(king, Position(1, 2))
        board.set_piece(queen, Position(2, 2))
        self.assertEqual('Rook', board.get_piece_name(Position(0, 0)))
        self.assertEqual('King', board.get_piece_name(Position(1, 2)))
        self.assertEqual('Queen', board.get_piece_name(Position(2, 2)))
        self.assertEqual('_', board.get_piece_name(Position(1, 1)))

    def test_piece_positioning(self):
        '''Test if the positioning is validated correctly'''
        board = Board(3, 3)
        board.add_piece('Bishop')
        board.add_piece('Rook')
        bishop = board.pieces[0]
        rook = board.pieces[1]

        #Bishop will be placed at 0,0
        bishop_position = Position(0, 0)

        #The position should be free since we're starting
        self.assertEqual(0, board.is_occupied(bishop_position))
        board.set_piece(bishop, bishop_position)

        #After placing the bishop expected to be occupied
        self.assertEqual(1, board.is_occupied(bishop_position))

        #Expedted to the bishop attack the postions (1,1), (2,2)
        #The return should be 2 since there is no piece, but its in
        #the attack area of another piece
        self.assertEqual(2, board.is_occupied(Position(1, 1)))
        self.assertEqual(2, board.is_occupied(Position(2, 2)))

        #Test if i put the Rook on (0,1) will harm the Bishop, what sould be true
        self.assertEqual(1, board.will_harm(rook, Position(0, 1)))

        rook_position = Position(1, 2)
        #Verify the position (1,2) where is empty and should not harm the bishop
        self.assertEqual(0, board.is_occupied(rook_position))
        self.assertEqual(1, board.will_harm(rook,rook_position))

        #Place it
        board.set_piece(rook, rook_position)
        self.assertEqual(1, board.is_occupied(rook_position))

    def test_save_play(self):
        '''Test if the method save_play doesn't allow duplicated results'''
        board = Board(2, 2)
        board.add_piece('Rook')
        board.add_piece('Knight')
        rook = board.pieces[0]
        knight = board.pieces[1]
        board.set_piece(rook, Position(0, 0))
        board.set_piece(knight, Position(1, 1))

        #Save play uses the array pieces_in_board, it is used to verify
        #pieces positioned on the board
        self.assertEqual(2, len(board.pieces_in_board))

        #Tries to save twice
        board.save_play()
        board.save_play()

        #Expected to be saved only one
        self.assertEqual(1, board.count_saved_plays)


    def test_play_01(self):
        '''Test the play with 4 kings in one board 3x3 expected 1 play to be possible'''
        board = Board(3, 3)
        board.add_piece('King')
        board.add_piece('King')
        board.add_piece('King')
        board.add_piece('King')
        board.set_play(0)
        self.assertEqual(1, len(board.saved_plays))

    def test_play_02(self):
        '''Test the play with 2 Kings and 1 Rook Board 3x3, expected 4 to be true'''
        board = Board(3, 3)
        board.add_piece('King')
        board.add_piece('King')
        board.add_piece('Rook')
        board.set_play(0)
        self.assertEqual(4, len(board.saved_plays))

    def test_play_03(self):
        '''Test the play with 4 Knights and 2 Rooks Board 4x4, expected 8 to be true'''
        board = Board(4, 4)
        board.add_piece('Knight')
        board.add_piece('Knight')
        board.add_piece('Knight')
        board.add_piece('Knight')
        board.add_piece('Rook')
        board.add_piece('Rook')
        board.set_play(0)
        self.assertEqual(8, len(board.saved_plays))

    def test_play_04(self):
        '''Test the play with 3 kings in one board 3x3 expected 1 play to be possible'''
        board = Board(3, 3)
        board.add_piece('King')
        board.add_piece('King')
        board.add_piece('King')
        board.set_play(0)
        self.assertEqual(8, len(board.saved_plays))

suite = unittest.TestLoader().loadTestsFromTestCase(TestModels)
unittest.TextTestRunner(verbosity=2).run(suite)
