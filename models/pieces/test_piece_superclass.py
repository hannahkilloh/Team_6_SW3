import unittest
from piece import Piece


class TestPiece(unittest.TestCase):
    def setUp(self):
        # Initialize a Piece instance for testing.
        self.piece = Piece('white', (0, 0))

    def test_init(self):
        # Check if the __init__ method sets the attributes correctly.
        self.assertEqual(self.piece._Piece__colour, 'white')
        self.assertEqual(self.piece._Piece__current_position, (0, 0))
        self.assertEqual(self.piece._Piece__valid_moves, [])

    def test_move_to_selected_position_valid(self):
        # Test moving to a valid position.
        self.piece._Piece__valid_moves = [(0, 1), (1, 0)]
        new_position = self.piece.move_to_selected_position((1, 0))
        self.assertEqual(new_position, (1, 0))

    def test_move_to_selected_position_invalid(self):
        # Test moving to an invalid position.
        self.piece._Piece__valid_moves = [(0, 1), (1, 0)]
        new_position = self.piece.move_to_selected_position((2, 2))
        # Should remain at the current position.
        self.assertEqual(new_position, (0, 0))


if __name__ == '__main__':
    unittest.main()
