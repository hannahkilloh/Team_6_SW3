from Team_6_SW3.models.pieces.pawn import Pawn

import pygame


class BoardSettings:
    def __init__(self, tile_colour_1, tile_colour_2, status_text_background, tile_border_colour,
                 font):
        self.tile_colour_1 = tile_colour_1
        self.tile_colour_2 = tile_colour_2
        self.status_text_background = status_text_background
        self.tile_border_colour = tile_border_colour
        self.font = pygame.font.Font(font, 20)
        self.medium_font = pygame.font.Font(font, 30)
        self.big_font = pygame.font.Font(font, 50)


class Board:
    def __init__(self, board_settings, settings):
        self.board_settings = board_settings
        self.settings = settings

    def initialise(self):
        self.settings.timer.tick(self.settings.fps)
        self.settings.screen.fill(self.board_settings.tile_colour_1)

        # Adding the main game background and setting the position
        main_game_background = pygame.image.load("assets/images/test_background_image.png").convert()
        self.settings.screen.blit(main_game_background, (0, 0))

        self.draw_board()
        self.draw_pieces()

    #  Function that will create the tiles of the board (8x8)
    def draw_board(self):

        for i in range(32):
            column = i % 4
            row = i // 4
            if row % 2 == 0:
                pygame.draw.rect(self.settings.screen, self.board_settings.tile_colour_2, [
                    600 - (column * 200), row * 100, 100, 100])
            else:
                pygame.draw.rect(self.settings.screen, self.board_settings.tile_colour_2, [
                    700 - (column * 200), row * 100, 100, 100])
        # pygame.draw.rect(self.settings.screen, self.board_settings.status_text_background, [
        #                  800, 0, self.settings.WIDTH, 100])
        # pygame.image.load(self.images("assets/images/test_background_image.png"))
        # pygame.draw.rect(self.settings.screen, self.board_settings.status_text_background, [
        #                  0, 800, self.settings.WIDTH, 100])
        # pygame.draw.rect(self.settings.screen, self.board_settings.tile_border_colour, [
        #                  0, 800, self.settings.WIDTH, 100], 2)
        # pygame.draw.rect(self.settings.screen, self.board_settings.tile_border_colour, [
        #                  800, 0, 200, self.settings.HEIGHT], 2)
        # pygame.draw.rect(self.settings.screen, self.board_settings.status_text_background, [
        #     0, 800, 200, self.settings.HEIGHT], 2)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        self.settings.screen.blit(self.board_settings.medium_font.render(
            status_text[self.settings.turn_step], True, 'blue'), (20, 820))

        # Adds horizontal and vertical lines to the board
        # for line in range(9):
        # pygame.draw.line(self.settings.screen, self.board_settings.tile_border_colour,
        #                  (0, 100 * line), (800, 100 * line), 2)
        # pygame.draw.line(self.settings.screen, self.board_settings.tile_border_colour,
        #                  (100 * line, 0), (100 * line, 800), 2)
        self.settings.screen.blit(self.board_settings.medium_font.render(
            'Resign?', True, 'blue'), (810, 830))

    def draw_move_suggestions(self, colour, potential_moves):
        for i in range(len(potential_moves)):
            pygame.draw.circle(self.settings.screen, colour,
                               (potential_moves[i][0] * 100 + 50, potential_moves[i][1] * 100 + 50), 5)

    def draw_piece(self, piece):
        x_coord = 10
        y_coord = 10

        if isinstance(piece, Pawn):
            x_coord = 22
            y_coord = 30

        self.settings.screen.blit(
            piece.get_image(),
            (piece.get_current_position()[0] * 100 + x_coord, piece.get_current_position()[1] * 100 + y_coord))

    def draw_pieces(self):  # draw pieces into the board
        # drawing new object pieces. calling all these functions on each piece object
        for piece in self.settings.white_piece_objects:
            self.draw_piece(piece)

        for piece in self.settings.black_piece_objects:
            self.draw_piece(piece)

        if self.settings.selected_piece is not None:
            selected_piece_is_white = self.settings.selected_piece.get_colour() == 'white'
            colour = 'red' if selected_piece_is_white else 'blue'
            pygame.draw.rect(self.settings.screen, colour, [self.settings.selected_piece.get_current_position()[0]
                                                            * 100 + 1,
                                                            self.settings.selected_piece.get_current_position()[1]
                                                            * 100 + 1,
                                                            100, 100], 2)
            self.draw_move_suggestions(colour, self.settings.selected_piece.get_valid_moves())
