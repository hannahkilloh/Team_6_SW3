import pygame
from models.helpers import get_file_path_from_root

class Piece:
    def __init__(self, colour, current_position, piece_type, small_size, normal_size):
        self._colour = colour
        self._piece_type = piece_type
        self._current_position = current_position
        self._valid_moves = []
        image_url = get_file_path_from_root(f'assets/images/{colour[0]}_{piece_type}.png')
        self._image = self.load_and_scale(image_url, normal_size)
        self._small_image = self.load_and_scale(image_url, small_size)

    def move_to_selected_position(self, new_position):
        if new_position in self._valid_moves:
            self._current_position = new_position
            self._valid_moves = []
        return self._current_position

    def force_move_to_selected_position(self, new_position):
        # move to position even if not in valid moves
        self._current_position = new_position
        self._valid_moves = []
        return self._current_position

    def calculate_valid_moves(self, move_history, white_locations, black_locations, update_protected_property=True):
        pass  # This method will be overridden by subclasses

    def check_valid_moves_for_check(self, white_locations, black_locations, settings):
        new_moves = []
        for valid_move in self._valid_moves:
            if self._colour == "white":
                locations = white_locations.copy()
                enemy_list = settings.black_piece_objects.copy()
                king = settings.white_king
            else:
                locations = black_locations.copy()
                enemy_list = settings.white_piece_objects.copy()
                king = settings.black_king

            # set the current position of that list to the current move we are testing
            for i in range(len(locations)):
                if self._current_position == locations[i]:
                    locations[i] = valid_move

            # if new position is occupied by enemy piece, remove it (simulates taking)
            for enemy in enemy_list:
                if enemy.get_current_position() == valid_move:
                    enemy_list.remove(enemy)

            if self._piece_type == "king":
                pos_override = valid_move
            else:
                pos_override = None

            # setup locations arrays for passing to calculate_king_in_check depending on current player colour
            if self._colour == "white":
                white_locations_copy = locations
                black_locations_copy = black_locations.copy()
            else:
                white_locations_copy = white_locations.copy()
                black_locations_copy = locations

            # check if this position would result in a check
            is_king_in_check_for_cur_move = king.calculate_king_in_check(enemy_list, white_locations_copy, black_locations_copy, pos_override=pos_override)
            if not is_king_in_check_for_cur_move:
                new_moves.append(valid_move)

        self._valid_moves = new_moves

        return new_moves

    def get_short_notation(self):
        pass  # This method will be overridden by subclasses

    def load_and_scale(self, image_path, size):
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, size)

    def get_image(self):
        return self._image

    def get_small_image(self):
        return self._small_image

    def get_colour(self):
        return self._colour

    def get_current_position(self):
        return self._current_position

    def get_valid_moves(self):
        return self._valid_moves

    def get_piece_type(self):
        return self._piece_type
