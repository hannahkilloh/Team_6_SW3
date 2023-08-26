import unittest
from models.pieces.king import King


class KingTests(unittest.TestCase):
    def test_valid_black_moves(self):
        king = King('black', (3, 7))
        valid_moves = king.calculate_valid_moves(None, [], [])
        self.assertCountEqual([(2, 7), (2, 6), (3, 6), (4, 6), (4, 7)], valid_moves)

    def test_valid_white_moves(self):
        king = King('white', (3, 0))
        valid_moves = king.calculate_valid_moves(None, [], [])
        self.assertCountEqual([(2, 0), (2, 1), (3, 1), (4, 1), (4, 0)], valid_moves)

    def test_moved(self):
        king = King('black', (3, 5))
        king.calculate_valid_moves(None, [], [])
        new_position = king.move_to_selected_position((3, 4))
        self.assertEqual((3, 4), new_position)

    def test_invalid_move(self):
        king = King('black', (1, 0))
        king.calculate_valid_moves(None, [], [])
        new_position = king.move_to_selected_position((0, 3))
        self.assertNotEqual((0, 3), new_position)

    def test_blocking_black_pieces(self):
        king = King('black', (3, 7))
        valid_moves = king.calculate_valid_moves(None, [], [(2, 7), (2, 6), (3, 6), (4, 6), (4, 7)])
        self.assertEqual([], valid_moves)

    def test_blocking_white_pieces(self):
        king = King('white', (3, 0))
        valid_moves = king.calculate_valid_moves(None, [(2, 0), (2, 1), (3, 1), (4, 1), (4, 0)], [])
        self.assertEqual([], valid_moves)

    def test_finds_one_available_not_blocked(self):
        king = King('white', (3, 0))
        valid_moves = king.calculate_valid_moves(None, [(2, 1), (3, 1), (4, 1), (4, 0)], [])
        self.assertEqual([(2, 0)], valid_moves)

    def test_valid_move_edge_of_board(self):
        king = King('black', (0, 5))
        valid_moves = king.calculate_valid_moves(None, [], [])
        self.assertCountEqual([(0, 4), (1, 4), (1, 5), (1, 6), (0, 6)], valid_moves)

    # king corner of board
    def test_corner_of_board(self):
        king = King('black', (0, 7))
        valid_moves = king.calculate_valid_moves(None, [], [])
        self.assertCountEqual([(0, 6), (1, 6), (1, 7)], valid_moves)

    def test_king_can_capture(self):
        king = King('black', (3, 7))
        king.calculate_valid_moves(None, [(4, 6)], [])
        new_position = king.move_to_selected_position((4, 6))
        self.assertEqual((4, 6), new_position)

    def test_king_can_capture_black_piece(self):
        king = King('black', (3, 0))
        king.calculate_valid_moves(None, [(4, 1)], [])
        new_position = king.move_to_selected_position((4, 1))
        self.assertEqual((4, 1), new_position)


if __name__ == '__main__':
    unittest.main()
