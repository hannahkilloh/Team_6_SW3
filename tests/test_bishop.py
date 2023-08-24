import unittest
from models.pieces.bishop import Bishop


class TestBishop(unittest.TestCase):
    def setUp(self):
        # Initialize a Bishop instance for testing (you can specify color and position as needed).
        self.bishop = Bishop('white', (0, 0))

    def test_exists(self):
        # Check if the Bishop class exists.
        self.assertIsNotNone(self.bishop)

    def test_color(self):
        # Check if the bishop's color is set correctly.
        self.assertEqual(self.bishop._colour, 'white')

    def test_get_valid_moves_unblocked(self):
        # Test valid moves when the bishop is not blocked by any pieces.
        own_locations = []
        opponent_locations = []
        valid_moves = self.bishop.calculate_valid_moves(None, own_locations, opponent_locations)
        # Only consider the positive quadrant moves, as they are mirrored in the negative quadrant.
        expected_moves = [(1, 1), (2, 2), (3, 3), (4, 4),
                          (5, 5), (6, 6), (7, 7)]
        self.assertEqual(valid_moves, expected_moves)

    def test_get_valid_moves_blocked(self):
        # Test valid moves when the bishop is blocked by own pieces.
        # Example: Bishop is blocked by own pieces at (1, 1) and (2, 2).
        own_locations = [(1, 1), (2, 2)]
        opponent_locations = []
        valid_moves = self.bishop.calculate_valid_moves(None, own_locations, opponent_locations)
        # Assert that the blocked positions are not in the valid_moves list.
        blocked_positions = [(1, 1), (2, 2)]
        for pos in blocked_positions:
            self.assertNotIn(pos, valid_moves)

    def test_get_valid_moves_edge_cases(self):
        # Test edge cases of moves, e.g., bishop moving 1 or 3 steps.
        own_locations = []
        opponent_locations = []
        # Only consider the positive quadrant moves, as they are mirrored in the negative quadrant.
        valid_moves = self.bishop.calculate_valid_moves(None, own_locations, opponent_locations)
        expected_moves = [(1, 1), (2, 2), (3, 3), (4, 4),
                          (5, 5), (6, 6), (7, 7)]
        self.assertEqual(valid_moves, expected_moves)

    def test_get_valid_moves_capture(self):
        # Test that the bishop can capture an opponent's piece.
        own_locations = []
        opponent_locations = [(1, 1)]  # Example: Opponent's piece at (1, 1).
        valid_moves = self.bishop.calculate_valid_moves(None, own_locations, opponent_locations)
        # Assert that the valid_moves list contains the position (1, 1).
        self.assertIn((1, 1), valid_moves)


if __name__ == '__main__':
    unittest.main()
