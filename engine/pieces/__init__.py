"""Piece move-generation modules."""

from .pawn import add_pawn_moves
from .rook import add_rook_moves
from .bishop import add_bishop_moves
from .queen import add_queen_moves
from .knight import add_knight_moves
from .king import add_king_moves

__all__ = [
    "add_pawn_moves",
    "add_rook_moves",
    "add_bishop_moves",
    "add_queen_moves",
    "add_knight_moves",
    "add_king_moves",
]
