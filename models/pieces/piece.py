class Piece:
    def __init__(self, colour, current_position):
        self.__colour = colour
        self.__current_position = current_position
        self.__valid_moves = []

    def move_to_selected_position(self, new_position):
        if new_position in self.__valid_moves:
            self.__current_position = new_position
        return self.__current_position

    def get_valid_moves(self, white_locations, black_locations):
        pass  # This method will be overridden by subclasses

