import pygame

from models.history import History
from models.settings import Settings
from models.board import Board, BoardSettings
from models.pieces.pawn import Pawn
from models.pieces.queen import Queen
from models.pieces.king import King
from models.pieces.rook import Rook

pygame.init()
pygame.font.init()
pygame.display.set_icon(pygame.image.load('assets/images/chess_icon.ico'))

# can pass in any colours, to set theme up easier
board_settings = BoardSettings(
    '#0000D2', '#7BFCFC', 'white', '#0000D2', 'assets/fonts/JetBrainsMono-Regular.ttf')
settings = Settings()
board = Board(board_settings, settings)

# setup moves dictionary
history = History(settings)

def draw_captured_objects():
    for index in range(len(settings.captured_piece_objects_white)):
        settings.win.blit(settings.captured_piece_objects_white[index].get_small_image(), (825, 155 + 50 * index))
    for index in range(len(settings.captured_piece_objects_black)):
        settings.win.blit(settings.captured_piece_objects_black[index].get_small_image(), (925, 155 + 50 * index))


def get_object_coords(piece):
    return piece.get_current_position()


def get_clicked_white(click_coords):
    for piece in settings.white_piece_objects:
        if click_coords == piece.get_current_position():
            return piece


def get_clicked_black(click_coords):
    for piece in settings.black_piece_objects:
        if click_coords == piece.get_current_position():
            return piece


def get_white_object_coords():
    # maps through white_piece_objects array of objects and passes each object into the
    # get_object_co-ords function and returns the co-ords as an array
    return list(map(get_object_coords, settings.white_piece_objects))


def get_black_object_coords():
    # maps through black_piece_objects array of objects and passes each object into the
    # get_object_co-ords function and returns the co-ords as an array
    return list(map(get_object_coords, settings.black_piece_objects))


# loops through all piece objects passed to it and returns the king
def get_king(pieces):
    for piece in pieces:
        if isinstance(piece, King):
            return piece


