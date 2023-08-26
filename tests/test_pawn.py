import unittest
from models.pieces.pawn import Pawn


class PawnTests(unittest.TestCase):
    def test_first_valid_moves(self):
        pawn = Pawn('white', (0, 1))
        valid_moves = pawn.calculate_valid_moves(None, [], [])
        self.assertCountEqual([(0, 2), (0, 3)], valid_moves)

    def test_moved(self):
        pawn = Pawn('white', (0, 1))
        pawn.calculate_valid_moves(None, [], [])
        new_position = pawn.move_to_selected_position((0, 2))
        self.assertEqual((0, 2), new_position)

    def test_moves_after_first(self):
        pawn = Pawn('white', (0, 2))
        valid_moves = pawn.calculate_valid_moves(None, [], [])
        self.assertEqual([(0, 3)], valid_moves)

    def test_blocking_black_piece(self):
        pawn = Pawn('white', (0, 3))
        valid_moves = pawn.calculate_valid_moves(None, [], [(0, 4)])
        self.assertEqual([], valid_moves)

    def test_blocking_white_piece(self):
        pawn = Pawn('black', (0, 4))
        valid_moves = pawn.calculate_valid_moves(None, [(0, 3)], [])
        self.assertEqual([], valid_moves)

    def test_blocking_same_colour(self):
        pawn = Pawn('black', (0, 4))
        valid_moves = pawn.calculate_valid_moves(None, [], [(0, 3)])
        self.assertEqual([], valid_moves)

    def test_valid_move_when_capture_available(self):
        pawn = Pawn('black', (0, 3))
        valid_moves = pawn.calculate_valid_moves(None, [(1, 2)], [])
        self.assertCountEqual([(0, 2), (1, 2)], valid_moves)

    def test_move_diagonal_if_captured(self):
        pawn = Pawn('black', (0, 3))
        pawn.calculate_valid_moves(None, [(1, 2)], [])
        new_position = pawn.move_to_selected_position((1, 2))
        self.assertEqual((1, 2), new_position)

    def test_captures_available_enemy(self):
        pawn = Pawn('black', (0, 3))
        valid_moves = pawn.calculate_valid_moves(None, [(1, 2)], [])
        self.assertCountEqual([(1, 2), (0, 2)], valid_moves)


if __name__ == '__main__':
    unittest.main()
