import unittest
from unittest.mock import patch
import pygame
from models.settings import Settings


class TestSettingsClass(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()

    def test_initialization(self):
        # Test the initialization of the Settings class
        self.assertEqual(self.settings.WIDTH, 1000)
        self.assertEqual(self.settings.HEIGHT, 900)
        self.assertIsInstance(self.settings.screen_, pygame.Surface)
        self.assertIsInstance(self.settings.win, pygame.Surface)
        self.assertIsInstance(self.settings.timer, pygame.time.Clock)
        self.assertEqual(self.settings.fps, 60)
        self.assertIsInstance(self.settings.x_names, list)

        # Test initial game state attributes
        self.assertFalse(self.settings.game_over)
        self.assertEqual(self.settings.selected_piece, None)
        self.assertEqual(self.settings.winner, "")
        self.assertEqual(self.settings.history_being_shown, -1)

        # Test lists and objects
        self.assertIsInstance(self.settings.white_piece_objects, list)
        self.assertIsInstance(self.settings.black_piece_objects, list)
        self.assertIsInstance(self.settings.captured_piece_objects_white, list)
        self.assertIsInstance(self.settings.captured_piece_objects_black, list)

    def test_reset_game(self):
        # Test the reset_game method
        self.settings.reset_game()
        self.assertFalse(self.settings.game_over)
        self.assertEqual(self.settings.turn_step, 0)


if __name__ == '__main__':
    unittest.main()
