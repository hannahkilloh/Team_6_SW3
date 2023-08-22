import unittest
from Team_6_SW3.Chess_Battle.models.pieces.queen import Queen


class QueenTests(unittest.TestCase):
    def test_valid_black_moves(self):
        queen = Queen('black', (3, 7))
        valid_moves = queen.calculate_valid_moves([], [])
        self.assertCountEqual([(2, 7), (2, 6), (3, 6), (4, 6), (4, 7)], valid_moves)
