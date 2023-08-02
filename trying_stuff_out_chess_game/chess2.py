import chess
import chess.engine
import chess.svg
from IPython.display import SVG, display


def play_chess(difficulty):
    """
    This function allows the user to play a text-based game of chess with a visual board against a CPU that has different difficulty settings using sunfish.

    Parameters:
    difficulty (int): The difficulty level of the CPU. 1 is the easiest, 10 is the hardest.

    Returns:
    None
    """
    try:
        # Initialize the chess board and engine
        board = chess.Board()
        engine = chess.engine.SimpleEngine.popen_uci("path/to/sunfish")

        # Set the CPU difficulty level
        options = {"Skill Level": difficulty}
        engine.configure(options)

        # Play the game
        while not board.is_game_over():
            # Display the board
            display(SVG(chess.svg.board(board=board)))

            # Get the user's move
            user_move = input("Enter your move (e.g. e2e4): ")
            try:
                board.push_san(user_move)
            except ValueError:
                print("Invalid move. Try again.")
                continue

            # Get the CPU's move
            cpu_move = engine.play(board, chess.engine.Limit(time=2.0))
            board.push(cpu_move.move)

        # Display the final board and result
        display(SVG(chess.svg.board(board=board)))
        print(f"Game over. Result: {board.result()}")
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return
    finally:
        # Close the engine
        engine.quit()