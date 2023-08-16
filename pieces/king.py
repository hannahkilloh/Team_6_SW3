class King:
    def __init__(self, colour, current_position, image):
        self.__colour = colour  # private variables with __
        self.__current_position = current_position
        self.__valid_moves = []
        self.__image = image

    def get_image(self):
        return self.__image

    def get_current_position(self):
        return self.__current_position

    def get_valid_moves(self):
        return self.__valid_moves

    def move_to_selected_position(self, new_position):
        if new_position in self.__valid_moves:
            self.__current_position = new_position

        return self.__current_position

    def calculate_valid_moves(self, white_locations, black_locations):
        moves_list = []
        if self.__colour == 'white':
            friends_list = white_locations
        else:
            friends_list = black_locations
        # 8 squares to check for kings moves, they can go one square in any direction
        targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
        for i in range(8):
            target = (self.__current_position[0] + targets[i][0], self.__current_position[1] + targets[i][1])
            if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                moves_list.append(target)

        self.__valid_moves = moves_list
        return moves_list