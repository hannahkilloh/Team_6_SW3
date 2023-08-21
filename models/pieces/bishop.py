from Team_6_SW3.models.pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position, 'bishop', (45, 45), (80, 80))

    def calculate_valid_moves(self, white_locations, black_locations):
        moves_list = []
        if self._colour == 'white':
            enemies_list = black_locations
            friends_list = white_locations
        else:
            friends_list = black_locations
            enemies_list = white_locations

        # Define directions for bishop movement: up-right, up-left, down-right, down-left
        directions = [(1, -1), (-1, -1), (1, 1), (-1, 1)]

        for x, y in directions:
            # Initialize the chain to 1, representing the number of steps in the current direction.
            chain = 1
            path = True
            # Continue looping until explicitly broken.
            while path:
                # Calculate the new position by adding chain * x and chain * y to the current position.
                new_x = self._current_position[0] + (chain * x)
                new_y = self._current_position[1] + (chain * y)

                # Check if the new position is within the board boundaries.
                within_boundaries = 0 <= new_x <= 7 and 0 <= new_y <= 7

                if within_boundaries:
                    # Create a new position tuple.
                    new_position = (new_x, new_y)

                    # Check if the new position is not occupied by the player's own piece.
                    not_occupied_by_own_piece = new_position not in friends_list

                    if not_occupied_by_own_piece:
                        moves_list.append(new_position)
                        # Check if the new position is occupied by an opponent's piece, and stop the path if so.
                        if new_position in enemies_list:
                            path = False

                        chain += 1
                    else:
                        # If the new position is occupied by the player's own piece, stop the path.
                        path = False
                else:
                    # If the new position is outside the board boundaries, stop the path.
                    path = False

        # Set the valid moves for this rook object and return the list of valid moves.
        self._valid_moves = moves_list
        return moves_list
