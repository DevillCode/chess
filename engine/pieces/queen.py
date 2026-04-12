"""Queen move generation."""

from .rook import add_rook_moves
from .bishop import add_bishop_moves


def add_queen_moves(state, r, c, moves):
    add_rook_moves(state, r, c, moves)
    add_bishop_moves(state, r, c, moves)
