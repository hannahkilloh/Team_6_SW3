import pygame

import menu
from models.history import History
from models.settings import Settings
from models.board import Board, BoardSettings
from models.pieces.pawn import Pawn
from models.pieces.queen import Queen
from models.pieces.king import King
from models.pieces.rook import Rook
from models.helpers import get_file_path_from_root

pygame.init()
pygame.font.init()
pygame.display.set_icon(pygame.image.load(get_file_path_from_root('assets/images/chess_icon.ico')))

board_settings = BoardSettings('white', '#0000D2', get_file_path_from_root('assets/fonts/JetBrainsMono-Regular.ttf'))
settings = Settings()
board = Board(board_settings, settings)

# setup moves dictionary
history = History(settings)


def draw_captured_objects():
    for index in range(len(settings.captured_piece_objects_white)):
        settings.win.blit(settings.captured_piece_objects_white[index].get_small_image(), (830, 155 + 50 * index))
    for index in range(len(settings.captured_piece_objects_black)):
        settings.win.blit(settings.captured_piece_objects_black[index].get_small_image(), (920, 155 + 50 * index))


def get_object_coords(piece):
    return piece.get_current_position()


def get_clicked_piece(click_coords, piece_objects):
    for piece in piece_objects:
        if click_coords == piece.get_current_position():
            return piece


def get_all_object_coords(piece_objects):
    # maps through white_piece_objects array of objects and passes each object into the
    # get_object_co-ords function and returns the co-ords as an array
    return list(map(get_object_coords, piece_objects))


# loops through all piece objects passed to it and returns the king
def get_king(pieces):
    for piece in pieces:
        if piece.get_piece_type() == "king":
            return piece


def pawn_promotion_for_white(click_coords, selected_piece, white_piece_objects):
    if isinstance(selected_piece, Pawn) and click_coords[1] == 7:
        for index in range(len(white_piece_objects)):
            if white_piece_objects[index].get_current_position() == click_coords:
                white_piece_objects.pop(index)
                break

        queen = Queen('white', (click_coords[0], click_coords[1]))
        white_piece_objects.append(queen)


def pawn_promotion_for_black(click_coords, selected_piece, black_piece_objects):
    if isinstance(selected_piece, Pawn) and click_coords[1] == 0:
        for index in range(len(black_piece_objects)):
            if black_piece_objects[index].get_current_position() == click_coords:
                black_piece_objects.pop(index)
                break

        queen = Queen('black', (click_coords[0], click_coords[1]))
        black_piece_objects.append(queen)


class InvalidSelectionError(Exception):
    pass


# dump the current moves to the file system
def dump_move_history():
    settings.write_json("moves", history.move_history)

