import pygame
from models.settings import Settings
from models.board import Board, BoardSettings

pygame.init()
pygame.font.init()
pygame.display.set_icon(pygame.image.load('assets/images/chess_icon.ico'))

# can pass in any colours, to set theme up easier
board_settings = BoardSettings(
    '#0000D2', '#7BFCFC', 'white', '#0000D2', 'assets/fonts/JetBrainsMono-Regular.ttf')
settings = Settings()
board = Board(board_settings, settings)


# Todo: use this in rook and bishop
# Define a function to determine friends and enemies based on color
# def get_friends_and_enemies(color):
#     if color == 'white':
#         return settings.white_locations, settings.black_locations
#     else:
#         return settings.black_locations, settings.white_locations

def draw_captured_objects():
    for index in range(len(settings.captured_piece_objects_white)):
        settings.screen.blit(settings.captured_piece_objects_white[index].get_small_image(), (825, 5 + 50 * index))
    for index in range(len(settings.captured_piece_objects_black)):
        settings.screen.blit(settings.captured_piece_objects_black[index].get_small_image(), (925, 5 + 50 * index))


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


# Main game loop
def play_game():
    run = True
    while run:
        board.initialise()
        draw_captured_objects()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not settings.game_over:
                x_coord = event.pos[0] // 100  # x coord
                y_coord = event.pos[1] // 100  # y coord
                click_coords = (x_coord, y_coord)

                # if the step is 0 or 1 then it is the whites turn
                if settings.turn_step <= 1:
                    # this is when they click 'Resign'
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        settings.winner = 'black'

                    # maps through white_piece_objects array of objects and passes each object into the
                    # get_object_co-ords function and returns the co-ords as an array
                    white_object_coords = list(map(get_object_coords, settings.white_piece_objects))
                    black_object_coords = list(map(get_object_coords, settings.black_piece_objects))

                    if click_coords in white_object_coords:  # if white piece has been clicked
                        settings.selected_piece = get_clicked_white(click_coords)
                        settings.selected_piece.calculate_valid_moves(get_white_object_coords(),
                                                                      get_black_object_coords())

                        if settings.turn_step == 0:  # if steps is 0 it moves onto the next step(1)
                            settings.turn_step = 1
                    elif settings.selected_piece is not None and click_coords in \
                            settings.selected_piece.get_valid_moves():
                        # moves selected piece to position only if it is a valid move
                        settings.selected_piece.move_to_selected_position(click_coords)

                        if click_coords in black_object_coords:
                            black_piece = get_clicked_black(click_coords)
                            settings.captured_piece_objects_white.append(black_piece)
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
                    # this is when they click 'Resign'
                    if click_coords == (8, 8) or click_coords == (9, 8):
                        settings.winner = 'white'

                    # maps through white_piece_objects array of objects and passes each object into the
                    # get_object_co-ords function and returns the co-ords as an array
                    white_object_coords = list(map(get_object_coords, settings.white_piece_objects))
                    black_object_coords = list(map(get_object_coords, settings.black_piece_objects))

                    if click_coords in black_object_coords:  # if black piece has been clicked
                        settings.selected_piece = get_clicked_black(click_coords)
                        settings.selected_piece.calculate_valid_moves(get_white_object_coords(),
                                                                      get_black_object_coords())

                        if settings.turn_step == 2:  # if step is 2 it moves onto the next step(3) of black player
                            settings.turn_step = 3
                    elif settings.selected_piece is not None and click_coords in \
                            settings.selected_piece.get_valid_moves():
                        settings.selected_piece.move_to_selected_position(click_coords)
                        if click_coords in white_object_coords:
                            white_piece = get_clicked_white(click_coords)
                            settings.captured_piece_objects_black.append(white_piece)
                            # sets white piece array to new array excluding the one that has been clicked
                            settings.white_piece_objects = [
                                x for x in settings.white_piece_objects if x.get_current_position() != click_coords
                            ]

                        settings.turn_step = 0  # turns back to other player now
                        # so resets the variable used for tracking the currently selected piece
                        settings.selected_piece = None

        pygame.display.flip()
    pygame.quit()
