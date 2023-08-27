class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, settings, internal_id=""):  # initialises properties
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.settings = settings
        self.internal_id = internal_id

    def update(self, screen):  # puts image and text on the screen
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):  # checks if we are clicking on it
        return position[0] in range(int(self.rect.left * self.settings.get_scale_factor_x()),
                                    int(self.rect.right * self.settings.get_scale_factor_x())) \
            and position[1] in range(int(self.rect.top * self.settings.get_scale_factor_y()),
                                     int(self.rect.bottom * self.settings.get_scale_factor_y()))

    def change_color(self, position):  # checks if were hovering over it ad if we are changes to desired colour
        if self.check_for_input(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


class ImageOnScreen:
    def __init__(self, image, pos):  # initialises its properties
        # self.image_size = size
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):  # puts image and text on the screen
        if self.image is not None:
            screen.blit(self.image, self.rect)

    def check_for_input(self, position):  # checks if we are clicking on it
        if position[0] in range(self.rect.left, self.rect.right) \
                and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
