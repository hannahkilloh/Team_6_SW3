import unittest
from Team_6_SW3.pieces.knight import Knight


class KnightTests(unittest.TestCase):
    # tests the knights first move
    def test_first_valid_moves(self):
        knight = Knight('white', (1, 0), None)
        valid_moves = knight.calculate_valid_moves([], [])
        self.assertEqual([(2, 2), (3, 1), (0, 2)], valid_moves)

    def test_move(self):
        knight = Knight('white', (1, 0), None)
        knight.calculate_valid_moves([], [])
        new_position = knight.move_to_selected_position((2, 2))
        self.assertEqual((2, 2), new_position)

    def test_invalid_move(self):
        knight = Knight('white', (1, 0), None)
        knight.calculate_valid_moves([], [])
        new_position = knight.move_to_selected_position((0, 3))
        self.assertNotEqual((0, 3), new_position)

# todo:
# test he can jump a pawn

if __name__ == '__main__':
    unittest.main()
