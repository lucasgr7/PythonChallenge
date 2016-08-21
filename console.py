import time
import os

from source.models import Board

class console_app(object):
    queens = 0
    bishops = 0
    kings = 0
    knights = 0
    rooks = 0
    board_x = 0
    board_y = 0
    def show_welcome_page(self):
        os.system('cls')
        print 'Welcome - Python Challenge'
        print 'By Lucas Garcia Ribeiro - 21/08/2016'
        print '\n'
        print 'Please choose an option'
        print '\n'
        print '1 - Add Queen ({0})'.format(self.queens)
        print '2 - Add Bishop ({0})'.format(self.bishops)
        print '3 - Add King ({0})'.format(self.kings)
        print '4 - Add Knight ({0})'.format(self.knights)
        print '5 - Add Rook ({0})'.format(self.rooks)
        print '-----'
        print '6 - Height Board (y) ({0})'.format(self.board_y)
        print '7 - Width Board (x) ({0})'.format(self.board_x)
        print '-----'
        print '8 - Calculate'
        print '0 - Exit'

    def add_piece(self, id_piece):
        message = 'How many {0} do you wish?'
        if id_piece == 1:
            self.queens = self.input_message(message, 'queens')
        elif id_piece == 2:
            self.bishops = self.input_message(message, 'bishops')
        elif id_piece == 3:
            self.kings = self.input_message(message, 'kings')
        elif id_piece == 4:
            self.knights = self.input_message(message, 'knights')
        elif id_piece == 5:
            self.rooks = self.input_message(message, 'rooks')

    def input_message(self, message, name):
        os.system('cls')
        print message.format(name)
        in_input = raw_input()
        return int(in_input)

    def show_message_set_board(self, value):
        message = 'Please set the {0} of the board'
        if value == 6:
            self.board_y = self.input_message(message, 'Height (Y)')
        if value == 7:
            self.board_x = self.input_message(message, 'Height (X)')

app = console_app()
app.show_welcome_page()
in_input = raw_input()
while in_input != '0':
    if in_input != '':
        value_input = int(in_input)
        if value_input > 0 and value_input < 6:
            app.add_piece(value_input)
        elif value_input == 6 or value_input == 7:
            app.show_message_set_board(value_input)
        elif value_input == 8:
            print 'Processing please wait...'
            board = Board(app.board_x, app.board_y)
            for rook in range(0, app.rooks):
                board.add_piece('Rook')
            for queen in range(0, app.queens):
                board.add_piece('Queen')            
            for bishop in range(0, app.bishops):
                board.add_piece('Bishop')            
            for king in range(0, app.kings):
                board.add_piece('King')            
            for knight in range(0, app.knights):
                board.add_piece('Knight')
            if board.x > 0 and board.y > 0:
                start = time.time()
                board.set_play(0)
                end = time.time()
                print('Number of possible plays : {0}'.format(board.count_saved_plays))
                print('Number of iterations : {0}'.format(board.iterations))
                print('Time elapsed : {0} seconds'.format(str(end-start)))
                print('Do you wish to see configurations sets? Y/N')
                x_input = raw_input()
                if x_input.lower() == 'y':
                    count = 0
                    for configuration_set in board.saved_plays:
                        board.show_play(configuration_set)
                        count += 1
                        print 'Number: {0}'.format(count)
                        print '\n'

                print('Press ENTER to continue')
                raw_input()
            else:
                print 'Sorry the board needs to have length and height to calculate!'
                print 'Try again :)'



    app.show_welcome_page()
    in_input = raw_input()
