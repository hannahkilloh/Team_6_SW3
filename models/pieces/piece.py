import pygame
import os

class Piece:
    def __init__(self, colour, current_position, piece_type, small_size, normal_size):
        self._colour = colour
        self.piece_type = piece_type
        self._current_position = current_position
        self._valid_moves = []
        # this gets the absolute path of the root 'Team_6_SW3_PROJECT' folder
        root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        image_url = f'{root_folder}/assets/images/{colour[0]}_{piece_type}.png'
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

    def calculate_valid_moves(self, move_history, white_locations, black_locations, settings):
        pass  # This method will be overridden by subclasses

    def check_valid_moves_for_check(self, valid_moves, white_locations, black_locations, settings):
        white_locations_copy = white_locations.copy()
        black_locations_copy = black_locations.copy()
        for m in valid_moves:
            # get locations of current team pieces
            if self._colour == "white":
                locations = white_locations_copy
            else:
                locations = black_locations_copy

            # get the king of the same team
            if self._colour == "white":
                king = settings.white_king
                enemy_list = settings.black_piece_objects.copy()
            else:
                king = settings.black_king
                enemy_list = settings.white_piece_objects.copy()

            if m in locations:
                locations.remove(m)
            for e in enemy_list:
                if e._current_position == m:
                    enemy_list.remove(e)

            # set the current position of that list to the current move we are testing
            for i in range(len(locations)):
                if self._current_position == locations[i]:
                    locations[i] = m

            # check if this position would result in a check
            is_king_in_check_for_cur_move = king.calculate_king_in_check(enemy_list, white_locations_copy, black_locations_copy, settings)
            if not is_king_in_check_for_cur_move:
                self._valid_moves.append(m)
            print(self._valid_moves)

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
