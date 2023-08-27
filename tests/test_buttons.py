import unittest
from unittest.mock import Mock

import pygame

from models.buttons import Button, ImageOnScreen
from models.helpers import get_file_path_from_root


class TestButtonAndImage(unittest.TestCase):
    def setUp(self):
        self.settings = Mock()
        self.button_font = Mock()
        self.button_image = pygame.image.load(get_file_path_from_root("assets/images/blank_button_long.png"))
        self.image = pygame.image.load(get_file_path_from_root("assets/images/blank_button_long.png"))
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
        self.assertEqual(self.button.text, self.button_font.render.return_value)
        self.assertEqual(self.button.rect, self.button_image.get_rect(center=(self.button.x_pos, self.button.y_pos)))
        self.assertEqual(self.button.text_rect, self.button_font.render.return_value.get_rect.return_value)
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
        self.assertEqual(self.image_on_screen.rect, self.image.get_rect(center=(self.image_on_screen.x_pos, self.image_on_screen.y_pos)))

    def test_image_on_screen_check_for_input(self):
        position_inside_image = (210, 210)
        position_outside_image = (10, 25)

        self.assertTrue(self.image_on_screen.check_for_input(position_inside_image))
        self.assertFalse(self.image_on_screen.check_for_input(position_outside_image))


if __name__ == '__main__':
    unittest.main()
=======
import pygame
from models.buttons import Button
from models.settings import Settings


class TestButtonClass(unittest.TestCase):
    def setUp(self):
        # Initialize pygame for testing
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.Surface(
            (self.settings.WIDTH, self.settings.HEIGHT))
        self.font = pygame.font.Font('../assets/fonts/BalloonDropShadow.ttf', 36)  # Use a font for testing

    def test_button_initialization(self):
        image = pygame.Surface((100, 50))  # Mock image
        pos = (100, 100)
        text_input = "Test Button"
        base_color = pygame.Color("blue")
        hovering_color = pygame.Color("green")
        internal_id = "test_id"

        button = Button(
            image=image,
            pos=pos,
            text_input=text_input,
            font=self.font,
            base_color=base_color,
            hovering_color=hovering_color,
            settings=self.settings,
            internal_id=internal_id,
        )

        self.assertEqual(button.x_pos, pos[0])
        self.assertEqual(button.y_pos, pos[1])
        self.assertEqual(button.text_input, text_input)
        self.assertEqual(button.base_color, base_color)
        self.assertEqual(button.hovering_color, hovering_color)
        self.assertEqual(button.internal_id, internal_id)

    # def test_button_update(self):
    #     image = pygame.Surface((100, 50))  # Mock image
    #     pos = (100, 100)
    #     text_input = "Test Button"
    #     base_color = pygame.Color("blue")
    #     hovering_color = pygame.Color("green")
    #     internal_id = "test_id"
    #
    #     button = Button(
    #         image=image,
    #         pos=pos,
    #         text_input=text_input,
    #         font=self.font,
    #         base_color=base_color,
    #         hovering_color=hovering_color,
    #         settings=self.settings,
    #         internal_id=internal_id,
    #     )
    #     # Create a new surface for testing
    #     test_screen = pygame.Surface((self.settings.WIDTH, self.settings.HEIGHT))
    #
    #     button.update(test_screen)
    #     test_screen.blit.assert_called_with(image, button.rect)
    #     test_screen.blit.assert_called_with(self.font.render,
    #                                    self.font.render)
    # def test_button_update(self):
    #     image = pygame.Surface((100, 50))  # Mock image
    #     pos = (0, 0)
    #     text_input = "Test Button"
    #     base_color = pygame.Color("blue")
    #     hovering_color = pygame.Color("green")
    #
    #     button = Button(
    #         image=image,
    #         pos=pos,
    #         text_input=text_input,
    #         font=self.font,
    #         base_color=base_color,
    #         hovering_color=hovering_color,
    #         settings=self.settings,
    #     )
    #
    #     # Create a new surface for testing
    #     test_screen = pygame.Surface((self.settings.WIDTH, self.settings.HEIGHT))
    #
    #     # Update the button on the test screen
    #     button.update(test_screen)
    #
    #     # Get the pixel colors at the button's position
    #     button_pixel_color = test_screen.get_at(pos)
    #     text_pixel_color = test_screen.get_at((pos[0], pos[1] + button.text.get_height()))
    #
    #     # Check if the pixel colors match the expected colors (button image and text)
    #     self.assertEqual(button_pixel_color, base_color)  # Check button image color
    #     self.assertEqual(text_pixel_color, base_color)  # Check text color

    # def test_button_check_for_input(self):
    #     image = pygame.Surface((100, 50))  # Mock image
    #     pos = (100, 100)
    #     text_input = "Test Button"
    #     base_color = pygame.Color("blue")
    #     hovering_color = pygame.Color("green")
    #
    #     button = Button(
    #         image=image,
    #         pos=pos,
    #         text_input=text_input,
    #         font=self.font,
    #         base_color=base_color,
    #         hovering_color=hovering_color,
    #         settings=self.settings,
    #     )
    #
    #     # Test a position within the button's rect
    #     position_within_button = (110, 110)
    #     self.assertTrue(button.check_for_input(position_within_button))
    #
    #     # Test a position outside the button's rect
    #     position_outside_button = (50, 50)
    #     self.assertFalse(button.check_for_input(position_outside_button))
    #
    # def test_button_change_color(self):
    #     image = pygame.Surface((100, 50))  # Mock image
    #     pos = (100, 100)
    #     text_input = "Test Button"
    #     base_color = pygame.Color("blue")
    #     hovering_color = pygame.Color("green")
    #
    #     button = Button(
    #         image=image,
    #         pos=pos,
    #         text_input=text_input,
    #         font=self.font,
    #         base_color=base_color,
    #         hovering_color=hovering_color,
    #         settings=self.settings,
    #     )
    #
    #     # Test when hovering over the button
    #     position_hovering = (110, 110)
    #     button.change_color(position_hovering)
    #     self.assertEqual(button.text, button.font.render(
    #         text_input, True, hovering_color))
    #
    #     # Test when not hovering over the button
    #     position_not_hovering = (50, 50)
    #     button.change_color(position_not_hovering)
    #     self.assertEqual(button.text, button.font.render(
    #         text_input, True, base_color))


if __name__ == '__main__':
    unittest.main()
