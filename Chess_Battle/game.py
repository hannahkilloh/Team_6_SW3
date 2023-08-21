import sys

import pygame
from models.settings import Settings
from models.board import Board, BoardSettings
from models.pieces.rook import Rook
from models.pieces.bishop import Bishop
from models.images import Images

pygame.init()
# surface = pygame.display.set_mode((900, 900), pygame.RESIZABLE)
pygame.font.init()
# pygame.display.set_caption('🐍🐍 Welcome to the Pythonic Chess 🐍🐍')
pygame.display.set_icon(pygame.image.load('assets/images/chess_icon.ico'))


# can pass in any colours, to set theme up easier
board_settings = BoardSettings(
    '#0000D2', '#7BFCFC', 'white', '#0000D2', 'assets/fonts/JetBrainsMono-Regular.ttf')
settings = Settings()
images = Images()
board = Board(board_settings, settings, images)


# Define a function to determine friends and enemies based on color
def get_friends_and_enemies(color):
    if color == 'white':
        return settings.white_locations, settings.black_locations
    else:
        return settings.black_locations, settings.white_locations


# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []  # gets every poss move for every piece
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        friends_list = settings.white_locations
    else:
        friends_list = settings.black_locations
    # 8 squares to check for kings moves, they can go one square in any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)

    return moves_list


# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


# check bishop moves

def check_bishop(position, color):
    bishop = Bishop(colour=color, current_position=position)
    # Use the get_friends_and_enemies function to set friends_list and enemies_list
    friends_list, enemies_list = get_friends_and_enemies(color)

    valid_moves = bishop.get_valid_moves(friends_list, enemies_list)
    return valid_moves


# check rook
def check_rook(position, color):
    rook = Rook(colour=color, current_position=position)

    # Use the get_friends_and_enemies function to set friends_list and enemies_list
    friends_list, enemies_list = get_friends_and_enemies(color)

    valid_moves = rook.get_valid_moves(friends_list, enemies_list)
    return valid_moves

# check valid pawn moves


def check_pawn(position, color):
    moves_list = []  # moves list calculates the possible moves of each piece
    if color == 'white':
        no_blocking_white_piece = (
            position[0], position[1] + 1) not in settings.white_locations
        no_blocking_black_piece = (
            position[0], position[1] + 1) not in settings.black_locations
        is_not_bottom_of_board = position[1] < 7

        # calculates one step forward move
        if no_blocking_white_piece and no_blocking_black_piece and is_not_bottom_of_board:
            # adds available tile to moves list []
            moves_list.append((position[0], position[1] + 1))

        is_first_move = position[1] == 1
        no_blocking_white_piece_for_two = (
            position[0], position[1] + 2) not in settings.white_locations
        no_blocking_black_piece_for_two = (
            position[0], position[1] + 2) not in settings.black_locations

        # calculates two steps forward first move
        if no_blocking_white_piece_for_two and no_blocking_black_piece_for_two and is_first_move:
            moves_list.append((position[0], position[1] + 2))

        # checks diagonal right for black piece
        diagonal_right_is_black = (
            position[0] + 1, position[1] + 1) in settings.black_locations
        if diagonal_right_is_black:
            moves_list.append((position[0] + 1, position[1] + 1))

        # checks diagonal left for black piece
        diagonal_left_is_black = (
            position[0] - 1, position[1] + 1) in settings.black_locations
        if diagonal_left_is_black:
            moves_list.append((position[0] - 1, position[1] + 1))

    else:
        no_blocking_white_piece = (
            position[0], position[1] - 1) not in settings.white_locations
        no_blocking_black_piece = (
            position[0], position[1] - 1) not in settings.black_locations
        is_not_top_of_board = position[1] > 0

        # calculates one step forward
        if no_blocking_white_piece and no_blocking_black_piece and is_not_top_of_board:
            moves_list.append((position[0], position[1] - 1))

        is_first_move = position[1] == 6
        no_blocking_white_piece_for_two = (
            position[0], position[1] - 2) not in settings.white_locations
        no_blocking_black_piece_for_two = (
            position[0], position[1] - 2) not in settings.black_locations

        # calculates two steps forward first move
        if no_blocking_white_piece_for_two and no_blocking_black_piece_for_two and is_first_move:
            moves_list.append((position[0], position[1] - 2))

        # checks diagonal right for white piece
        diagonal_right_is_white = (
            position[0] + 1, position[1] - 1) in settings.white_locations
        if diagonal_right_is_white:
            moves_list.append((position[0] + 1, position[1] - 1))

        # checks diagonal left for white piece
        diagonal_left_is_white = (
            position[0] - 1, position[1] - 1) in settings.white_locations
        if diagonal_left_is_white:
            moves_list.append((position[0] - 1, position[1] - 1))

    return moves_list


