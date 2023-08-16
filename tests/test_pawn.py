import unittest
from Team_6_SW3.pieces.pawn import Pawn

# todo: ONCE THE BOARD AND COLOURS ARE FLIPPED, ALL 'black' AND 'white' WILL SWAP
class PawnTests(unittest.TestCase):
    # TESTS PAWN CAN MOVE ONE OR TWO STEPS AS FIRST MOVE
    def test_first_valid_moves(self):
        pawn = Pawn('white', (0, 1), None)
        valid_moves = pawn.calculate_valid_moves([], [])
        self.assertEqual([(0, 2), (0, 3)], valid_moves)

    # TEST PAWN ONLY MOVES ONCE AFTER FIRST MOVE
    def test_moves_after_first(self):
        pawn = Pawn('white', (0, 2), None)
        valid_moves = pawn.calculate_valid_moves([], [])
        self.assertEqual([(0, 3)], valid_moves)

    # # IF IT HAS BLACK IN FRONT IT SHOULD HAVE [] EMPTY ARRAY AS THERE ARE NO AVAILABLE MOVES
    def test_blocking_black_piece(self):
        pawn = Pawn('white', (0, 3), None)
        valid_moves = pawn.calculate_valid_moves([], [(0, 4)])
        self.assertEqual([], valid_moves)

    # SAME FOR A BLOCKING WHITE PIECE
    def test_blocking_white_piece(self):
        pawn = Pawn('black', (0, 4), None)
        valid_moves = pawn.calculate_valid_moves([], [(0, 3)])
        self.assertEqual([], valid_moves)

    # EDGE CASE
    # THAT PAWN CAPTURES TO THE RIGHT
    def test_valid_moves_when_capture_available(self):
        pawn = Pawn('black', (0, 3), None)  # PASSING A BLACK PIECE ON TILE 0,3, DOESN'T NEED IMAGE INPUT
        valid_moves = pawn.calculate_valid_moves([(1, 2)], [])  # PASSING WHITE CO-ORDS THAT WOULD ALLOW CAPTURING
        self.assertEqual([(0, 2), (1, 2)], valid_moves)  # THE TWO POSSIBLE CO-ORDS FOR THE BLACK PIECE TO MOVE TO

    # TESTS THAT IT ACTUALLY MOVES, THAT THE new_position AND THE SPECIFIED MATCH
    def test_move(self):
        pawn = Pawn('white', (0, 1), None)
        pawn.calculate_valid_moves([], [])
        new_position = pawn.move_to_selected_position((0, 2))
        self.assertEqual((0, 2), new_position)


if __name__ == '__main__':
    unittest.main()
