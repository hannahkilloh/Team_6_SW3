import unittest
from models.pieces.rook import Rook


class TestRook(unittest.TestCase):
    def setUp(self):
        # Initialize a Rook instance for testing.
        self.rook = Rook('white', (0, 0))

    def test_exists(self):
        # Check if the Rook class exists.
        self.assertIsNotNone(self.rook)

    def test_color(self):
        # Check if the rook's color is set correctly.
        self.assertEqual(self.rook._colour, 'white')

    def test_get_valid_moves_unblocked(self):
        # Test valid moves when the rook is not blocked by any pieces.
        own_locations = []
        opponent_locations = []
        valid_moves = self.rook.calculate_valid_moves(None, own_locations, opponent_locations)
        expected_moves = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                          (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        self.assertEqual(valid_moves, expected_moves)

    def test_get_valid_moves_blocked(self):
        # Test valid moves when the rook is blocked by own pieces.
        # Example: Rook is blocked by own pieces at (0, 1) and (0, 2).
        own_locations = [(0, 1), (0, 2)]
        opponent_locations = []
        valid_moves = self.rook.calculate_valid_moves(None, own_locations, opponent_locations)

        # Assert that the blocked positions are not in the valid_moves list.
        blocked_positions = [(0, 1), (0, 2)]
        for pos in blocked_positions:
            self.assertNotIn(pos, valid_moves)

    def test_get_valid_moves_edge_cases(self):
        # Test edge cases of moves, e.g., rook moving 1 or 3 steps.
        own_locations = []
        opponent_locations = []
        # Test scenarios where the rook can move 1, 2, or 3 steps in each direction.
        valid_moves = self.rook.calculate_valid_moves(None, own_locations, opponent_locations)
        expected_moves = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                          (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        self.assertEqual(valid_moves, expected_moves)

    def test_get_valid_moves_capture(self):
        # Test that the rook can capture an opponent's piece.
        own_locations = []
        opponent_locations = [(0, 1)]  # Example: Opponent's piece at (0, 1).
        valid_moves = self.rook.calculate_valid_moves(None, own_locations, opponent_locations)
        # Assert that the valid_moves list contains the position (0, 1).
        self.assertIn((0, 1), valid_moves)


if __name__ == '__main__':
    unittest.main()
