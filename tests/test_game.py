import unittest
from game import get_object_coords, get_clicked_piece, get_all_object_coords, pawn_promotion_for_white, get_king, \
    pawn_promotion_for_black
from models.pieces.pawn import Pawn
from models.pieces.queen import Queen
from models.pieces.king import King
from models.pieces.rook import Rook
from models.pieces.bishop import Bishop
from models.pieces.knight import Knight


class GameTests(unittest.TestCase):
    def test_get_object_coords(self):
        piece = Pawn('white', (0, 0))
        coords = get_object_coords(piece)
        self.assertEqual((0, 0), coords)

    def test_off_board_coords_get_object_coords(self):
        piece = Pawn('white', (100, 100))
        coords = get_object_coords(piece)
        self.assertEqual((100, 100), coords)

    def test_invalid_get_object_coords(self):
        piece = Pawn('white', (10, 10))
        coords = get_object_coords(piece)
        self.assertNotEqual((100, 100), coords)

    def test_edgecase_black_get_object_coords(self):
        piece = Rook('black', (7, 7))
        coords = get_object_coords(piece)
        self.assertEqual((7, 7), coords)

    def test_valid_get_clicked_piece(self):
        coords = (0, 1)
        white_piece_objects = [Pawn('white', (0, 1)), Pawn('white', (1, 1)), Pawn('white', (2, 1)),
                               Pawn('white', (3, 1)), Pawn('white', (4, 1)), Pawn('white', (5, 1)),
                               Pawn('white', (6, 1)), Pawn('white', (7, 1)), King('white', (3, 0)),
                               Knight('white', (1, 0)), Knight('white', (6, 0)),
                               Rook('white', (0, 0)), Rook('white', (7, 0)),
                               Bishop('white', (2, 0)), Bishop('white', (5, 0)),
                               Queen('white', (4, 0))]
        piece = get_clicked_piece(coords, white_piece_objects)
        self.assertTrue(isinstance(piece, Pawn))

    def test_invalid_get_clicked_piece(self):
        coords = (1, 0)
        white_piece_objects = [Pawn('white', (0, 1)), Pawn('white', (1, 1)), Pawn('white', (2, 1)),
                               Pawn('white', (3, 1)), Pawn('white', (4, 1)), Pawn('white', (5, 1)),
                               Pawn('white', (6, 1)), Pawn('white', (7, 1)), King('white', (3, 0)),
                               Knight('white', (1, 0)), Knight('white', (6, 0)),
                               Rook('white', (0, 0)), Rook('white', (7, 0)),
                               Bishop('white', (2, 0)), Bishop('white', (5, 0)),
                               Queen('white', (4, 0))]
        piece = get_clicked_piece(coords, white_piece_objects)
        self.assertFalse(isinstance(piece, Pawn))

    def test_invalid_coord_get_clicked_piece(self):
        coords = (9, 10)
        white_piece_objects = [Pawn('white', (0, 1)), Pawn('white', (1, 1)), Pawn('white', (2, 1)),
                               Pawn('white', (3, 1)), Pawn('white', (4, 1)), Pawn('white', (5, 1)),
                               Pawn('white', (6, 1)), Pawn('white', (7, 1)), King('white', (3, 0)),
                               Knight('white', (1, 0)), Knight('white', (6, 0)),
                               Rook('white', (0, 0)), Rook('white', (7, 0)),
                               Bishop('white', (2, 0)), Bishop('white', (5, 0)),
                               Queen('white', (4, 0))]
        piece = get_clicked_piece(coords, white_piece_objects)
        self.assertFalse(isinstance(piece, Pawn))

    def test_valid_edge_coord_get_clicked_piece(self):
        coords = (4, 0)
        white_piece_objects = [Pawn('white', (0, 1)), Pawn('white', (1, 1)), Pawn('white', (2, 1)),
                               Pawn('white', (3, 1)), Pawn('white', (4, 1)), Pawn('white', (5, 1)),
                               Pawn('white', (6, 1)), Pawn('white', (7, 1)), King('white', (3, 0)),
                               Knight('white', (1, 0)), Knight('white', (6, 0)),
                               Rook('white', (0, 0)), Rook('white', (7, 0)),
                               Bishop('white', (2, 0)), Bishop('white', (5, 0)),
                               Queen('white', (4, 0))]
        piece = get_clicked_piece(coords, white_piece_objects)
        self.assertTrue(isinstance(piece, Queen))

    def test_one_object_get_clicked_piece(self):
        coords = (7, 0)
        white_piece_objects = [Rook('white', (7, 0))]
        piece = get_clicked_piece(coords, white_piece_objects)
        self.assertTrue(isinstance(piece, Rook))

    def test_black_piece_get_clicked_piece(self):
        coords = (7, 7)
        white_piece_objects = [Rook('black', (7, 7))]
        piece = get_clicked_piece(coords, white_piece_objects)
        self.assertTrue(isinstance(piece, Rook))

    def test_get_all_object_coords(self):
        piece_objects = [Pawn('white', (0, 1)), Pawn('white', (1, 1)), Pawn('white', (2, 1)), Pawn('white', (3, 1)),
                         Pawn('white', (4, 1)), Pawn('white', (5, 1)), Pawn('white', (6, 1)), Pawn('white', (7, 1))]
        piece = get_all_object_coords(piece_objects)
        coord_list = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
        self.assertCountEqual(coord_list, piece)

    def test_invalid_get_all_object_coords(self):
        piece_objects = [Pawn('white', (0, 1)), Pawn('white', (1, 1)), Pawn('white', (2, 1)), Pawn('white', (3, 1)),
                         Pawn('white', (4, 1)), Pawn('white', (5, 1)), Pawn('white', (6, 1)), Pawn('white', (7, 1))]
        piece = get_all_object_coords(piece_objects)
        coord_list = [(9, 1), (16, 1), (70, 11)]
        self.assertNotEqual(coord_list, piece)

    def test_edge_case_get_all_object_coords(self):
        piece_objects = [Pawn('white', (0, 1))]
        piece = get_all_object_coords(piece_objects)
        coord_list = [(0, 1)]
        self.assertEqual(coord_list, piece)

    def test_edge_case_empty_get_all_object_coords(self):
        piece_objects = []
        piece = get_all_object_coords(piece_objects)
        self.assertCountEqual([], piece)

    def test_white_get_king(self):
        piece = [King('white', (3, 0))]
        king = get_king(piece)
        self.assertTrue(isinstance(king, King))

    def test_black_get_king(self):
        piece = [King('black', (3, 7))]
        king = get_king(piece)
        self.assertTrue(isinstance(king, King))

    def test_invalid_get_king(self):
        piece = [Pawn('white', (3, 0))]
        pawn = get_king(piece)
        self.assertFalse(isinstance(pawn, King))

    def test_pawn_promotion_for_white(self):
        coords = (6, 7)
        piece = Pawn('white', (6, 7))
        piece_objects = [Pawn('white', (6, 7)), Pawn('white', (1, 1)), Pawn('white', (2, 1)), Pawn('white', (3, 1)),
                         Pawn('white', (4, 1)), Pawn('white', (5, 1)), Pawn('white', (6, 1)), Pawn('white', (7, 1)),
                         King('white', (3, 0)), Knight('white', (1, 0)), Knight('white', (6, 0)), Rook('white', (0, 0)),
                         Rook('white', (7, 0)), Bishop('white', (2, 0)), Bishop('white', (5, 0))]
        pawn_promotion_for_white(coords, piece, piece_objects)
        queen = piece_objects[len(piece_objects)-1]
        pawn_promoted = isinstance(queen, Queen)
        self.assertTrue(pawn_promoted)

    def test_pawn_promotion_for_black(self):
        coords = (6, 0)
        piece = Pawn('black', (6, 0))
        piece_objects = [Pawn('black', (0, 6)), Pawn('black', (1, 6)), Pawn('black', (2, 6)), Pawn('black', (3, 6)),
                         Pawn('black', (4, 6)), Pawn('black', (5, 6)), Pawn('black', (6, 6)), Pawn('black', (7, 6)),
                         King('black', (3, 7)), Knight('black', (1, 7)), Knight('black', (6, 7)), Rook('black', (7, 7)),
                         Rook('black', (0, 7)), Bishop('black', (2, 7)), Bishop('black', (5, 7))]
        pawn_promotion_for_black(coords, piece, piece_objects)
        queen = piece_objects[len(piece_objects)-1]
        pawn_promoted = isinstance(queen, Queen)
        self.assertTrue(pawn_promoted)

    def test_invalid_coord_for_pawn_promotion_for_black(self):
        coords = (6, 2)
        piece = Pawn('black', (6, 2))
        piece_objects = [Pawn('black', (0, 6)), Pawn('black', (1, 6)), Pawn('black', (2, 6)), Pawn('black', (3, 6)),
                         Pawn('black', (4, 6)), Pawn('black', (5, 6)), Pawn('black', (6, 6)), Pawn('black', (7, 6)),
                         King('black', (3, 7)), Knight('black', (1, 7)), Knight('black', (6, 7)), Rook('black', (7, 7)),
                         Rook('black', (0, 7)), Bishop('black', (2, 7)), Bishop('black', (5, 7))]
        pawn_promotion_for_black(coords, piece, piece_objects)
        queen = piece_objects[len(piece_objects)-1]
        pawn_promoted = isinstance(queen, Queen)
        self.assertFalse(pawn_promoted)

    def test_invalid_piece_for_pawn_promotion_for_black(self):
        coords = (6, 0)
        piece = Rook('black', (6, 0))
        piece_objects = [Pawn('black', (0, 6)), Pawn('black', (1, 6)), Pawn('black', (2, 6)), Pawn('black', (3, 6)),
                         Pawn('black', (4, 6)), Pawn('black', (5, 6)), Pawn('black', (6, 6)), Pawn('black', (7, 6)),
                         King('black', (3, 7)), Knight('black', (1, 7)), Knight('black', (6, 7)), Rook('black', (7, 7)),
                         Rook('black', (0, 7)), Bishop('black', (2, 7)), Bishop('black', (5, 7))]
        pawn_promotion_for_black(coords, piece, piece_objects)
        queen = piece_objects[len(piece_objects)-1]
        pawn_promoted = isinstance(queen, Queen)
        self.assertFalse(pawn_promoted)


# todo test castling once coverted to function in here


if __name__ == '__main__':
    unittest.main()
