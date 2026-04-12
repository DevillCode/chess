"""Compatibility layer for the chess engine models.

This module provides a stable import path for game-state primitives so UI and
other layers do not import the legacy top-level module directly.
"""

from ChessEngine import GameState, Move, castleRights

__all__ = ["GameState", "Move", "castleRights"]
