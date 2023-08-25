from models.pieces.pawn import Pawn
from models.pieces.king import King
from models.pieces.knight import Knight
from models.pieces.rook import Rook
from models.pieces.bishop import Bishop
from models.pieces.queen import Queen
from models.helpers import get_file_path_from_root


import os
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
        self.timer = pygame.time.Clock()
        self.fps = 60

        # Lists for notation conversion
        self.x_names = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

        # Declare game reset related object properties here because they have to be done in the class init
        # We then call the 'reset_game' function which populated all the correct values
        self.game_over = False
        self.white_piece_objects = []
        self.black_piece_objects = []
        self.white_king = None
        self.black_king = None
        # Lists to keep track of captured pieces per player
        self.captured_piece_objects_white = []
        self.captured_piece_objects_black = []
        self.turn_step = 0
        # Current piece selection, default to a value not in the board
        self.selected_piece = None
        self.winner = ""
        self.history_being_shown = -1
        self.reset_game()

    def reset_game(self):
        self.game_over = False
        self.turn_step = 0
        # Current piece selection, default to a value not in the board
        self.selected_piece = None
        self.winner = ""
        self.black_piece_objects = [Pawn('black', (0, 6)), Pawn('black', (1, 6)),
                                    Pawn('black', (2, 6)), Pawn('black', (3, 6)),
                                    Pawn('black', (4, 6)), Pawn('black', (5, 6)),
                                    Pawn('black', (6, 6)), Pawn('black', (7, 6)),

                                    King('black', (3, 7)),
                                    Knight('black', (1, 7)), Knight('black', (6, 7)),
                                    Rook('black', (7, 7)), Rook('black', (0, 7)),
                                    Bishop('black', (2, 7)), Bishop('black', (5, 7)),
                                    Queen('black', (4, 7))]

        self.white_piece_objects = [Pawn('white', (0, 1)), Pawn('white', (1, 1)),
                                    Pawn('white', (2, 1)), Pawn('white', (3, 1)),
                                    Pawn('white', (4, 1)), Pawn('white', (5, 1)),
                                    Pawn('white', (6, 1)), Pawn('white', (7, 1)),

                                    King('white', (3, 0)),
                                    Knight('white', (1, 0)), Knight('white', (6, 0)),
                                    Rook('white', (0, 0)), Rook('white', (7, 0)),
                                    Bishop('white', (2, 0)), Bishop('white', (5, 0)),
                                    Queen('white', (4, 0))]

        self.captured_piece_objects_white = []
        self.captured_piece_objects_black = []

    def compute_notation(self, coords):
        return self.selected_piece.get_short_notation() + self.x_names[int(coords[0])] + str(int(coords[1]) + 1)

    def get_font(self, size=35):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font(get_file_path_from_root('assets/fonts/JetBrainsMono-Bold.ttf'), size)  # add size variable to settings file

    def get_scale_factor_x(self):
        return self.screen_.get_size()[0] / self.WIDTH

    def get_scale_factor_y(self):
        return self.screen_.get_size()[1] / self.HEIGHT

    def load_json(self, file):
        if not os.path.exists(f"{file}.json"):
            self.write_json("moves", {})
        with open(f"{file}.json") as open_file:
            return json.load(open_file)

    def write_json(self, file, contents):
        with open(f"{file}.json", "w") as output:
            json.dump(contents, output, indent=2)
