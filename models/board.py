from threading import Timer

import pygame
from models.pieces.pawn import Pawn
from models.buttons import Button
from models.pieces.king import King
from models.helpers import get_file_path_from_root


class BoardSettings:
    def __init__(self, status_text_background, tile_border_colour,
                 font):
        self.status_text_background = status_text_background
        self.tile_border_colour = tile_border_colour
        self.font = pygame.font.Font(font, 20)
        self.medium_font = pygame.font.Font(font, 25)
        self.big_font = pygame.font.Font(font, 50)


class Board:
    def __init__(self, board_settings, settings):
        self.board_settings = board_settings
        self.settings = settings
        self.resign_button = Button(image=pygame.image.load(get_file_path_from_root("assets/images/resign_button.png")),
                                    pos=(900, 850), text_input="", font=self.settings.get_font(), base_color="blue",
                                    hovering_color='#7BFCFC', settings=self.settings)
        self.display_error = False
        self.error_message = ""

    def initialise(self):
        self.settings.timer.tick(self.settings.fps)
        # self.settings.win.fill(self.board_settings.tile_colour_1)
        # Adding the main game background and setting the position
        main_game_background = pygame.image.load(
            get_file_path_from_root("assets/images/chess_board_MAIN.png")).convert()
        self.settings.win.blit(main_game_background, (0, 0))

        self.draw_board()
        self.draw_pieces()
        self.draw_error()

    def draw_board(self):
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']

        if self.settings.game_over:
            # winning_screen()
            self.settings.win.blit(self.board_settings.medium_font.render(
                f'{self.settings.winner} won the game!', True, 'blue'), (120, 820))
        else:
            self.settings.win.blit(self.board_settings.medium_font.render(
                status_text[self.settings.turn_step], True, 'blue'), (150, 830))

        for button in [self.resign_button]:
            if pygame.mouse.get_pos()[0] in range(int(self.resign_button.rect.left *
                                                      self.settings.get_scale_factor_x()),
                                                  int(self.resign_button.rect.right *
                                                      self.settings.get_scale_factor_x())) \
                    and pygame.mouse.get_pos()[1] in range(int(self.resign_button.rect.top *
                                                               self.settings.get_scale_factor_y()),
                                                           int(self.resign_button.rect.bottom *
                                                               self.settings.get_scale_factor_y())):
                self.resign_button = Button(image=pygame.image.load(get_file_path_from_root("assets/images/resign_button_hover.png")),
                                            pos=(900, 850), text_input="", font=self.settings.get_font(),
                                            base_color="blue", hovering_color='#7BFCFC', settings=self.settings)
            else:
                self.resign_button = Button(image=pygame.image.load(get_file_path_from_root("assets/images/resign_button.png")),
                                            pos=(900, 850), text_input="", font=self.settings.get_font(),
                                            base_color="blue", hovering_color='#7BFCFC', settings=self.settings)
            button.update(self.settings.win)

    def draw_move_suggestions(self, colour, potential_moves):
        for i in range(len(potential_moves)):
            pygame.draw.circle(self.settings.win, colour,
                               (potential_moves[i][0] * 100 + 50, potential_moves[i][1] * 100 + 50), 5)

    def draw_flashing_check(self, king_piece):
        if king_piece.get_is_in_check():
            pygame.draw.rect(self.settings.win, 'red', [king_piece.get_current_position()[0] * 100 + 1,
                                                        king_piece.get_current_position()[1] * 100 + 1,
                                                        100, 100], 5)

    def draw_piece(self, piece):
        x_coord = 10
        y_coord = 10

        if isinstance(piece, Pawn):
            x_coord = 18
            y_coord = 24

        self.settings.win.blit(
            piece.get_image(),
            (piece.get_current_position()[0] * 100 + x_coord, piece.get_current_position()[1] * 100 + y_coord))

        if isinstance(piece, King):
            self.draw_flashing_check(piece)

    def draw_pieces(self):
        # drawing new object pieces onto the board. calling all these functions on each piece object
        for piece in self.settings.white_piece_objects:
            self.draw_piece(piece)

        for piece in self.settings.black_piece_objects:
            self.draw_piece(piece)

        if self.settings.selected_piece is not None:
            selected_piece_is_white = self.settings.selected_piece.get_colour() == 'white'
            colour = 'red' if selected_piece_is_white else 'yellow'
            pygame.draw.rect(self.settings.win, colour, [self.settings.selected_piece.get_current_position()[0]
                                                         * 100 + 1,
                                                         self.settings.selected_piece.get_current_position()[1]
                                                         * 100 + 1, 100, 100], 2)
            self.draw_move_suggestions(colour, self.settings.selected_piece.get_valid_moves())

    def draw_error(self):
        if self.display_error:
            invalid_selection = Button(image=pygame.image.load("assets/images/blank_button_long.png").convert_alpha(),
                                       pos=(400, 400), text_input=self.error_message, font=self.settings.get_font(),
                                       base_color="blue",
                                       hovering_color='#7BFCFC', settings=self.settings)
            invalid_selection.update(self.settings.win)

            hide_message_timer = Timer(1.0, self.hide_error_message)
            hide_message_timer.start()

    def display_error_message(self, message):
        self.display_error = True
        self.error_message = message

    def hide_error_message(self):
        self.display_error = False
        self.error_message = ""
