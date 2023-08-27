import unittest
from unittest.mock import Mock
from models.history import History


class TestHistory(unittest.TestCase):

    def setUp(self):
        self.settings_mock = Mock()
        self.settings_mock.compute_notation.side_effect = lambda x: f"move_{x}"
        self.settings_mock.load_json.return_value = {}

    # Tests if 'is_move_in_history' method correctly identifies move in the history
    def test_is_move_in_history_with_existing_move(self):
        history = History(self.settings_mock)
        history.move_history = {"session1": [("move_123", "data1"), ("move_456", "data2")]}
        history.cur_session = "session1"
        result = history.is_move_in_history(123)
        self.assertTrue(result)

    # tests if the 'is_move_in_history' methods identifies a non-existent move in the history
    def test_is_move_in_history_with_non_existing_move(self):
        history = History(self.settings_mock)
        history.move_history = {"session1": [("move_123", "data1"), ("move_456", "data2")]}
        history.cur_session = "session1"
        result = history.is_move_in_history(789)
        self.assertFalse(result)

    # Tests to see if 'reset_history' updates the move history and current session correctly
    def test_reset_history(self):
        history = History(self.settings_mock)
        history.reset_history(self.settings_mock)
        self.assertEqual(history.move_history[history.cur_session], [])


if __name__ == '__main__':
    unittest.main()
