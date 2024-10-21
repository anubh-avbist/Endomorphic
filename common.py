from typing import Sequence, Tuple, Union

from pygame import Color, Vector2

RGBAOutput = Tuple[int, int, int, int]
ColorValue = Union[Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]

IntoVector2 = str | float | Sequence[float] | Vector2

MapCoordinates = Tuple[int, int]


class Game:
    pass
