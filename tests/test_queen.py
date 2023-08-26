import unittest
from models.pieces.queen import Queen


class QueenTests(unittest.TestCase):
    def test_valid_white_moves(self):
        queen = Queen('white', (3, 7))
        valid_moves = queen.calculate_valid_moves(None, [], [])
        expected_moves = [(0, 7), (1, 7), (2, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                          (2, 6), (1, 5), (0, 4),
                          (3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (3, 0),
                          (4, 6), (5, 5), (6, 4), (7, 3)]
        self.assertCountEqual(expected_moves, valid_moves)

    def test_valid_black_moves(self):
        queen = Queen('black', (3, 0))
        valid_moves = queen.calculate_valid_moves(None, [], [])
        expected_moves = [(0, 0), (1, 0), (2, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                          (2, 1), (1, 2), (0, 3),
                          (3, 7), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1),
                          (4, 1), (5, 2), (6, 3), (7, 4)]
        self.assertCountEqual(expected_moves, valid_moves)

    def test_invalid_black_move(self):
        queen = Queen('black', (3, 0))
        valid_moves = queen.calculate_valid_moves(None, [], [])
        expected_moves = [(7, 5)]
        self.assertNotEqual(expected_moves, valid_moves)

    def test_invalid_white_move(self):
        queen = Queen('white', (3, 7))
        valid_moves = queen.calculate_valid_moves(None, [], [])
        expected_moves = [(0, 2)]
        self.assertNotEqual(expected_moves, valid_moves)

    def test_moved(self):
        queen = Queen('black', (3, 0))
        queen.calculate_valid_moves(None, [], [])
        new_position = queen.move_to_selected_position((3, 1))
        self.assertEqual((3, 1), new_position)

    def test_blocking_same_piece(self):
        queen = Queen('black', (3, 0))
        expected_moves = [(0, 0), (1, 0), (2, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                          (2, 1), (1, 2), (0, 3),
                          (4, 1), (5, 2), (6, 3), (7, 4)]
        valid_moves = queen.calculate_valid_moves(None, [], [(3, 1)])
        self.assertCountEqual(expected_moves, valid_moves)

    def test_valid_black_moves_with_all_blocking_whites(self):
        queen = Queen('black', (3, 0))
        expected_moves = [(2, 0), (2, 1), (3, 1), (4, 1), (4, 0)]
        valid_moves = queen.calculate_valid_moves(None, [(2, 0), (2, 1), (3, 1), (4, 1), (4, 0)], [])
        self.assertCountEqual(expected_moves, valid_moves)

    def test_valid_black_moves_with_some_blocking_whites(self):
        queen = Queen('black', (3, 0))
        expected_moves = [(2, 0), (2, 1), (3, 1),
                          (4, 1), (5, 2), (6, 3), (7, 4),
                          (4, 0), (5, 0), (6, 0), (7, 0)]
        valid_moves = queen.calculate_valid_moves(None, [(2, 0), (2, 1), (3, 1)], [])
        self.assertCountEqual(expected_moves, valid_moves)

    def test_valid_white_moves_with_all_blocking_blacks(self):
        queen = Queen('white', (3, 7))
        expected_moves = [(2, 7), (2, 6), (3, 6), (4, 6), (4, 7)]
        valid_moves = queen.calculate_valid_moves(None, [], [(2, 7), (2, 6), (3, 6), (4, 6), (4, 7)])
        self.assertCountEqual(expected_moves, valid_moves)

    def test_valid_white_moves_with_some_blocking_blacks(self):
        queen = Queen('white', (3, 7))
        expected_moves = [(2, 7), (2, 6), (3, 6),
                          (4, 6), (5, 5), (6, 4), (7, 3),
                          (4, 7), (5, 7), (6, 7), (7, 7)]
        valid_moves = queen.calculate_valid_moves(None, [], [(2, 7), (2, 6), (3, 6)])
        self.assertCountEqual(expected_moves, valid_moves)

    def test_captures_black_piece(self):
        queen = Queen('white', (3, 7))
        queen.calculate_valid_moves(None, [], [(3, 6)])
        new_position = queen.move_to_selected_position((3, 6))
        self.assertEqual((3, 6), new_position)

    def test_captures_white_piece(self):
        queen = Queen('black', (3, 0))
        queen.calculate_valid_moves(None, [(3, 1)], [])
        new_position = queen.move_to_selected_position((3, 1))
        self.assertEqual((3, 1), new_position)
