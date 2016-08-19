import time

from source.models import Board, Piece, Position

board = Board(3,3)
board.add_piece('king')
board.add_piece('bishop')
board.add_piece('bishop')

start = time.time()

board.set_play(0)

end = time.time()
for play in board.saved_plays:
    board.show_play(play)

#print('Number of possible plays : {0}'.format(len(board.saved_plays)))
print('Number of possible plays : {0}'.format(board.count_saved_plays))
print('Number of iterations : {0}'.format(board.iterations))
print('Time elapsed : {0}'.format(str(end-start)))
