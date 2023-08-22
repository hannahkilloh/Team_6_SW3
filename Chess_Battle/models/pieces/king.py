from Team_6_SW3.Chess_Battle.models.pieces.piece import Piece


class King(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position, 'king', (45, 45), (80, 80))

    def get_short_notation(self):
        if self._colour == 'white':
            return "K"
        else:
            return "k"

    def calculate_valid_moves(self, white_locations, black_locations):
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

        self._valid_moves = moves_list
        return moves_list
