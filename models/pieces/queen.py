from models.pieces.rook import Rook
from models.pieces.piece import Piece
from models.pieces.bishop import Bishop


class Queen(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position, 'queen', (45, 45), (80, 80))

    def get_short_notation(self):
        if self._colour == 'white':
            return "Q"
        else:
            return "q"

    def calculate_valid_moves(self, move_history, white_locations, black_locations, update_protected_property=True):
        moves_list = []

        # create a new instance of rook and pass queens colour and position
        rook = Rook(self._colour, self.get_current_position())
        # get rooks valid moves and add to the list
        rook_valid_moves = rook.calculate_valid_moves(move_history, white_locations, black_locations)
        moves_list.extend(rook_valid_moves)

        # same for bishop
        bishop = Bishop(self._colour, self.get_current_position())
        bishop_valid_moves = bishop.calculate_valid_moves(move_history, white_locations, black_locations)
        moves_list.extend(bishop_valid_moves)

        # if king is in check
        if update_protected_property:
            self._valid_moves = moves_list

        return moves_list
