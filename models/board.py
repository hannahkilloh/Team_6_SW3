import pygame


class BoardSettings:
    def __init__(self, tile_colour_1, tile_colour_2, status_text_background, tile_border_colour,
                 font):
        self.tile_colour_1 = tile_colour_1
        self.tile_colour_2 = tile_colour_2
        self.status_text_background = status_text_background
        self.tile_border_colour = tile_border_colour
        self.font = pygame.font.Font(font, 20)
        self.medium_font = pygame.font.Font(font, 40)
        self.big_font = pygame.font.Font(font, 50)


class Board:
    def __init__(self, board_settings, settings, images):
        self.board_settings = board_settings
        self.settings = settings
        self.images = images

    def initialise(self):
        self.settings.timer.tick(self.settings.fps)
        self.settings.screen.fill(self.board_settings.tile_colour_1)
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
            pygame.draw.rect(self.settings.screen, self.board_settings.status_text_background, [
                             0, 800, self.settings.WIDTH, 100])
            pygame.draw.rect(self.settings.screen, self.board_settings.tile_border_colour, [
                             0, 800, self.settings.WIDTH, 100], 2)
            pygame.draw.rect(self.settings.screen, self.board_settings.tile_border_colour, [
                             800, 0, 200, self.settings.HEIGHT], 2)
            status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                           'Black: Select a Piece to Move!', 'Black: Select a Destination!']
            self.settings.screen.blit(self.board_settings.medium_font.render(
                status_text[self.settings.turn_step], True, 'black'), (20, 820))

            # Adds horizontal and vertical lines to the board
            for line in range(9):
                pygame.draw.line(self.settings.screen, self.board_settings.tile_border_colour,
                                 (0, 100 * line), (800, 100 * line), 2)
                pygame.draw.line(self.settings.screen, self.board_settings.tile_border_colour,
                                 (100 * line, 0), (100 * line, 800), 2)
            self.settings.screen.blit(self.board_settings.medium_font.render(
                'Sacrifice', True, 'white'), (810, 830))

    def draw_pieces(self):  # draw pieces into the board
        for i in range(len(self.settings.white_pieces)):
            index = self.settings.piece_list.index(self.settings.white_pieces[i])
            if self.settings.white_pieces[i] == 'pawn':
                self.settings.screen.blit(
                    self.images.white_pawn, (self.settings.white_locations[i][0] * 100 + 22,
                                             self.settings.white_locations[i][1] * 100 + 30))
            else:
                self.settings.screen.blit(self.images.white_images[index], (
                    self.settings.white_locations[i][0] * 100 + 1, self.settings.white_locations[i][1] * 100 + 10))
            if self.settings.turn_step < 2:
                if self.settings.selection == i:
                    pygame.draw.rect(self.settings.screen, 'red', [self.settings.white_locations[i][0] * 100 + 1,
                                                                   self.settings.white_locations[i][1] * 100 + 1,
                                                                   100, 100], 2)
        for i in range(len(self.settings.black_pieces)):
            index = self.settings.piece_list.index(self.settings.black_pieces[i])
            if self.settings.black_pieces[i] == 'pawn':
                self.settings.screen.blit(
                    self.images.black_pawn, (self.settings.black_locations[i][0] * 100 + 22,
                                             self.settings.black_locations[i][1] * 100 + 30))
            else:
                self.settings.screen.blit(self.images.black_images[index], (
                    self.settings.black_locations[i][0] * 100 + 10, self.settings.black_locations[i][1] * 100 + 10))
            if self.settings.turn_step >= 2:
                if self.settings.selection == i:
                    pygame.draw.rect(self.settings.screen, 'blue', [self.settings.black_locations[i][0] * 100 + 1,
                                                                    self.settings.black_locations[i][1] * 100 + 1,
                                                                    100, 100], 2)
