"""Repository wrapper around the database implementation."""

from database.db import Database


class GameRepository:
    """Persistence boundary for chess matches."""

    def __init__(self):
        self._db = Database()

    def create_game(self, user_id, difficulty):
        return self._db.create_game(user_id, difficulty)

    def end_game(self, game_id, result, pgn, move_count):
        self._db.end_game(game_id, result, pgn, move_count)

    def close(self):
        self._db.close()
