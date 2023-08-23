from models.pieces.piece import Piece


class King(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position, 'king', (45, 45), (80, 80))

    def get_short_notation(self):
        if self._colour == 'white':
            return "K"
        else:
            return "k"

    def calculate_valid_moves(self, move_history, white_locations, black_locations, is_adjacent_=None):
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

        # append castling moves for kingside and queenside
        if self._colour == 'black':
            # king is in initial position, and has not moved once.
            is_king_initial_pos = not move_history.is_move_in_history('black', (3, 7))
            is_a_rook_initial_pos = not move_history.is_move_in_history('black', (0, 7))
            is_b_rook_initial_pos = not move_history.is_move_in_history('black', (7, 7))
            is_a_adjacent_pos_free = ((1, 7) not in white_locations and (1, 7) not in black_locations) and ((2, 7) not in white_locations and (2, 7) not in black_locations)
            is_b_adjacent_pos_free = ((6, 7) not in white_locations and (6, 7) not in black_locations) and ((5, 7) not in white_locations and (5, 7) not in black_locations) and ((4, 7) not in white_locations and (4, 7) not in black_locations)
            if is_king_initial_pos and is_a_rook_initial_pos and is_a_adjacent_pos_free:
                # can castle with left rook
                moves_list.append((0, 7))
            if is_king_initial_pos and is_b_rook_initial_pos and is_b_adjacent_pos_free:
                # can castle with right rook
                moves_list.append((7, 7))

        elif self._colour == 'white':
            # king is in initial position, and has not moved once.
            is_king_initial_pos = not move_history.is_move_in_history('white', (3, 0))
            is_a_rook_initial_pos = not move_history.is_move_in_history('white', (0, 0))
            is_b_rook_initial_pos = not move_history.is_move_in_history('white', (7, 0))
            is_a_adjacent_pos_free = ((1, 0) not in white_locations and (1, 0) not in black_locations) and ((2, 0) not in white_locations and (2, 0) not in black_locations)
            is_b_adjacent_pos_free = ((6, 0) not in white_locations and (6, 0) not in black_locations) and ((5, 0) not in white_locations and (5, 0) not in black_locations) and ((4, 0) not in white_locations and (4, 0) not in black_locations)
            if is_king_initial_pos and is_a_rook_initial_pos and is_a_adjacent_pos_free:
                # can castle with left rook
                moves_list.append((0, 0))
            if is_king_initial_pos and is_b_rook_initial_pos and is_b_adjacent_pos_free:
                # can castle with right rook
                moves_list.append((7, 0))

        self._valid_moves = moves_list
        return moves_list
