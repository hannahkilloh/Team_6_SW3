import datetime


class History:
    def __init__(self, settings):
        self.settings = settings
        self.move_history = {}
        self.cur_session = ""
        self.reset_history(settings)

    def is_move_in_history(self, move):
        # convert the int x, y coords to chess notation before checking history dict
        move = self.settings.compute_notation(move)
        moves = self.move_history[self.cur_session]
        for m in moves:
            if m[0] == move:
                return True
        return False

    def reset_history(self, settings):
        self.move_history = settings.load_json("moves")
        self.cur_session = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        self.move_history[self.cur_session] = []
