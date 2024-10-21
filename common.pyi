from typing import Any, List, Sequence, Tuple

from pygame import Color, Surface, Vector2
from pygame.time import Clock

from game import Game as BaseGame
from scripts.player import Player
from scripts.tilemap import Tile, Tilemap

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
)

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
    debug: dict[str, Any]

Game_t = Game | BaseGame
