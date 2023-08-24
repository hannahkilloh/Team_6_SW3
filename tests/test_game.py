import unittest
import ..game


class GameTests(unittest.TestCase):
    def test_get_object_coords(self):
        self.piece = game('white', (0, 0), 'queen', (45, 45), (80, 80))
        piece =

        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
