from Team_6_SW3.pieces.pawn import Pawn
import pygame

pygame.init()


class Settings:
    def __init__(self, image):
        # game variables
        self.WIDTH = 1000
        self.HEIGHT = 900
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        # self.board_size = pygame.draw.rect(600)
        self.game_over = False
        self.timer = pygame.time.Clock()
        self.fps = 60

        # Pieces in the board
        self.piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
        self.white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook']

        # Coordinates for pieces
        self.white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        self.black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook']

        self.black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

        self.black_piece_objects = [Pawn('black', (0, 6)), Pawn('black', (1, 6)),
                                    Pawn('black', (2, 6)), Pawn('black', (3, 6)),
                                    Pawn('black', (4, 6)), Pawn('black', (5, 6)),
                                    Pawn('black', (6, 6)), Pawn('black', (7, 6)),

                                    # King('black', (0, 6)), King('black', (1, 6)),
                                    # King('black', (2, 6)), King('black', (3, 6)),
                                    # King('black', (4, 6)), King('black', (5, 6)),
                                    # King('black', (6, 6)), King('black', (7, 6))
                                    ]

        self.white_piece_objects = [Pawn('white', (0, 1)), Pawn('white', (1, 1)),
                                    Pawn('white', (2, 1)), Pawn('white', (3, 1)),
                                    Pawn('white', (4, 1)), Pawn('white', (5, 1)),
                                    Pawn('white', (6, 1)), Pawn('white', (7, 1))]

        # Lists to keep track of captured pieces per team
        self.captured_pieces_white = []
        self.captured_pieces_black = []

        self.captured_piece_objects_white = []
        self.captured_piece_objects_black = []

        # Which phase we are, valid moves
        self.turn_step = 0
        # Current piece selection, default to a value not in the board
        self.selection = 100  # once done game.py delete me
        self.selected_piece = None
        self.valid_moves = []
        self.winner = ""
