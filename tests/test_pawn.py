import unittest
from Team_6_SW3.pieces.pawn import Pawn
# from pieces.pawn import Pawn


class PawnTests(unittest.TestCase):
    def test_first_valid_moves(self):
        pawn = Pawn('white', (0, 1))
        valid_moves = pawn.get_valid_moves([], [])
        self.assertEqual([(0, 2), (0, 3)], valid_moves)

    def test_move(self):
        pawn = Pawn('white', (0, 1))
        pawn.get_valid_moves([], [])
        new_position = pawn.move_to_selected_position((0, 2))
        self.assertEqual((0, 2), new_position)


if __name__ == '__main__':
    unittest.main()
