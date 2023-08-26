import unittest
from models.pieces.knight import Knight


class KnightTests(unittest.TestCase):
    def test_white_calculate_valid_moves(self):
        knight = Knight('white', (1, 0))
        valid_moves = knight.calculate_valid_moves(None, [], [])
        self.assertCountEqual([(2, 2), (3, 1), (0, 2)], valid_moves)

    def test_black_calculate_valid_moves(self):
        knight = Knight('black', (1, 7))
        valid_moves = knight.calculate_valid_moves(None, [], [])
        self.assertCountEqual([(2, 5), (3, 6), (0, 5)], valid_moves)

    def test_moved_white_calculate_valid_moves(self):
        knight = Knight('white', (1, 0))
        knight.calculate_valid_moves(None, [], [])
        new_position = knight.move_to_selected_position((2, 2))
        self.assertEqual((2, 2), new_position)

    def test_moved_black_calculate_valid_moves(self):
        knight = Knight('black', (1, 7))
        knight.calculate_valid_moves(None, [], [])
        new_position = knight.move_to_selected_position((0, 5))
        self.assertEqual((0, 5), new_position)

    def test_invalid_edge_calculate_valid_move(self):
        knight = Knight('white', (1, 0))
        knight.calculate_valid_moves(None, [], [])
        new_position = knight.move_to_selected_position((0, 3))
        self.assertNotEqual((0, 3), new_position)

    def test_can_jump_friend_move(self):
        knight = Knight('white', (0, 0))
        knight.calculate_valid_moves(None, [(0, 2)], [])
        new_position = knight.move_to_selected_position((1, 2))
        self.assertEqual((1, 2), new_position)

    def test_can_jump_friend_black_move(self):
        knight = Knight('black', (0, 0))
        knight.calculate_valid_moves(None, [], [(0, 2)])
        new_position = knight.move_to_selected_position((1, 2))
        self.assertEqual((1, 2), new_position)

    def test_can_jump_enemy_white_move(self):
        knight = Knight('black', (0, 0))
        knight.calculate_valid_moves(None, [(0, 2)], [])
        new_position = knight.move_to_selected_position((1, 2))
        self.assertEqual((1, 2), new_position)

    def test_can_jump_enemy_black_move(self):
        knight = Knight('white', (0, 0))
        knight.calculate_valid_moves(None, [], [(0, 2)])
        new_position = knight.move_to_selected_position((1, 2))
        self.assertEqual((1, 2), new_position)

    def test_no_move_if_blocked_by_friend(self):
        knight = Knight('white', (1, 0))
        knight.calculate_valid_moves(None, [(0, 2), (2, 2), (3, 1)], [])
        new_position = knight.move_to_selected_position((0, 2))
        self.assertNotEqual((0, 2), new_position)

    def test_captures_black_piece(self):
        knight = Knight('white', (1, 0))
        knight.calculate_valid_moves(None, [], [(0, 2), (2, 2), (3, 1)])
        new_position = knight.move_to_selected_position((0, 2))
        self.assertEqual((0, 2), new_position)

    def test_captures_black_piece_edge_case(self):
        knight = Knight('white', (0, 0))
        knight.calculate_valid_moves(None, [], [(2, 1), (1, 2)])
        new_position = knight.move_to_selected_position((1, 2))
        self.assertEqual((1, 2), new_position)

    def test_captures_white_piece(self):
        knight = Knight('black', (1, 7))
        knight.calculate_valid_moves(None, [(2, 5), (3, 6), (0, 5)], [])
        new_position = knight.move_to_selected_position((2, 5))
        self.assertEqual((2, 5), new_position)


if __name__ == '__main__':
    unittest.main()