def play_game():
    run = True
    while run:
        # maps through white_piece_objects array of objects and passes each object into the
        # get_object_co-ords function and returns the co-ords as an array
        white_object_coords = list(map(get_object_coords, settings.white_piece_objects))
        black_object_coords = list(map(get_object_coords, settings.black_piece_objects))

        settings.white_king = get_king(settings.white_piece_objects)
        settings.black_king = get_king(settings.black_piece_objects)

        if settings.white_king is not None:
            settings.white_king.calculate_king_in_check(settings.black_piece_objects, white_object_coords,
                                                        black_object_coords)

        if settings.black_king is not None:
            settings.black_king.calculate_king_in_check(settings.white_piece_objects, white_object_coords,
                                                        black_object_coords)

        board.initialise()
        draw_captured_objects()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            try:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not settings.game_over:
                    x_coord = int((event.pos[0] / settings.get_scale_factor_x()) // 100)
                    y_coord = int((event.pos[1] / settings.get_scale_factor_y()) // 100)
                    click_coords = (x_coord, y_coord)

                    if settings.turn_step == 0 and click_coords not in white_object_coords and \
                                board.resign_button.check_for_input(pygame.mouse.get_pos()) is False:
                        raise InvalidSelectionError("Select white")
                    elif settings.turn_step == 2 and click_coords not in black_object_coords and \
                                board.resign_button.check_for_input(pygame.mouse.get_pos()) is False:
                        raise InvalidSelectionError("Select black")

                    # if the step is 0 or 1 then it is the whites turn
                    if settings.turn_step <= 1:
                        white_object_coords = get_all_object_coords(settings.white_piece_objects)
                        black_object_coords = get_all_object_coords(settings.black_piece_objects)

                        if click_coords in white_object_coords:  # if white piece has been clicked
                            # King is selected, and we are trying to move to Rook, but allowed to castle on this Rook

                            if isinstance(settings.selected_piece, King) and \
                                    isinstance(get_clicked_piece(click_coords, settings.white_piece_objects), Rook) \
                                    and click_coords in settings.selected_piece.get_valid_moves():
                                if click_coords == (0, 0):  # short castle
                                    settings.selected_piece.force_move_to_selected_position(
                                        (1, 0))  # move king to short castle pos
                                    for piece in settings.white_piece_objects:  # find short rook
                                        if piece.get_current_position() == (0, 0):
                                            piece.force_move_to_selected_position((2, 0))  # move rook to short castle
                                elif click_coords == (7, 0):  # long castle
                                    settings.selected_piece.force_move_to_selected_position(
                                        (5, 0))  # move king to long castle pos
                                    for piece in settings.white_piece_objects:  # find long rook
                                        if piece.get_current_position() == (7, 0):
                                            piece.force_move_to_selected_position((4, 0))  # move rook to long castle

                                settings.turn_step = 2  # turns back to other player now
                                # so resets the variable used for tracking the currently selected piece
                                settings.selected_piece = None

                            # Standard piece selection logic
                            else:
                                settings.selected_piece = get_clicked_piece(click_coords, settings.white_piece_objects)
                                settings.selected_piece.calculate_valid_moves(
                                    history, get_all_object_coords(settings.white_piece_objects),
                                    get_all_object_coords(settings.black_piece_objects))

                                # test for check
                                settings.selected_piece.check_valid_moves_for_check(
                                    get_all_object_coords(settings.white_piece_objects),
                                    get_all_object_coords(settings.black_piece_objects), settings)

                                if settings.turn_step == 0:  # if steps is 0 it moves onto the next step(1)
                                    settings.turn_step = 1

                        elif settings.selected_piece is not None and click_coords not in \
                                settings.selected_piece.get_valid_moves() and \
                                board.resign_button.check_for_input(pygame.mouse.get_pos()) is False:
                            raise InvalidSelectionError("Invalid move")

                        elif settings.selected_piece is not None and click_coords in \
                                settings.selected_piece.get_valid_moves():

                            # add move to history
                            history.move_history[history.cur_session].append([
                                settings.compute_notation(settings.selected_piece.get_current_position()),
                                settings.compute_notation(click_coords)  # new position
                            ])

                            # moves selected piece to position only if it is a valid move
                            settings.selected_piece.move_to_selected_position(click_coords)

                            # Pawn Promotion for bottom of board
                            pawn_promotion_for_white(click_coords, settings.selected_piece, settings.white_piece_objects)

                            if click_coords in black_object_coords:
                                black_piece = get_clicked_piece(click_coords, settings.black_piece_objects)
                                settings.captured_piece_objects_white.append(black_piece)

                                # sets black piece array to new array excluding the one that has been clicked
                                settings.black_piece_objects = [
                                    x for x in settings.black_piece_objects if x.get_current_position() != click_coords
                                ]

                            # check if black's king is in check and out of moves, thus making white the winner
                            settings.black_king.calculate_king_in_check(
                                settings.black_piece_objects, get_all_object_coords(settings.white_piece_objects),
                                get_all_object_coords(settings.black_piece_objects))

                            settings.black_king.calculate_valid_moves(
                                history, get_all_object_coords(settings.white_piece_objects),
                                get_all_object_coords(settings.black_piece_objects))
                            settings.black_king.check_valid_moves_for_check(
                                get_all_object_coords(settings.white_piece_objects),
                                get_all_object_coords(settings.black_piece_objects), settings)

                            if settings.black_king.get_is_in_check() and \
                                    len(settings.black_king.get_valid_moves()) == 0:
                                settings.winner = 'White'
                                settings.reset_game()
                                dump_move_history()
                                menu.winning_screen("White")

                            settings.turn_step = 2  # turns to other player now
                            # so resets the variable used for tracking the currently selected piece
                            settings.selected_piece = None

                    # if the step is 2 or 3 then it is the blacks turn
                    if settings.turn_step > 1:
                        white_object_coords = list(map(get_object_coords, settings.white_piece_objects))
                        black_object_coords = list(map(get_object_coords, settings.black_piece_objects))

                        if click_coords in black_object_coords:  # if black piece has been clicked
                            # King is selected and we are trying to move to Rook, but also we are allowed to castle on this Rook

                            if isinstance(settings.selected_piece, King) \
                                    and isinstance(get_clicked_piece(click_coords, settings.black_piece_objects), Rook)\
                                    and click_coords in settings.selected_piece.get_valid_moves():
                                if click_coords == (0, 7):  # short castle
                                    settings.selected_piece.force_move_to_selected_position(
                                        (1, 7))  # move king to short castle pos
                                    for piece in settings.black_piece_objects:  # find short rook
                                        if piece.get_current_position() == (0, 7):
                                            piece.force_move_to_selected_position((2, 7))  # move rook to short castle
                                elif click_coords == (7, 7):  # long castle
                                    settings.selected_piece.force_move_to_selected_position(
                                        (5, 7))  # move king to long castle pos
                                    for piece in settings.black_piece_objects:  # find long rook
                                        if piece.get_current_position() == (7, 7):
                                            piece.force_move_to_selected_position((4, 7))  # move rook to long castle
                                # end turn
                                settings.turn_step = 0
                                settings.selected_piece = None

                            # Standard piece selection logic
                            else:
                                settings.selected_piece = get_clicked_piece(click_coords, settings.black_piece_objects)
                                settings.selected_piece.calculate_valid_moves(
                                    history, get_all_object_coords(settings.white_piece_objects),
                                    get_all_object_coords(settings.black_piece_objects))

                                # test for check
                                settings.selected_piece.check_valid_moves_for_check(
                                    get_all_object_coords(settings.white_piece_objects),
                                    get_all_object_coords(settings.black_piece_objects), settings)

                                if settings.turn_step == 2:
                                    settings.turn_step = 3

                        elif settings.selected_piece is not None and click_coords not in \
                                settings.selected_piece.get_valid_moves() and \
                                board.resign_button.check_for_input(pygame.mouse.get_pos()) is False:
                            raise InvalidSelectionError("Invalid move")

                        elif settings.selected_piece is not None and click_coords in \
                                settings.selected_piece.get_valid_moves():

                            # add move to history
                            history.move_history[history.cur_session].append([
                                settings.compute_notation(settings.selected_piece.get_current_position()),  # old posit
                                settings.compute_notation(click_coords)  # new position
                            ])

                            # moves selected piece to position only if it is a valid move
                            settings.selected_piece.move_to_selected_position(click_coords)

                            # Pawn Promotion for top
                            pawn_promotion_for_black(click_coords, settings.selected_piece, settings.black_piece_objects)

                            if click_coords in white_object_coords:
                                white_piece = get_clicked_piece(click_coords, settings.white_piece_objects)
                                settings.captured_piece_objects_black.append(white_piece)

                                # sets white piece array to new array excluding the one that has been clicked
                                settings.white_piece_objects = [
                                    x for x in settings.white_piece_objects if x.get_current_position() != click_coords
                                ]

                            # check if white's king is in check and out of moves, thus making black the winner
                            settings.white_king.calculate_king_in_check(
                                settings.black_piece_objects, get_all_object_coords(settings.white_piece_objects),
                                get_all_object_coords(settings.black_piece_objects))

                            settings.white_king.calculate_valid_moves(
                                history, get_all_object_coords(settings.white_piece_objects),
                                get_all_object_coords(settings.black_piece_objects))
                            settings.white_king.check_valid_moves_for_check(
                                get_all_object_coords(settings.white_piece_objects),
                                get_all_object_coords(settings.black_piece_objects), settings)
                            if settings.white_king.get_is_in_check() and len(settings.white_king.get_valid_moves()) == 0:
                                settings.winner = 'Black'
                                settings.reset_game()
                                dump_move_history()
                                menu.winning_screen("Black")

                            settings.turn_step = 0  # turns back to other player now
                            # so resets the variable used for tracking the currently selected piece
                            settings.selected_piece = None

                    # checking if resign button has been clicked
                    if board.resign_button.check_for_input(pygame.mouse.get_pos()):
                        dump_move_history()
                        settings.reset_game()
                        history.reset_history(settings)
            except InvalidSelectionError as error:
                board.display_error_message(str(error))

            scaled_win = pygame.transform.smoothscale(settings.win, settings.screen_.get_size())
            settings.screen_.blit(scaled_win, (0, 0))

        pygame.display.flip()

        if settings.winner != '':
            settings.game_over = True

    dump_move_history()
    pygame.quit()
