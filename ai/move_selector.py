"""Move-selection service for AI opponents."""

import SmartMoveFinder


def choose_move(game_state, valid_moves, difficulty):
    """Return the best available move for the current position."""
    move, _ = SmartMoveFinder.findBestMove(game_state, valid_moves, difficulty)
    if move is None:
        move = SmartMoveFinder.findRandomMove(valid_moves)
    return move
