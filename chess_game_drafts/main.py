import pygame
import chess
import chess.engine

from chess_game_drafts.data.classes.board import Board

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

pygame.display.set_caption("Chess Pals")


def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update()


def evaluate_board(board):
    # Simple evaluation function that counts the material difference between white and black
    score = 0
    for square in board.squares:
        if square.occupying_piece:
            if square.occupying_piece.color == 'white':
                score += square.occupying_piece.value
            else:
                score -= square.occupying_piece.value
    return score


def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float("-inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def computer_move(board):
    best_move = None
    max_eval = float("-inf")
    for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, depth=3, alpha=float("-inf"), beta=float("inf"), maximizing_player=False)
        board.pop()
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move


if __name__ == '__main__':
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # Quit the game if the user presses the close button
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the mouse is clicked
                if event.button == 1:
                    board.handle_click(mx, my)

        if board.is_in_checkmate('black'):  # If black is in checkmate
            print('White wins!')
            running = False
        elif board.is_in_checkmate('white'):  # If white is in checkmate
            print('Black wins!')
            running = False
        # else:
        #     if board.turn == 'white':
        #         # Player's turn
        #         # Your existing player input handling
        #     else:
        #         # Computer's turn
        #         move = computer_move(board)
        #         board.push(move)

        # Draw the board
        draw(screen)

def stockfish_move(board):
    with chess.engine.SimpleEngine.popen_uci("path/to/stockfish") as engine:
        result = engine.play(board, chess.engine.Limit(time=2.0))
        return result.move