import pygame
from models.settings import Settings
from models.images import Images


images = Images()

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

#  Function that will create the tiles of the board (8x8) there are 64 squares, we can draw the half


# if you look at lines 66 to 79 and lines 80 to 94, this code is almost identical except for a few small differences.
# You can refactor that code into a reusable function and call it once and pass in the white peice and another
# time and pass in the black pieces. The colour that's used for the piece selector (blue or red) could be a value
# which comes from the settings object too


# things like the font variables from line 12 to 14 seems like it should come from the settings too


class Board:
    def __init__(self, tile_colour_1, tile_colour_2, status_text_background, tile_border_colour):
        # Create an instance of the Settings class
        self.settings = Settings()
        self.tile_colour_1 = tile_colour_1
        self.tile_colour_2 = tile_colour_2
        self.status_text_background = status_text_background
        self.tile_border_colour = tile_border_colour

    def initialise(self):
        self.settings.timer.tick(self.settings.fps)
        self.settings.screen.fill(self.tile_colour_1)
        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        for i in range(32):
            column = i % 4
            row = i // 4
            if row % 2 == 0:
                pygame.draw.rect(self.settings.screen, self.tile_colour_2, [
                                 600 - (column * 200), row * 100, 100, 100])
            else:
                pygame.draw.rect(self.settings.screen, self.tile_colour_2, [
                                 700 - (column * 200), row * 100, 100, 100])
            pygame.draw.rect(self.settings.screen, self.status_text_background, [
                             0, 800, self.settings.WIDTH, 100])
            pygame.draw.rect(self.settings.screen, self.tile_border_colour, [
                             0, 800, self.settings.WIDTH, 100], 2)
            pygame.draw.rect(self.settings.screen, self.tile_border_colour, [
                             800, 0, 200, self.settings.HEIGHT], 2)
            status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                           'Black: Select a Piece to Move!', 'Black: Select a Destination!']
            self.settings.screen.blit(medium_font.render(
                status_text[self.settings.turn_step], True, 'black'), (20, 820))

            # Adds horizontal and vertical lines to the board
            for line in range(9):
                pygame.draw.line(self.settings.screen, self.tile_border_colour,
                                 (0, 100 * line), (800, 100 * line), 2)
                pygame.draw.line(self.settings.screen, self.tile_border_colour,
                                 (100 * line, 0), (100 * line, 800), 2)
            self.settings.screen.blit(medium_font.render(
                'Forfeit', True, 'white'), (810, 830))

#  draw pieces into the board

    def draw_pieces(self):
        for i in range(len(self.settings.white_pieces)):
            index = self.settings.piece_list.index(self.settings.white_pieces[i])
            if self.settings.white_pieces[i] == 'pawn':
                self.settings.screen.blit(
                    images.white_pawn, (self.settings.white_locations[i][0] * 100 + 22,
                                        self.settings.white_locations[i][1] * 100 + 30))
            else:
                self.settings.screen.blit(images.white_images[index], (
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
                    images.black_pawn, (self.settings.black_locations[i][0] * 100 + 22,
                                        self.settings.black_locations[i][1] * 100 + 30))
            else:
                self.settings.screen.blit(images.black_images[index], (
                    self.settings.black_locations[i][0] * 100 + 10, self.settings.black_locations[i][1] * 100 + 10))
            if self.settings.turn_step >= 2:
                if self.settings.selection == i:
                    pygame.draw.rect(self.settings.screen, 'blue', [self.settings.black_locations[i][0] * 100 + 1,
                                                                    self.settings.black_locations[i][1] * 100 + 1,
                                                                    100, 100], 2)
