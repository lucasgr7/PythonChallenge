"""
Lucas Garcia Ribeiro - 18/08/2016
This Module is used to calculate an algorithm of proccess of chess.
It uses to calculate how many positions of any size board can fill with pices
into positions that no one can theath each other.
"""
import copy

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
        '''
        Define a position for the Piece
        :param position: The position that Piece will take place
        '''
        self.position = position
        self.set_attack_positions()

    def set_attack_positions(self):
        '''Set the attacks positions from the piece using the name to identify the type'''
        if self.board is None:
            raise ValueError('Board must be defined so can generate the attack positions')

        if self.name.lower() == 'rook':
            self.rook_moves()

        if self.name.lower() == 'knight':
            self.knight_moves()

        if self.name.lower() == 'bishop':
            self.bishop_moves()

        if self.name.lower() == 'king':
            self.king_moves()

        if self.name.lower() == 'queen':
            self.rook_moves()
            self.bishop_moves()

    def rook_moves(self):
        '''Fill the list attack_position of the Rook on the board'''
        for position_x in range(0, self.board.x):
            self.push(Position(position_x, self.position.y))
            for position_y in range(0, self.board.y):
                self.push(Position(self.position.x, position_y))

    def knight_moves(self):
        '''Fill the list attack_position of the Knight on the board'''
        self.push(Position(self.position.x + 2, self.position.y - 1))
        self.push(Position(self.position.x + 2, self.position.y + 1))
        self.push(Position(self.position.x - 2, self.position.y + 1))
        self.push(Position(self.position.x - 2, self.position.y - 1))

        self.push(Position(self.position.x + 1, self.position.y - 2))
        self.push(Position(self.position.x + 1, self.position.y + 2))
        self.push(Position(self.position.x - 1, self.position.y + 2))
        self.push(Position(self.position.x - 1, self.position.y - 2))

    def bishop_moves(self):
        '''Fill the list attack_position of the Bishop on the board'''
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
        '''Fill the list attack_position of the King on the board'''
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
        '''
        Push the the position "target" to the list of attack_positions
        Prevents duplications validating previous values on the list
        '''
        if len(self.attack_positions) > 0:
            for at_positions in self.attack_positions:
                if at_positions == target:
                    return
        if target != self.position and target.x < self.board.x and target.y < self.board.y:
            if target.x >= 0 and target.y >= 0:
                self.attack_positions.append(target)

    def clear(self):
        '''Clear all the attack_positions of this piece'''
        self.attack_positions = []

    def __str__(self):
        return self.name + ' ' + str(self.position)

class Board(object):
    '''Object to define the board where the pieces will be played'''
    x = 0
    y = 0
    pieces = []
    board_positions = []
    pieces_in_board = []
    saved_plays = []
    iterations = 0
    count_saved_plays = 0

    def __init__(self, position_x, position_y):
        '''Constructor already set the length (y) and the width (x) of the board'''
        self.x = position_x
        self.y = position_y

        for position_x in range(0, self.x):
            for position_y in range(0, self.y):
                self.board_positions.append(Position(position_x, position_y))

    def add_piece(self, piece_name):
        '''Add one piece to the game'''
        self.pieces.append(Piece(piece_name, self))

    def set_piece(self, piece, position):
        '''Set a location for one piece'''
        piece.set_position(position)
        if piece not in self.pieces_in_board:
            self.pieces_in_board.append(piece)

    def get_piece_name(self, position):
        '''Returns the piece name from the location'''
        for piece in self.pieces_in_board:
            if piece.position == position:
                if piece.name.lower() == 'knight':
                    return 'N'
                else:
                    return piece.name

        return '_'

    def show_play(self, play):
        '''Show on the console the play'''
        self.pieces_in_board = play
        for positon_x in range(0, self.x):
            line = ''
            for position_y in range(0, self.y):
                occupied = self.is_occupied(Position(positon_x, position_y))
                if occupied == 1:
                    line = line + ' ' + self.get_piece_name(
                        Position(positon_x, position_y)
                    )[0:1] + ' |'
                elif occupied == 2:
                    line = line + ' _ |'
                else:
                    line = line + ' _ |'
            print(line)
        print('-----------')

    def is_occupied(self, position):
        '''
        Validates if a position is occupied or not
        :param position: The position that will be validate
        :return: 1 if there is another piece in there
                 2 if the position is in the area of attack of another piece
                 0 if it's empty
        '''
        value = 0
        for piece in self.pieces_in_board:
            if piece.position == position:
                return 1
            for at_space in piece.attack_positions:
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
        #for each position on the board will passes the piece
        for pos in self.board_positions:
            self.iterations += 1
            #if the position is not occupied and either is an attack position of
            # other piece
            if self.is_occupied(pos) == 0:
                #check if this piece placed will threat another piece
                if not self.will_harm(piece, pos):
                    self.set_piece(piece, pos)
                    #if there is another piece will find a position for it
                    if count + 1 < len(self.pieces):
                        self.set_play(count +1)
                    #if isn't another piece save the play
                    else:
                        self.save_play()
                piece.clear()

            if count == 0:
                self.clear()
        #in the end of a looping removes the piece from the board
        if len(self.pieces_in_board) > 0:
            self.pieces_in_board.pop(len(self.pieces_in_board)-1)

    def save_play(self):
        '''Save the play as a approved positioning of the pieces'''
        if len(self.saved_plays) > 0:
            for play in self.saved_plays:
                repet = 0
                for board_piece in self.pieces_in_board:
                    for saved_piece in play:
                        if board_piece.name == saved_piece.name and board_piece.position == saved_piece.position:
                            repet += 1
                if repet == len(self.pieces_in_board):
                    return

        self.saved_plays.append(copy.deepcopy(self.pieces_in_board))
        self.count_saved_plays += 1

    def clear(self):
        '''Clear data from the board object'''
        self.pieces_in_board = []

class Position(object):
    '''Abstract object to define positions in the board'''
    x = 0
    y = 0

    def __init__(self, position_x, position_y):
        '''Constructor already set the postion vertical (y) and the horizontal (x)'''
        self.x = position_x
        self.y = position_y

    def __str__(self):
        return ' x : {0} y : {1}'.format(self.x, self.y)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
