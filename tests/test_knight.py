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

    def test_cannot_not_l(self):
        knight = Knight('white', (1, 0), None)
        knight.calculate_valid_moves([], [])
        new_position = knight.move_to_selected_position((0, 3))
        self.assertFalse((0, 3), new_position)



if __name__ == '__main__':
    unittest.main()
