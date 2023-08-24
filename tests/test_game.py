import unittest
from game import get_object_coords, get_clicked_white
from models.pieces.pawn import Pawn
from models.pieces.queen import Queen
from models.pieces.king import King
from models.pieces.rook import Rook
from models.pieces.bishop import Bishop
from models.pieces.knight import Knight

class GameTests(unittest.TestCase):


    def test_get_object_coords(self):
        # Arrange - set up the data to be passed to the function
        piece = Pawn('white', (0, 0))
        # Act - actually call the function and get the result
        coords = get_object_coords(piece)
        # Assert - check that the result you got from the function call is as exoected
        self.assertEqual((0, 0), coords)

    def test_get_clicked_white(self):
        coords = (0, 1)
        white_piece_objects = [Pawn('white', (0, 1)), Pawn('white', (1, 1)), Pawn('white', (2, 1)),
                               Pawn('white', (3, 1)), Pawn('white', (4, 1)), Pawn('white', (5, 1)),
                               Pawn('white', (6, 1)), Pawn('white', (7, 1)), King('white', (3, 0)),
                               Knight('white', (1, 0)), Knight('white', (6, 0)),
                               Rook('white', (0, 0)), Rook('white', (7, 0)),
                               Bishop('white', (2, 0)), Bishop('white', (5, 0)),
                               Queen('white', (4, 0))]
        coords = get_clicked_white(coords, white_piece_objects)
        self.assertEqual((0, 1), coords)


if __name__ == '__main__':
    unittest.main()
