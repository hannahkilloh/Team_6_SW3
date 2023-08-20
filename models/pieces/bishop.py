from piece import Piece


class Bishop(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position)

    def get_valid_moves(self, own_locations, opponent_locations):
        moves_list = []

        for i in range(4):  # up-right, up-left, down-right, down-left
            path = True
            chain = 1
            if i == 0:
                x = 1
                y = -1
            elif i == 1:
                x = -1
                y = -1
            elif i == 2:
                x = 1
                y = 1
            else:
                x = -1
                y = 1
            while path:
                if (self._Piece__current_position[0] + (chain * x), self._Piece__current_position[1] + (chain * y)) not in own_locations and \
                        0 <= self._Piece__current_position[0] + (chain * x) <= 7 and 0 <= self._Piece__current_position[1] + (chain * y) <= 7:
                    moves_list.append(
                        (self._Piece__current_position[0] + (chain * x), self._Piece__current_position[1] + (chain * y)))
                    if (self._Piece__current_position[0] + (chain * x), self._Piece__current_position[1] + (chain * y)) in opponent_locations:
                        path = False
                    chain += 1
                else:
                    path = False
        return moves_list
