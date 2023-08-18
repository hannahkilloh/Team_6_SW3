from models.pieces.piece import Piece


class Rook(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position)

    def get_valid_moves(self, own_locations, opponent_locations):
        moves_list = []
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            chain = 1
            while True:
                new_x = self._Piece__current_position[0] + chain * x
                new_y = self._Piece__current_position[1] + chain * y

                new_position = (new_x, new_y)

                if new_position in own_locations:
                    break

                if not (0 <= new_x <= 7 and 0 <= new_y <= 7):
                    break

                moves_list.append(new_position)

                if new_position in opponent_locations:
                    break

                chain += 1

        self._Piece__valid_moves = moves_list
        return moves_list
