import pygame
from models.helpers import Board


def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press enter to restart', True, 'white'), (210, 240))



# game loop
# black_options = check_options(black_pieces, black_locations, 'black')
# # white_options = check_options(white_pieces, white_locations, 'white')
# run = True
# while run:
#     timer.tick(fps)
#     screen.fill('dark gray')
#     draw_board()
#     draw_pieces()
    # draw_captured()
    # if selection != 100:
    #     valid_moves = check_valid_moves()
    #     draw_valid(valid_moves)

# event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
#             x_coord = event.pos[0] // 100  # x coord
#             y_coord = event.pos[1] // 100  # y coord
#             click_coords = (x_coord, y_coord)
#             if turn_step <= 1:
#                 if click_coords == (8, 8) or click_coords == (9, 8):
#                     winner = 'black'
#                 if click_coords in white_locations:
#                     selection = white_locations.index(click_coords)  # piece location we want the index of that piece
#                     if turn_step == 0:
#                         turn_step = 1
#                 if click_coords in valid_moves and selection != 100:  # don't want to be able to click somewhere and
#                     # move without a piece selected
#                     white_locations[selection] = click_coords  # the piece is allowed to go to where is selected
#                     if click_coords in black_locations:  # checking it takes us to where a black piece is sitting
#                         black_piece = black_locations.index(click_coords)
#                         captured_pieces_white.append(black_pieces[black_piece])
#                         if black_pieces[black_piece] == 'king':
#                             winner = 'white'
#                         black_pieces.pop(black_piece)
#                         black_locations.pop(black_piece)
#                     black_options = check_options(black_pieces, black_locations, 'black')
#                     white_options = check_options(white_pieces, white_locations, 'white')
#                     turn_step = 2
#                     selection = 100
#                     valid_moves = []
#             if turn_step > 1:
#                 if click_coords == (8, 8) or click_coords == (9, 8):
#                     winner = 'white'
#                 if click_coords in black_locations:
#                     selection = black_locations.index(click_coords)  # piece location we want the index of that piece
#                     if turn_step == 2:
#                         turn_step = 3
#                 if click_coords in valid_moves and selection != 100:  # don't want to be able to click somewhere and
#                     # move without a piece selected
#                     black_locations[selection] = click_coords  # the piece is allowed to go to where is selected
#                     if click_coords in white_locations:  # checking it takes us to where a black piece is sitting
#                         white_piece = white_locations.index(click_coords)
#                         captured_pieces_black.append(white_pieces[white_piece])
#                         if black_pieces[white_piece] == 'king':
#                             winner = 'black'
#                         white_pieces.pop(white_piece)
#                         white_locations.pop(white_piece)
#                     black_options = check_options(black_pieces, black_locations, 'black')
#                     white_options = check_options(white_pieces, white_locations, 'white')
#                     turn_step = 0
#                     selection = 100
#                     valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100  # variable for what index piece is currently selected
                valid_moves = []  # list to check valid moves
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')


    if winner != '':
        game_over = True
        draw_game_over()