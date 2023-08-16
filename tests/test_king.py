import unittest
from Team_6_SW3.pieces.king import King


class KingTests(unittest.TestCase):
    def test_first_valid_moves(self):
        king = King('white', (0, 1), None)
        valid_moves = king.calculate_valid_moves([], [])
        self.assertEqual([(0, 2), (0, 3)], valid_moves)

    def test_move(self):
        pawn = King('white', (0, 1), None)
        pawn.calculate_valid_moves([], [])
        new_position = pawn.move_to_selected_position((0, 2))
        self.assertEqual((0, 2), new_position)


if __name__ == '__main__':
    unittest.main()
