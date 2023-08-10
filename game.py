import pygame
from models.settings import Settings
from models.board import Board, BoardSettings
from models.images import Images

pygame.init()
pygame.font.init()
pygame.display.set_caption('🐍🐍 Welcome to the Pythonic Chess 🐍🐍')

# can pass in any colours, to set theme up easier

board_settings = BoardSettings("light grey", "dark grey", "pink", "black", 'freesansbold.ttf')
settings = Settings()
images = Images()
board = Board(board_settings, settings, images)

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
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
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
    moves_list = []
    if color == 'white':
        enemies_list = settings.black_locations
        friends_list = settings.white_locations
    else:
        friends_list = settings.black_locations
        enemies_list = settings.white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check rook
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = settings.black_locations
        friends_list = settings.white_locations
    else:
        friends_list = settings.black_locations
        enemies_list = settings.white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in settings.white_locations and \
                         (position[0], position[1] + 1) not in settings.black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in settings.white_locations and (position[0], position[1] + 2) \
                not in settings.black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in settings.black_locations:
            moves_list.append((position[0], position[1] + 1))
        if (position[0] - 1, position[1] + 1) in settings.black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in settings.white_locations and \
                         (position[0], position[1] - 1) not in settings.black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in settings.white_locations and (position[0], position[1] + 2) \
                not in settings.black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in settings.white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in settings.white_locations:
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
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list



def draw_captured():
    for i in range(len(settings.captured_pieces_white)):
        captured_piece = settings.captured_pieces_white[i]
        index = settings.piece_list.index(captured_piece)
        settings.screen.blit(images.small_black_images[index], (825, 5 + 50*i))
    for i in range(len(settings.captured_pieces_black)):
        captured_piece = settings.captured_pieces_black[i]
        index = settings.piece_list.index(captured_piece)
        settings.screen.blit(images.small_white_images[index], (925, 5 + 50*i))


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
        pygame.draw.circle(settings.screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)



black_options = check_options(settings.black_pieces, settings.black_locations, 'black')
white_options = check_options(settings.white_pieces, settings.white_locations, 'white')
# Main game loop
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
            x_coord = event.pos[0] // 100  # x coord
            y_coord = event.pos[1] // 100  # y coord
            click_coords = (x_coord, y_coord)
            if settings.turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    settings.winner = 'black'
                if click_coords in settings.white_locations:
                    settings.selection = settings.white_locations.index(click_coords)  # piece location we want the index of that piece
                    if settings.turn_step == 0:
                        settings.turn_step = 1
                if click_coords in settings.valid_moves and settings.selection != 100:  # don't want to be able to click somewhere and
                    # move without a piece selected
                    settings.white_locations[settings.selection] = click_coords  # the piece is allowed to go to where is selected
                    if click_coords in settings.black_locations:  # checking it takes us to where a black piece is sitting
                        black_piece = settings.black_locations.index(click_coords)
                        settings.captured_pieces_white.append(settings.black_pieces[black_piece])
                        if settings.black_pieces[black_piece] == 'king':
                            settings.winner = 'white'
                        settings.black_pieces.pop(black_piece)
                        settings.black_locations.pop(black_piece)
                    black_options = check_options(settings.black_pieces, settings.black_locations, 'black')
                    white_options = check_options(settings.white_pieces, settings.white_locations, 'white')
                    settings.turn_step = 2
                    settings.selection = 100
                    settings.valid_moves = []
            if settings.turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    settings.winner = 'white'
                if click_coords in settings.black_locations:
                    settings.selection = settings.black_locations.index(click_coords)  # piece location we want the index of that piece
                    if settings.turn_step == 2:
                        settings.turn_step = 3
                if click_coords in settings.valid_moves and settings.selection != 100:  # don't want to be able to click somewhere and
                    # move without a piece selected
                    settings.black_locations[settings.selection] = click_coords  # the piece is allowed to go to where is selected
                    if click_coords in settings.white_locations:  # checking it takes us to where a black piece is sitting
                        white_piece = settings.white_locations.index(click_coords)
                        settings.captured_pieces_black.append(settings.white_pieces[white_piece])
                        if settings.black_pieces[white_piece] == 'king':
                            settings.winner = 'black'
                        settings.white_pieces.pop(white_piece)
                        settings.white_locations.pop(white_piece)
                    black_options = check_options(settings.black_pieces, settings.black_locations, 'black')
                    white_options = check_options(settings.white_pieces, settings.white_locations, 'white')
                    settings.turn_step = 0
                    settings.selection = 100
                    settings.valid_moves = []

    pygame.display.flip()
pygame.quit()
