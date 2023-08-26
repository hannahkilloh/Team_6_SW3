from models.pieces.piece import Piece
from models.helpers import get_friends_and_enemies


class Rook(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position, 'rook', (45, 45), (80, 80))

    def get_short_notation(self):
        if self._colour == 'white':
            return "R"
        else:
            return "r"

    def calculate_valid_moves(self, move_history, white_locations, black_locations, update_protected_property=True):
        moves_list = []

        # Use the get_friends_and_enemies function to set friends_list and enemies_list
        friends_list, enemies_list = get_friends_and_enemies(self._colour, white_locations, black_locations)

        # Iterate through the four possible directions for a rook: up, down, left, and right.
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Initialize the chain to 1, representing the number of steps in the current direction.
            chain = 1

            # Continue looping until explicitly broken.
            while True:
                # Calculate the new position by adding chain * x and chain * y to the current position.
                new_x = self._current_position[0] + chain * x
                new_y = self._current_position[1] + chain * y

                new_position = (new_x, new_y)  # Create a new position tuple.

                # If the new position is occupied by the player's own piece, break the loop.
                if new_position in friends_list:
                    break

                # If the new position is outside the board boundaries, break the loop.
                if not (0 <= new_x <= 7 and 0 <= new_y <= 7):
                    break

                # Append the new position as a valid move.
                moves_list.append(new_position)

                # If the new position is occupied by the opponent's piece, break the loop.
                if new_position in enemies_list:
                    break

                # Increment the chain to explore further in the current direction.
                chain += 1

        if update_protected_property:
            self._valid_moves = moves_list

        # Set the valid moves for this rook object and return the list of valid moves.
        return moves_list
