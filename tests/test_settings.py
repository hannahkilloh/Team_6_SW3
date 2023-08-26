import unittest
from unittest.mock import patch
import pygame
from models.settings import Settings

# Mock classes for testing
class MockPiece:
    def get_short_notation(self):
        return 'MockShortNotation'

class MockScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_size(self):
        return (self.width, self.height)

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

    def test_compute_notation(self):
        # Mock the selected_piece for this test
        self.settings.selected_piece = MockPiece()

        coords = (1, 2)
        notation = self.settings.compute_notation(coords)

        expected_notation = 'MockShortNotationg3'
        self.assertEqual(notation, expected_notation)

    def test_get_scale_factor_x(self):
        # Mock the screen_ object for this test
        self.settings.screen_ = MockScreen(2000, 1000)

        scale_factor_x = self.settings.get_scale_factor_x()
        expected_scale_factor_x = 2.0  # Expected scale factor
        self.assertEqual(scale_factor_x, expected_scale_factor_x)

    def test_load_json(self):
        # Mock the file system access for this test
        with patch('models.settings.os.path.exists') as mock_os_exists, \
                patch('models.settings.open') as mock_open:
            mock_os_exists.return_value = True
            mock_open.return_value.__enter__.return_value.read.return_value = '{"key": "value"}'

            data = self.settings.load_json('test_file')
            expected_data = {"key": "value"}  # Replace with the expected data
            self.assertEqual(data, expected_data)


if __name__ == '__main__':
    unittest.main()
