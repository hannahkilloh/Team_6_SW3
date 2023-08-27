from models.pieces.piece import Piece


class King(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position, 'king', (45, 45), (80, 80))
        self.__is_in_check = False

    # calculates whether king is in check and returns true if so and sets is_in_check property
    def calculate_king_in_check(self, enemy_pieces, white_locations, black_locations, pos_override=None):
        possible_enemy_moves = []
        for piece in enemy_pieces:
            current_piece_possible_moves = \
                piece.calculate_valid_moves(None, white_locations, black_locations, update_protected_property=False)
            possible_enemy_moves.extend(current_piece_possible_moves)

        if pos_override is not None:
            return pos_override in possible_enemy_moves
        else:
            if self._current_position in possible_enemy_moves:
                self.__is_in_check = True
            else:
                self.__is_in_check = False

            return self.__is_in_check

    def get_is_in_check(self):
        return self.__is_in_check

    def get_short_notation(self):
        if self._colour == 'white':
            return "K"
        else:
            return "k"

    def calculate_castling_moves(self, move_history, white_locations, black_locations):
        castling_moves = []
        if move_history is not None:
            if self._colour == "black":
                second_pos = 7
            else:
                second_pos = 0

            # king is in initial position, and has not moved once.
            is_king_initial_pos = not move_history.is_move_in_history((3, second_pos))
            is_a_rook_initial_pos = not move_history.is_move_in_history((0, second_pos))
            is_b_rook_initial_pos = not move_history.is_move_in_history((7, second_pos))
            is_a_adjacent_pos_free = ((1, second_pos) not in white_locations and (1, second_pos) not in black_locations) and (
                    (2, second_pos) not in white_locations and (2, second_pos) not in black_locations)
            is_b_adjacent_pos_free = ((6, second_pos) not in white_locations and (6, second_pos) not in black_locations) and (
                    (5, second_pos) not in white_locations and (5, second_pos) not in black_locations) and (
                                             (4, second_pos) not in white_locations and (4, second_pos) not in black_locations)
            if is_king_initial_pos and is_a_rook_initial_pos and is_a_adjacent_pos_free:
                # can castle with left rook
                castling_moves.append((0, second_pos))
            if is_king_initial_pos and is_b_rook_initial_pos and is_b_adjacent_pos_free:
                # can castle with right rook
                castling_moves.append((7, second_pos))

        return castling_moves

    def calculate_valid_moves(self, move_history, white_locations, black_locations,
                              update_protected_property=True, is_adjacent_=None):
        moves_list = []
        if self._colour == 'white':
            friends_list = white_locations
        else:
            friends_list = black_locations
        # 8 squares to check for kings moves, they can go one square in any direction
        targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
        for i in range(len(targets)):
            # get the current positions first coord + loop each targets first coord
            # , then the current positions second coord plus each targets second coord
            # loop each target for the length of targets to find if the tile is taken and by black or white
            target = (self._current_position[0] + targets[i][0], self._current_position[1] + targets[i][1])
            if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                moves_list.append(target)

        # calling the castling function
        castling_moves = self.calculate_castling_moves(move_history, white_locations, black_locations)
        moves_list.extend(castling_moves)

        if update_protected_property:
            self._valid_moves = moves_list

        return moves_list
