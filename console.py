import time

from source.models import Board

board = Board(7, 7)
board.add_piece('Queen')
board.add_piece('Queen')
board.add_piece('Bishop')
board.add_piece('Bishop')
board.add_piece('King')
board.add_piece('King')
board.add_piece('Knight')

start = time.time()

board.set_play(0)

end = time.time()
#for play in board.saved_plays:
#    board.show_play(play)

print('Number of possible plays : {0}'.format(board.count_saved_plays))
print('Number of iterations : {0}'.format(board.iterations))
print('Time elapsed : {0}'.format(str(end-start)))
