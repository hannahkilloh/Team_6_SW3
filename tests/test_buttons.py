import unittest
from unittest.mock import Mock

import pygame

from models.buttons import Button, ImageOnScreen
from models.helpers import get_file_path_from_root


class TestButtonAndImage(unittest.TestCase):
    def setUp(self):
        self.settings = Mock()
        self.button_font = Mock()
        self.button_image = pygame.image.load(
            get_file_path_from_root("assets/images/blank_button_long.png"))
        self.image = pygame.image.load(get_file_path_from_root(
            "assets/images/blank_button_long.png"))
        self.button = Button(
            image=self.button_image,
            pos=(100, 100),
            text_input="Click Me",
            font=self.button_font,
            base_color="blue",
            hovering_color='#7BFCFC',
            settings=self.settings
        )
        self.image_on_screen = ImageOnScreen(
            image=self.image,
            pos=(200, 200)
        )

    def test_button_initialization(self):
        self.assertEqual(self.button.image, self.button_image)
        self.assertEqual(self.button.x_pos, 100)
        self.assertEqual(self.button.y_pos, 100)
        self.assertEqual(self.button.font, self.button_font)
        self.assertEqual(self.button.base_color, "blue")
        self.assertEqual(self.button.hovering_color, '#7BFCFC')
        self.assertEqual(self.button.text_input, "Click Me")
        self.assertEqual(self.button.text,
                         self.button_font.render.return_value)
        self.assertEqual(self.button.rect, self.button_image.get_rect(
            center=(self.button.x_pos, self.button.y_pos)))
        self.assertEqual(self.button.text_rect,
                         self.button_font.render.return_value.get_rect.return_value)
        self.assertEqual(self.button.settings, self.settings)

    def test_button_check_for_input(self):
        self.settings.get_scale_factor_x.return_value = 1.0
        self.settings.get_scale_factor_y.return_value = 1.0

        position_inside_button = (120, 120)
        position_outside_button = (10, 25)

        self.assertTrue(self.button.check_for_input(position_inside_button))
        self.assertFalse(self.button.check_for_input(position_outside_button))

    def test_button_change_color(self):
        self.settings.get_scale_factor_x.return_value = 1.0
        self.settings.get_scale_factor_y.return_value = 1.0

        position_hovering = (120, 120)
        position_not_hovering = (90, 90)

        self.button.change_color(position_hovering)
        self.button_font.render.assert_called_with("Click Me", True, '#7BFCFC')

        self.button_font.render.reset_mock()

        self.button.change_color(position_not_hovering)
        self.button_font.render.assert_called_with("Click Me", True, '#7BFCFC')

    def test_image_on_screen_initialization(self):
        self.assertEqual(self.image_on_screen.image, self.image)
        self.assertEqual(self.image_on_screen.x_pos, 200)
        self.assertEqual(self.image_on_screen.y_pos, 200)
        self.assertEqual(self.image_on_screen.rect, self.image.get_rect(
            center=(self.image_on_screen.x_pos, self.image_on_screen.y_pos)))

    def test_image_on_screen_check_for_input(self):
        position_inside_image = (210, 210)
        position_outside_image = (10, 25)

        self.assertTrue(self.image_on_screen.check_for_input(
            position_inside_image))
        self.assertFalse(self.image_on_screen.check_for_input(
            position_outside_image))


if __name__ == '__main__':
    unittest.main()
