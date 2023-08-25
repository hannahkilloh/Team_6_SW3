import unittest
from models.pieces.pawn import Pawn


# todo: ONCE THE BOARD AND COLOURS ARE FLIPPED, ALL 'black' AND 'white' WILL SWAP

class PawnTests(unittest.TestCase):
    # TESTS PAWN CAN MOVE ONE OR TWO STEPS AS FIRST MOVE
    def test_first_valid_moves(self):
        pawn = Pawn('white', (0, 1))
        valid_moves = pawn.calculate_valid_moves(None, [], [])
        self.assertCountEqual([(0, 2), (0, 3)], valid_moves)

    # TESTS THAT PAWN ACTUALLY MOVES, THAT THE new_position AND THE SPECIFIED MATCH
    def test_moved(self):
        pawn = Pawn('white', (0, 1))
        pawn.calculate_valid_moves(None, [], [])
        new_position = pawn.move_to_selected_position((0, 2))
        self.assertEqual((0, 2), new_position)

    # TEST PAWN ONLY MOVES ONCE AFTER FIRST MOVE
    def test_moves_after_first(self):
        pawn = Pawn('white', (0, 2))
        valid_moves = pawn.calculate_valid_moves(None, [], [])
        self.assertEqual([(0, 3)], valid_moves)

    # # IF IT HAS A BLACK IN FRONT IT SHOULD HAVE [] EMPTY ARRAY AS THERE ARE NO AVAILABLE MOVES
    def test_blocking_black_piece(self):
        pawn = Pawn('white', (0, 3))
        valid_moves = pawn.calculate_valid_moves(None, [], [(0, 4)])
        self.assertEqual([], valid_moves)

    # SAME FOR A BLOCKING WHITE PIECE
    def test_blocking_white_piece(self):
        pawn = Pawn('black', (0, 4))
        valid_moves = pawn.calculate_valid_moves(None, [(0, 3)], [])
        self.assertEqual([], valid_moves)

    def test_blocking_same_colour(self):
        pawn = Pawn('black', (0, 4))
        valid_moves = pawn.calculate_valid_moves(None, [], [(0, 3)])
        self.assertEqual([], valid_moves)

    # THAT PAWN CAN MOVE TO THE RIGHT WHEN CAPTURE IS AVAILABLE
    def test_valid_move_when_capture_available(self):
        pawn = Pawn('black', (0, 3))  # PASSING A BLACK PIECE ON TILE 0,3, DOESN'T NEED IMAGE INPUT
        valid_moves = pawn.calculate_valid_moves(None, [(1, 2)], [])  # PASSING WHITE CO-ORDS THAT WOULD ALLOW CAPTURING
        self.assertCountEqual([(0, 2), (1, 2)], valid_moves)  # THE TWO POSSIBLE CO-ORDS FOR THE BLACK PIECE TO MOVE TO

    # THAT PAWN HAS MOVED WHEN CAPTURE WAS AVAILABLE
    def test_move_diagonal_if_captured(self):
        pawn = Pawn('black', (0, 3))  # PASSING A BLACK PIECE ON TILE 0,3, DOESN'T NEED IMAGE INPUT
        pawn.calculate_valid_moves(None, [(1, 2)], [])  # PASSING W.LOCATION TO THE CALCULATE VALID MOVES FUNC
        # PASSING NEW WHITE LOCATION POSITION TO FUNC AND SETTING IT EQUAL TO NEW POSITION VARIABLE
        new_position = pawn.move_to_selected_position((1, 2))
        # ASSERTING IF THE NEW POSITION IS EQUAL TO THE PROPOSED WHITE LOCATION CAPTURE
        self.assertEqual((1, 2), new_position)

    def test_captures_available_enemy(self):
        pawn = Pawn('black', (0, 3))  # PASSING A BLACK PIECE ON TILE 0,3, DOESN'T NEED IMAGE INPUT
        valid_moves = pawn.calculate_valid_moves(None, [(1, 2)], [])  # PASSING WHITE CO-ORDS THAT WOULD ALLOW CAPTURING
        self.assertCountEqual([(1, 2), (0, 2)], valid_moves)  # THE TWO POSSIBLE CO-ORDS FOR THE BLACK PIECE TO MOVE TO


if __name__ == '__main__':
    unittest.main()
