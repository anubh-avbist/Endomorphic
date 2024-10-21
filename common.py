from typing import List, Sequence, Tuple

from pygame import Color, Vector2

RGBAOutput = Tuple[int, int, int, int]
ColorValue = Color | int | str | Tuple[int, int, int] | RGBAOutput | Sequence[int]

Vector2Like = (
    Vector2
    | Tuple[float, float]
    | Tuple[float, int]
    | Tuple[int, float]
    | Tuple[int, int]
    | Tuple[int | float, int | float]
    | List[int]
    | List[float]
    | List[int | float]
)

MapCoordinates = Tuple[int, int]


class Game:
    pass


Game_t = Game
