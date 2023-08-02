import chess
import time
import random
import pygame

# Tutorial link: https://www.youtube.com/watch?app=desktop&v=aJQB775AZck#dialog

# Making the board and moving pieces
board = chess.Board()
# board.push_san('d4')
# board.push_san('b1c3')
# board.push_san('d5')
print(board)

# Show legal moves that can currently be made
# legal_moves = board.legal_moves
# print(legal_moves)

# Show count of legal moves
# legal_moves_count = board.legal_moves.count
# print(legal_moves_count)

# list of legal moves
legal_moves_list = str(list(board.legal_moves)[0])

# Making moves on the board
board = chess.Board()
while not board.is_checkmate():
    max_move_count = board.legal_moves.count() - 1
    random_move = random.randint(0, max_move_count)
    move = legal_moves_list = str(list(board.legal_moves)[random_move])

    board.push_san(move)
    print(board)
    print('\n\n')
    time.sleep(1)
