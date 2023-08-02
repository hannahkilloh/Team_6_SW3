import chess
import chess.svg
import random


def play_chess():
    """
    This function starts a game of chess with a graphical interface and AI opponent.
    """
    try:
        # Initialize the board and display it
        board = chess.Board()
        print(board)

        # Loop until the game is over
        while not board.is_game_over():
            # Get the move from the player
            move = input("Enter your move (e.g. e2e4): ")

            # Check if the move is valid
            if move not in [str(m) for m in board.legal_moves]:
                print("Invalid move. Try again.")
                continue

            # Make the move and display the updated board
            board.push_san(move)
            print(board)

            # Check if the game is over
            if board.is_game_over():
                break

            # Get the AI's move
            ai_move = random.choice(list(board.legal_moves))

            # Make the AI's move and display the updated board
            board.push(ai_move)
            print(board)

        # Print the result of the game
        print("Game over. Result: ", board.result())
    except Exception as e:
        # Log the error
        print(f"Error: {e}")