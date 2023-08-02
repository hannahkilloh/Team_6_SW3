import pygame
import sys
import chess
import chess.svg
import chess.engine

# Constants
WIDTH, HEIGHT = 512, 512
SQUARE_SIZE = WIDTH // 8
FPS = 30
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")
clock = pygame.time.Clock()


def draw_chessboard():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else pygame.Color("gray")
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces(board):
    svg_image = chess.svg.board(board=board)
    with open("board.svg", "w") as f:
        f.write(svg_image)


def evaluate_board(board):
    # Simple evaluation function based on piece values
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0,  # The king's value is not relevant for this simple heuristic
    }

    evaluation = 0
    for square, piece in board.piece_map().items():
        if piece.color == chess.WHITE:
            evaluation += piece_values[piece.piece_type]
        else:
            evaluation -= piece_values[piece.piece_type]

    return evaluation


def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float("-inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True)
            board.pop()
            min_eval = min(min_eval, eval)
        return min_eval


def computer_move(board):
    best_move = None
    max_eval = float("-inf")
    for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, depth=2, maximizing_player=False)
        board.pop()
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move


def main():
    board = chess.Board()

    while not board.is_game_over():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if board.turn == chess.WHITE:
            # Player's turn
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // SQUARE_SIZE
                    row = event.pos[1] // SQUARE_SIZE
                    square = 8 * (7 - row) + col
                    piece = board.piece_at(square)
                    if piece and piece.color == chess.WHITE:
                        selected_square = square
                elif event.type == pygame.MOUSEBUTTONUP:
                    col = event.pos[0] // SQUARE_SIZE
                    row = event.pos[1] // SQUARE_SIZE
                    target_square = 8 * (7 - row) + col
                    if selected_square != target_square:
                        move = chess.Move(selected_square, target_square)
                        if move in board.legal_moves:
                            board.push(move)
                    selected_square = None
        else:
            # Computer's turn
            move = computer_move(board)
            board.push(move)

        draw_chessboard()
        draw_pieces(board)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
