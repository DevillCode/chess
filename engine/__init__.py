"""Engine package for chess rules and state."""

__all__ = ["GameState", "Move", "castleRights"]


def __getattr__(name):
    if name in __all__:
        from .models import GameState, Move, castleRights
        mapping = {
            "GameState": GameState,
            "Move": Move,
            "castleRights": castleRights,
        }
        return mapping[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