def play_game():
    run = True
    while run:
        # todo: could possibly refactor w/b_object_coords as its duplicated
        # maps through white_piece_objects array of objects and passes each object into the
        # get_object_co-ords function and returns the co-ords as an array
        white_object_coords = list(map(get_object_coords, settings.white_piece_objects))
        black_object_coords = list(map(get_object_coords, settings.black_piece_objects))

        white_king = get_king(settings.white_piece_objects)
        black_king = get_king(settings.black_piece_objects)
        white_king.calculate_king_in_check(settings.black_piece_objects, white_object_coords, black_object_coords)
        black_king.calculate_king_in_check(settings.white_piece_objects, white_object_coords, black_object_coords)

        board.initialise()
        draw_captured_objects()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not settings.game_over:
                x_coord = (event.pos[0] / settings.get_scale_factor_x()) // 100  # x coord
                y_coord = (event.pos[1] / settings.get_scale_factor_y()) // 100  # y coord
                click_coords = (x_coord, y_coord)

                # if the step is 0 or 1 then it is the whites turn
                if settings.turn_step <= 1:
                    # maps through white_piece_objects array of objects and passes each object into the
                    # get_object_co-ords function and returns the co-ords as an array
                    white_object_coords = list(map(get_object_coords, settings.white_piece_objects))
                    black_object_coords = list(map(get_object_coords, settings.black_piece_objects))

                    if click_coords in white_object_coords:  # if white piece has been clicked
                        # King is selected and we are trying to move to Rook, but also we are allowed to castle on this Rook
                        if isinstance(settings.selected_piece, King) and isinstance(get_clicked_white(click_coords), Rook) and click_coords in settings.selected_piece.get_valid_moves():
                            if click_coords == (0, 0):  # short castle
                                settings.selected_piece.force_move_to_selected_position((1, 0))  # move king to short castle pos
                                for piece in settings.white_piece_objects:  # find short rook
                                    if piece.get_current_position() == (0, 0):
                                        piece.force_move_to_selected_position((2, 0))  # move rook to short castle pos
                            elif click_coords == (7, 0):  # long castle
                                settings.selected_piece.force_move_to_selected_position((5, 0))  # move king to long castle pos
                                for piece in settings.white_piece_objects:  # find long rook
                                    if piece.get_current_position() == (7, 0):
                                        piece.force_move_to_selected_position((4, 0))  # move rook to long castle pos
                            # end turn
                            settings.turn_step = 2  # turns back to other player now
                            # so resets the variable used for tracking the currently selected piece
                            settings.selected_piece = None

                        # Standard piece selection logic
                        else:
                            settings.selected_piece = get_clicked_white(click_coords)
                            settings.selected_piece.calculate_valid_moves(history, get_white_object_coords(),
                                                                          get_black_object_coords())

                            if settings.turn_step == 0:  # if steps is 0 it moves onto the next step(1)
                                settings.turn_step = 1
                    elif settings.selected_piece is not None and click_coords in \
                            settings.selected_piece.get_valid_moves():

                        # add move to history
                        history.move_history[history.cur_session]["white"].append([
                            settings.compute_notation(settings.selected_piece.get_current_position()),  # old position
                            settings.compute_notation(click_coords)  # new position
                        ])

                        # moves selected piece to position only if it is a valid move
                        settings.selected_piece.move_to_selected_position(click_coords)

                        # Pawn Promotion for bottom of board
                        if isinstance(settings.selected_piece, Pawn) and click_coords[1] == 7:
                            for index in range(len(settings.white_piece_objects)):
                                if settings.white_piece_objects[index].get_current_position() == click_coords:
                                    settings.white_piece_objects.pop(index)
                                    break
                            queen = Queen('white', (click_coords[0], click_coords[1]))
                            settings.white_piece_objects.append(queen)

                        if click_coords in black_object_coords:
                            black_piece = get_clicked_black(click_coords)
                            settings.captured_piece_objects_white.append(black_piece)

                            if isinstance(black_piece, King):
                                settings.winner = 'White'

                            # sets black piece array to new array excluding the one that has been clicked
                            settings.black_piece_objects = [
                                x for x in settings.black_piece_objects if x.get_current_position() != click_coords
                            ]
                            print(settings.black_piece_objects)

                        settings.turn_step = 2  # turns to other player now
                        # so resets the variable used for tracking the currently selected piece
                        settings.selected_piece = None

                # if the step is 2 or 3 then it is the blacks turn
                if settings.turn_step > 1:
                    # maps through white_piece_objects array of objects and passes each object into the
                    # get_object_co-ords function and returns the co-ords as an array
                    white_object_coords = list(map(get_object_coords, settings.white_piece_objects))
                    black_object_coords = list(map(get_object_coords, settings.black_piece_objects))

                    if click_coords in black_object_coords:  # if black piece has been clicked
                        # King is selected and we are trying to move to Rook, but also we are allowed to castle on this Rook
                        if isinstance(settings.selected_piece, King) and isinstance(get_clicked_black(click_coords), Rook) and click_coords in settings.selected_piece.get_valid_moves():
                            if click_coords == (0, 7):  # short castle
                                settings.selected_piece.force_move_to_selected_position((1, 7))  # move king to short castle pos
                                for piece in settings.black_piece_objects:  # find short rook
                                    if piece.get_current_position() == (0, 7):
                                        piece.force_move_to_selected_position((2, 7))  # move rook to short castle pos
                            elif click_coords == (7, 7):  # long castle
                                settings.selected_piece.force_move_to_selected_position((5, 7))  # move king to long castle pos
                                for piece in settings.black_piece_objects:  # find long rook
                                    if piece.get_current_position() == (7, 7):
                                        piece.force_move_to_selected_position((4, 7))  # move rook to long castle pos
                            # end turn
                            settings.turn_step = 0  # turns back to other player now
                            # so resets the variable used for tracking the currently selected piece
                            settings.selected_piece = None

                        # Standard piece selection logic
                        else:
                            settings.selected_piece = get_clicked_black(click_coords)
                            settings.selected_piece.calculate_valid_moves(history, get_white_object_coords(),
                                                                          get_black_object_coords())

                            if settings.turn_step == 2:  # if step is 2 it moves onto the next step(3) of black player
                                settings.turn_step = 3
                    elif settings.selected_piece is not None and click_coords in \
                            settings.selected_piece.get_valid_moves():

                        # add move to history
                        history.move_history[history.cur_session]["black"].append([
                            settings.compute_notation(settings.selected_piece.get_current_position()),  # old position
                            settings.compute_notation(click_coords)  # new position
                        ])

                        # moves selected piece to position only if it is a valid move
                        settings.selected_piece.move_to_selected_position(click_coords)

                        # Pawn Promotion for top
                        if isinstance(settings.selected_piece, Pawn) and click_coords[1] == 0:
                            for index in range(len(settings.black_piece_objects)):
                                if settings.black_piece_objects[index].get_current_position() == click_coords:
                                    settings.black_piece_objects.pop(index)
                                    break
                            queen = Queen('black', (click_coords[0], click_coords[1]))
                            settings.black_piece_objects.append(queen)

                        if click_coords in white_object_coords:
                            white_piece = get_clicked_white(click_coords)
                            settings.captured_piece_objects_black.append(white_piece)

                            if isinstance(white_piece, King):
                                settings.winner = 'Black'

                            # sets white piece array to new array excluding the one that has been clicked
                            settings.white_piece_objects = [
                                x for x in settings.white_piece_objects if x.get_current_position() != click_coords
                            ]

                        settings.turn_step = 0  # turns back to other player now
                        # so resets the variable used for tracking the currently selected piece
                        settings.selected_piece = None

                # checking if resign button has been clicked
                if board.resign_button.check_for_input(pygame.mouse.get_pos()):
                    settings.reset_game()

            scaled_win = pygame.transform.smoothscale(settings.win, settings.screen_.get_size())
            settings.screen_.blit(scaled_win, (0, 0))
        pygame.display.flip()

        if settings.winner != '':
            settings.game_over = True

    # dump the current moves on quit
    settings.write_json("moves", history.move_history)
    pygame.quit()
