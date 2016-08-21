'''
Class to run the console application to use the algorithm for the Python Challenge
'''
import time
import os

from source.models import Board

class console_application(object):
    '''Class to store methods of the application'''
    queens = 0
    bishops = 0
    kings = 0
    knights = 0
    rooks = 0
    board_x = 0
    board_y = 0
    def show_welcome_page(self):
        '''Prints a welcome page with instructions on the console terminal'''
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
        '''Print instructions to add piece to the process
        and return the quantity used by the user'''
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
        '''
        Method that shows a message to the user and return the input converted to int
        :param message: static message that always show with 1 arg
        :param name: The dinamic value from the static message
        :return: int informed by the user
        '''
        os.system('cls')
        print message.format(name)
        in_input = raw_input()
        return int(in_input)

    def show_message_set_board(self, value):
        '''Print instructions to set the board specifications'''
        message = 'Please set the {0} of the board'
        if value == 6:
            self.board_y = self.input_message(message, 'Height (Y)')
        if value == 7:
            self.board_x = self.input_message(message, 'Height (X)')

APP = console_application()
APP.show_welcome_page()
IN_INPUT = raw_input()
while IN_INPUT != '0':
    if IN_INPUT != '':
        VALUE_INPUT = int(IN_INPUT)
        if VALUE_INPUT > 0 and VALUE_INPUT < 6:
            APP.add_piece(VALUE_INPUT)
        elif VALUE_INPUT == 6 or VALUE_INPUT == 7:
            APP.show_message_set_board(VALUE_INPUT)
        elif VALUE_INPUT == 8:
            print 'Processing please wait...'
            BOARD = Board(APP.board_x, APP.board_y)
            for rook in range(0, APP.rooks):
                BOARD.add_piece('Rook')
            for queen in range(0, APP.queens):
                BOARD.add_piece('Queen')
            for bishop in range(0, APP.bishops):
                BOARD.add_piece('Bishop')
            for king in range(0, APP.kings):
                BOARD.add_piece('King')
            for knight in range(0, APP.knights):
                BOARD.add_piece('Knight')
            if BOARD.x > 0 and BOARD.y > 0:
                START = time.time()
                BOARD.set_play(0)
                END = time.time()
                print 'Number of possible plays : {0}'.format(BOARD.count_saved_plays)
                print 'Number of iterations : {0}'.format(BOARD.iterations)
                print 'Time elapsed : {0} seconds'.format(str(END - START))
                print 'Do you wish to see configurations sets? Y/N'
                X_INPUT = raw_input()
                if X_INPUT.lower() == 'y':
                    COUNT = 0
                    for configuration_set in BOARD.saved_plays:
                        BOARD.show_play(configuration_set)
                        COUNT += 1
                        print 'Number: {0}'.format(COUNT)
                        print '\n'

                print 'Press ENTER to continue'
                raw_input()
            else:
                print 'Sorry the board needs to have length and height to calculate!'
                print 'Try again :)'



    APP.show_welcome_page()
    IN_INPUT = raw_input()
