from Team_6_SW3.models.pieces.piece import Piece


class Queen(Piece):
    def __init__(self, colour, current_position):
        super().__init__(colour, current_position, 'queen', (45, 45), (80, 80))