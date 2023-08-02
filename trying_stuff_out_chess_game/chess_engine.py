# Import necessary libraries
import chess
import chess.engine


def chess_engine():
    """
    This function creates a chess engine using the python-chess library and the Stockfish engine.
    It then allows the user to play a game of chess against the engine.
    """
    try:
        # Create a chess board object
        board = chess.Board()

        # Load the Stockfish engine
        engine = chess.engine.SimpleEngine.popen_uci("stockfish")

        # Play a game of chess against the engine
        while not board.is_game_over():
            # Get the user's move
            user_move = input("Enter your move (in algebraic notation): ")

            # Make sure the move is legal
            if chess.Move.from_uci(user_move) not in board.legal_moves:
                print("Illegal move, try again.")
                continue

            # Make the user's move and print the board
            board.push(chess.Move.from_uci(user_move))
            print(board)

            # Get the engine's move
            engine_move = engine.play(board, chess.engine.Limit(time=2.0))
            board.push(engine_move.move)
            print(f"Engine move: {engine_move.move}")

        # Close the engine
        engine.quit()
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
