from Team_6_SW3.models.pieces.pawn import Pawn
from Team_6_SW3.models.pieces.king import King
from Team_6_SW3.models.pieces.knight import Knight
from Team_6_SW3.models.pieces.rook import Rook
from Team_6_SW3.models.pieces.bishop import Bishop
from Team_6_SW3.models.pieces.queen import Queen


import pygame
pygame.init()


class Settings:
    def __init__(self):
        # game variables
        self.WIDTH = 1000
        self.HEIGHT = 900
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.game_over = False
        self.timer = pygame.time.Clock()
        self.fps = 60

        # Pieces in the board
        self.piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

        self.black_piece_objects = [Pawn('black', (0, 6)), Pawn('black', (1, 6)),
                                    Pawn('black', (2, 6)), Pawn('black', (3, 6)),
                                    Pawn('black', (4, 6)), Pawn('black', (5, 6)),
                                    Pawn('black', (6, 6)), Pawn('black', (7, 6)),

                                    King('black', (4, 7)),
                                    Knight('black', (1, 7)), Knight('black', (6, 7)),
                                    Rook('black', (7, 7)), Rook('black', (0, 7)),
                                    Bishop('black', (2, 7)), Bishop('black', (5, 7)),
                                    Queen('black', (3, 7))]

        self.white_piece_objects = [Pawn('white', (0, 1)), Pawn('white', (1, 1)),
                                    Pawn('white', (2, 1)), Pawn('white', (3, 1)),
                                    Pawn('white', (4, 1)), Pawn('white', (5, 1)),
                                    Pawn('white', (6, 1)), Pawn('white', (7, 1)),

                                    King('white', (4, 0)),
                                    Knight('white', (1, 0)), Knight('white', (6, 0)),
                                    Rook('white', (0, 0)), Rook('white', (7, 0)),
                                    Bishop('white', (2, 0)), Bishop('white', (5, 0)),
                                    Queen('white', (3, 0))]

        # Lists to keep track of captured pieces per player
        self.captured_piece_objects_white = []
        self.captured_piece_objects_black = []

        # Which phase we are, valid moves
        self.turn_step = 0
        # Current piece selection, default to a value not in the board
        self.selected_piece = None
        self.valid_moves = []
        self.winner = ""
