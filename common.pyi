from typing import Sequence, Tuple, Union

from pygame import Color, Surface, Vector2
from pygame.time import Clock

from scripts.player import Player
from scripts.tilemap import Tile, Tilemap
from game import Game as BaseGame

RGBAOutput = Tuple[int, int, int, int]
ColorValue = Union[Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]

IntoVector2 = str | float | Sequence[float] | Vector2

MapCoordinates = Tuple[int, int]

class Game:
    FPS: int
    TILESIZE: int
    UPSCALE: int
    DISPLAY_SIZE: Tuple[int, int]
    SCREEN_SIZE: Tuple[int, int]

    screen: Surface
    display: Surface
    clock: Clock
    assets: dict[str, Surface]
    tiles: dict[MapCoordinates, Tile]
    movement: list[list[bool]]
    player: Player
    level: Tilemap
    delta_time: int


Game_t = Game | BaseGame