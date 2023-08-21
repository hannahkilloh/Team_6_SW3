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
        # self.board_size = pygame.draw.rect(600)
        self.game_over = False
        self.timer = pygame.time.Clock()
        self.fps = 60

        # Pieces in the board
        self.piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
        self.white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                             'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

        # Coordinates for pieces
        self.white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
        self.black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                             'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
        self.black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

        # Lists for notation conversion
        self.white_pieces_short = ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R', '', '', '', '', '', '', '', '']
        self.black_pieces_short = ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r', '', '', '', '', '', '', '', '']
        self.x_names = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

        # Lists to keep track of captured pieces per team
        self.captured_pieces_white = []
        self.captured_pieces_black = []

        # Which phase we are, valid moves
        self.turn_step = 0
        # Current piece selection, default to a value not in the board
        self.selection = 100
        self.valid_moves = []
        self.winner = ""

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
