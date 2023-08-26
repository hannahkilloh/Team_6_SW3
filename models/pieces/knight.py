from models.pieces.piece import Piece


class Knight(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position, 'knight', (45, 45), (80, 80))

    def get_short_notation(self):
        if self._colour == 'white':
            return "N"
        else:
            return "n"

    def calculate_valid_moves(self, move_history, white_locations, black_locations, update_protected_property=True):
        moves_list = []
        if self._colour == 'white':
            friends_list = white_locations
        else:
            friends_list = black_locations
        # 8 squares to check for knights moves, they can go two squares in one direction and one in another direction
        targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for i in range(8):
            target = (self._current_position[0] + targets[i][0], self._current_position[1] + targets[i][1])
            if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                moves_list.append(target)

        if update_protected_property:
            self._valid_moves = moves_list

        return moves_list
