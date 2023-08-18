import pygame


class Pawn:
    def __init__(self, colour, current_position):
        # private variables with __
        self.__colour = colour
        self.__current_position = current_position
        self.__valid_moves = []
        image_url = f'assets/images/{colour[0]}_pawn.png'
        self.__image = self.load_and_scale(image_url, (65, 65))
        self.__small_image = self.load_and_scale(image_url, (45, 45))


    # todo: move to helper func or super class
    def load_and_scale(self, image_path, size):
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, size)

    def get_image(self):
        return self.__image

    def get_small_image(self):
        return self.__small_image

    def get_colour(self):
        return self.__colour

    def get_current_position(self):
        return self.__current_position

    def get_valid_moves(self):
        return self.__valid_moves

    def move_to_selected_position(self, new_position):
        if new_position in self.__valid_moves:
            self.__current_position = new_position
            self.__valid_moves = []

        return self.__current_position

    def calculate_valid_moves(self, white_locations, black_locations):
        moves_list = []  # moves list calculates the possible moves of each piece
        if self.__colour == 'white':
            no_blocking_white_piece = (self.__current_position[0], self.__current_position[1] + 1) not in white_locations
            no_blocking_black_piece = (self.__current_position[0], self.__current_position[1] + 1) not in black_locations
            is_not_bottom_of_board = self.__current_position[1] < 7

            # calculates one step forward move
            if no_blocking_white_piece and no_blocking_black_piece and is_not_bottom_of_board:
                moves_list.append((self.__current_position[0], self.__current_position[1] + 1))  # adds available tile to moves list []

            is_first_move = self.__current_position[1] == 1
            no_blocking_white_piece_for_two = (self.__current_position[0], self.__current_position[1] + 2) not in white_locations
            no_blocking_black_piece_for_two = (self.__current_position[0], self.__current_position[1] + 2) not in black_locations

            # calculates two steps forward first move
            if no_blocking_white_piece_for_two and no_blocking_black_piece_for_two and is_first_move:
                moves_list.append((self.__current_position[0], self.__current_position[1] + 2))

            # checks diagonal right for black piece
            diagonal_right_is_black = (self.__current_position[0] + 1, self.__current_position[1] + 1) in black_locations
            if diagonal_right_is_black:
                moves_list.append((self.__current_position[0] + 1, self.__current_position[1] + 1))

            # checks diagonal left for black piece
            diagonal_left_is_black = (self.__current_position[0] - 1, self.__current_position[1] + 1) in black_locations
            if diagonal_left_is_black:
                moves_list.append((self.__current_position[0] - 1, self.__current_position[1] + 1))

        else:
            no_blocking_white_piece = (self.__current_position[0], self.__current_position[1] - 1) not in white_locations
            no_blocking_black_piece = (self.__current_position[0], self.__current_position[1] - 1) not in black_locations
            is_not_top_of_board = self.__current_position[1] > 0

            # calculates one step forward
            if no_blocking_white_piece and no_blocking_black_piece and is_not_top_of_board:
                moves_list.append((self.__current_position[0], self.__current_position[1] - 1))

            is_first_move = self.__current_position[1] == 6
            no_blocking_white_piece_for_two = (self.__current_position[0], self.__current_position[1] - 2) not in white_locations
            no_blocking_black_piece_for_two = (self.__current_position[0], self.__current_position[1] - 2) not in black_locations

            # calculates two steps forward first move
            if no_blocking_white_piece_for_two and no_blocking_black_piece_for_two and is_first_move:
                moves_list.append((self.__current_position[0], self.__current_position[1] - 2))

            # checks diagonal right for white piece
            diagonal_right_is_white = (self.__current_position[0] + 1, self.__current_position[1] - 1) in white_locations
            if diagonal_right_is_white:
                moves_list.append((self.__current_position[0] + 1, self.__current_position[1] - 1))

            # checks diagonal left for white piece
            diagonal_left_is_white = (self.__current_position[0] - 1, self.__current_position[1] - 1) in white_locations
            if diagonal_left_is_white:
                moves_list.append((self.__current_position[0] - 1, self.__current_position[1] - 1))

        self.__valid_moves = moves_list
        return moves_list
