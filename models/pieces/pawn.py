from models.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position, 'pawn', (45, 45), (65, 65))

    def get_short_notation(self):
        if self._colour == 'white':
            return ""
        else:
            return ""

    def calculate_valid_moves(self, move_history, white_locations, black_locations, update_protected_property=True):
        moves_list = []  # moves list calculates the possible moves of each piece
        if self._colour == 'white':
            no_blocking_white_piece = (self._current_position[0], self._current_position[1] + 1) not in white_locations
            no_blocking_black_piece = (self._current_position[0], self._current_position[1] + 1) not in black_locations
            is_not_bottom_of_board = self._current_position[1] < 7

            # calculates one step forward move
            if no_blocking_white_piece and no_blocking_black_piece and is_not_bottom_of_board:
                moves_list.append((self._current_position[0], self._current_position[1] + 1))

            is_first_move = self._current_position[1] == 1
            no_blocking_white_piece_for_two = (self._current_position[0], self._current_position[1] + 2) \
                                              not in white_locations and no_blocking_white_piece
            no_blocking_black_piece_for_two = (self._current_position[0], self._current_position[1] + 2) \
                                              not in black_locations and no_blocking_black_piece

            # calculates two steps forward first move
            if no_blocking_white_piece_for_two and no_blocking_black_piece_for_two and is_first_move:
                moves_list.append((self._current_position[0], self._current_position[1] + 2))

            # checks diagonal right for black piece
            diagonal_right_is_black = (self._current_position[0] + 1, self._current_position[1] + 1) in black_locations
            if diagonal_right_is_black:
                moves_list.append((self._current_position[0] + 1, self._current_position[1] + 1))

            # checks diagonal left for black piece
            diagonal_left_is_black = (self._current_position[0] - 1, self._current_position[1] + 1) in black_locations
            if diagonal_left_is_black:
                moves_list.append((self._current_position[0] - 1, self._current_position[1] + 1))

        else:
            no_blocking_white_piece = (self._current_position[0], self._current_position[1] - 1) not in white_locations
            no_blocking_black_piece = (self._current_position[0], self._current_position[1] - 1) not in black_locations
            is_not_top_of_board = self._current_position[1] > 0

            # calculates one step forward
            if no_blocking_white_piece and no_blocking_black_piece and is_not_top_of_board:
                moves_list.append((self._current_position[0], self._current_position[1] - 1))

            is_first_move = self._current_position[1] == 6
            no_blocking_white_piece_for_two = (self._current_position[0], self._current_position[1] - 2) \
                                              not in white_locations and no_blocking_white_piece
            no_blocking_black_piece_for_two = (self._current_position[0], self._current_position[1] - 2) \
                                              not in black_locations and no_blocking_black_piece

            # calculates two steps forward first move
            if no_blocking_white_piece_for_two and no_blocking_black_piece_for_two and is_first_move:
                moves_list.append((self._current_position[0], self._current_position[1] - 2))

            # checks diagonal right for white piece
            diagonal_right_is_white = (self._current_position[0] + 1, self._current_position[1] - 1) in white_locations
            if diagonal_right_is_white:
                moves_list.append((self._current_position[0] + 1, self._current_position[1] - 1))

            # checks diagonal left for white piece
            diagonal_left_is_white = (self._current_position[0] - 1, self._current_position[1] - 1) in white_locations
            if diagonal_left_is_white:
                moves_list.append((self._current_position[0] - 1, self._current_position[1] - 1))

        if update_protected_property:
            self._valid_moves = moves_list

        return moves_list