# check knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        friends_list = settings.white_locations
    else:
        friends_list = settings.black_locations
    # 8 squares to check for knights moves, they can go two squares in one direction and one in another direction
    targets = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


def draw_captured():
    for i in range(len(settings.captured_pieces_white)):
        captured_piece = settings.captured_pieces_white[i]
        index = settings.piece_list.index(captured_piece)
        settings.win.blit(
            images.small_black_images[index], (825, 155 + 50 * i))
    for i in range(len(settings.captured_pieces_black)):
        captured_piece = settings.captured_pieces_black[i]
        index = settings.piece_list.index(captured_piece)
        settings.win.blit(
            images.small_white_images[index], (925, 155 + 50 * i))


def check_valid_moves():
    if settings.turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[settings.selection]
    return valid_options


def draw_valid(moves):
    if settings.turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(settings.win, color,
                           (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


black_options = check_options(
    settings.black_pieces, settings.black_locations, 'black')
white_options = check_options(
    settings.white_pieces, settings.white_locations, 'white')


# Main game loop
def play_game():
    global black_options
    global white_options

    run = True
    while run:
        board.initialise()
        draw_captured()

        if settings.selection != 100:
            settings.valid_moves = check_valid_moves()
            draw_valid(settings.valid_moves)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not settings.game_over:
                x_coord = (event.pos[0] / settings.get_scale_factor_x()) // 100  # x coord
                y_coord = (event.pos[1] / settings.get_scale_factor_y()) // 100  # y coord
                click_coords = (x_coord, y_coord)
                if settings.turn_step <= 1:
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        settings.winner = 'black'
                    if click_coords in settings.white_locations:
                        # piece location we want the index of that piece
                        settings.selection = settings.white_locations.index(
                            click_coords)
                        if settings.turn_step == 0:
                            settings.turn_step = 1
                            # don't want to be able to click somewhere and move without a piece selected
                    if click_coords in settings.valid_moves and settings.selection != 100:
                        # the piece is allowed to go to where is selected
                        settings.white_locations[settings.selection] = click_coords

                        # add move to history
                        board.moves[1].append(settings.compute_notation("white", click_coords))

                        # checking it takes us to where a black piece is sitting
                        if click_coords in settings.black_locations:
                            black_piece = settings.black_locations.index(
                                click_coords)
                            settings.captured_pieces_white.append(
                                settings.black_pieces[black_piece])
                            if settings.black_pieces[black_piece] == 'king':
                                settings.winner = 'white'
                            settings.black_pieces.pop(black_piece)
                            settings.black_locations.pop(black_piece)
                        black_options = check_options(
                            settings.black_pieces, settings.black_locations, 'black')
                        white_options = check_options(
                            settings.white_pieces, settings.white_locations, 'white')
                        settings.turn_step = 2
                        settings.selection = 100
                        settings.valid_moves = []
                if settings.turn_step > 1:
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        settings.winner = 'white'
                    if click_coords in settings.black_locations:
                        # piece location we want the index of that piece
                        settings.selection = settings.black_locations.index(
                            click_coords)
                        if settings.turn_step == 2:
                            settings.turn_step = 3
                            # don't want to be able to click somewhere and move without a piece selected
                    if click_coords in settings.valid_moves and settings.selection != 100:
                        # the piece is allowed to go to where is selected
                        settings.black_locations[settings.selection] = click_coords

                        # add move to history
                        board.moves[0].append(settings.compute_notation("black", click_coords))

                        # checking it takes us to where a black piece is sitting
                        if click_coords in settings.white_locations:
                            white_piece = settings.white_locations.index(
                                click_coords)
                            settings.captured_pieces_black.append(
                                settings.white_pieces[white_piece])
                            if settings.black_pieces[white_piece] == 'king':
                                settings.winner = 'black'
                            settings.white_pieces.pop(white_piece)
                            settings.white_locations.pop(white_piece)
                        black_options = check_options(
                            settings.black_pieces, settings.black_locations, 'black')
                        white_options = check_options(
                            settings.white_pieces, settings.white_locations, 'white')
                        settings.turn_step = 0
                        settings.selection = 100
                        settings.valid_moves = []
                # checking if resign button has been clicked
                if board.resign_button.check_for_input(pygame.mouse.get_pos()):
                    settings.write_json("moves", board.moves)
                    pygame.quit()
                    sys.exit()

        scaled_win = pygame.transform.smoothscale(settings.win, settings.screen_.get_size())
        settings.screen_.blit(scaled_win, (0, 0))
        pygame.display.flip()
    pygame.quit()
