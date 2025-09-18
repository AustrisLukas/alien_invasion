class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        self.fleet_rows = self.settings.starting_fleet_rows
        self.game_level = 1

    def advance_level(self):
        self.fleet_drop_speed += 1
        self.fleet_rows += 1