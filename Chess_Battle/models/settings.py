from Team_6_SW3.Chess_Battle.models.pieces.pawn import Pawn
from Team_6_SW3.Chess_Battle.models.pieces.king import King
from Team_6_SW3.Chess_Battle.models.pieces.knight import Knight
from Team_6_SW3.Chess_Battle.models.pieces.rook import Rook
from Team_6_SW3.Chess_Battle.models.pieces.bishop import Bishop
from Team_6_SW3.Chess_Battle.models.pieces.queen import Queen


import pygame
import json

pygame.init()


class Settings:
    def __init__(self):
        # game variables
        self.WIDTH = 1000
        self.HEIGHT = 900
        self.screen_ = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        self.win = pygame.Surface((self.WIDTH, self.HEIGHT))
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

        # Lists for notation conversion
        self.white_pieces_short = ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R', '', '', '', '', '', '', '', '']
        self.black_pieces_short = ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r', '', '', '', '', '', '', '', '']
        self.x_names = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

        # Which phase we are, valid moves
        self.turn_step = 0
        # Current piece selection, default to a value not in the board
        self.selected_piece = None
        self.valid_moves = []
        self.winner = ""

    # todo: self.selection doesn't exist anymore we need to use self.selected_piece
    def compute_notation(self, type, coords):
        if type == "black":
            return self.black_pieces_short[self.selection] + self.x_names[int(coords[0])] + str(int(coords[1]) + 1)
        else:
            return self.white_pieces_short[self.selection] + self.x_names[int(coords[0])] + str(int(coords[1]) + 1)

    def get_font(self, size=35):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font('assets/fonts/JetBrainsMono-Bold.ttf', size)  # add size variable to settings file

    def get_scale_factor_x(self):
        return self.screen_.get_size()[0] / self.WIDTH

    def get_scale_factor_y(self):
        return self.screen_.get_size()[1] / self.HEIGHT

    def write_json(self, file, contents):
        with open(f"{file}.json", "w") as output:
            json.dump(contents, output, indent=2)
