import unittest
from models.helpers import get_friends_and_enemies


class TestHelpersFunctions(unittest.TestCase):
    def test_get_friends_and_enemies(self):
        white_locations = [(1, 2), (3, 4)]
        black_locations = [(5, 6), (7, 8)]

        # Test with 'white' color
        friends, enemies = get_friends_and_enemies(
            'white', white_locations, black_locations)
        self.assertEqual(friends, white_locations)
        self.assertEqual(enemies, black_locations)

        # Test with 'black' color
        friends, enemies = get_friends_and_enemies(
            'black', white_locations, black_locations)
        self.assertEqual(friends, black_locations)
        self.assertEqual(enemies, white_locations)


if __name__ == '__main__':
    unittest.main()
