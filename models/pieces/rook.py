from piece import Piece


class Rook(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position)

    # move_to_selected_position does not need to be written again

    def get_valid_moves(self, white_locations, black_locations):
        pass
