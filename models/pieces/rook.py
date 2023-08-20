from Team_6_SW3.models.pieces.piece import Piece


class Rook(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position, 'rook', (45, 45), (80, 80))

    def calculate_valid_moves(self, white_locations, black_locations):
        moves_list = []

        if self._colour == 'white':
            enemies_list = black_locations
            friends_list = white_locations
        else:
            friends_list = black_locations
            enemies_list = white_locations

        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            chain = 1
            while True:
                new_x = self._current_position[0] + chain * x
                new_y = self._current_position[1] + chain * y

                new_position = (new_x, new_y)

                if new_position in friends_list:
                    break

                if not (0 <= new_x <= 7 and 0 <= new_y <= 7):
                    break

                moves_list.append(new_position)

                if new_position in enemies_list:
                    break

                chain += 1

        self._valid_moves = moves_list
        return moves_list
