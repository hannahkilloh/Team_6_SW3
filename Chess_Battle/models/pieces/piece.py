import pygame
import os


class Piece:
    def __init__(self, colour, current_position, piece_type, small_size, normal_size):
        self._colour = colour
        self._current_position = current_position
        self._valid_moves = []
        # this gets the absolute path of the root 'Team_6_SW3' folder
        root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        image_url = f'{root_folder}/assets/images/{colour[0]}_{piece_type}.png'
        self._image = self.load_and_scale(image_url, normal_size)
        self._small_image = self.load_and_scale(image_url, small_size)

    def move_to_selected_position(self, new_position):
        if new_position in self._valid_moves:
            self._current_position = new_position
            self._valid_moves = []
        return self._current_position

    def calculate_valid_moves(self, white_locations, black_locations):
        pass  # This method will be overridden by subclasses

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
