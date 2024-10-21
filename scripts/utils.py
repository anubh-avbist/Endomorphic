from typing import Any

import pygame

from common import Game_t as Game
from common import MapCoordinates, Vector2Like


class Line():
    def __init__(self, start, direction: pygame.Vector2):
        self.start = pygame.Vector2(start)
        self.direction = direction

    def r(self, t: int | float) -> pygame.Vector2:
        return self.start + t * self.direction

    def get_intersection_parameter(self, other_line: 'Line'):
        alpha = other_line.direction.x
        beta = other_line.direction.y
        x_1 = other_line.start.x
        y_1 = other_line.start.y

        u = self.direction.x
        v = self.direction.y
        x_0 = self.start.x
        y_0 = self.start.y

        if (alpha*v-beta*u) != 0:
            return (alpha*(y_1-y_0)-beta*(x_1-x_0))/(alpha*v-beta*u)
        else: 
            return -1

    def get_intersection(self, other_line: 'Line') -> pygame.Vector2:
        return self.r(self.get_intersection_parameter(other_line))

    def draw(self, surf: pygame.Surface, range):
        pygame.draw.line(surf, (0,0,0), self.start + self.direction*range[0], self.start + self.direction*range[1])

def load_sprite(game: Game, sprite: str, size: Vector2Like) -> pygame.Surface:
    return pygame.transform.scale(game.assets[sprite], (size))

def rotate_sprite(sprite, angle):
    pass

def raycast(game: Game, line: Line, length: int, step: int | float, tileset: dict[MapCoordinates, Any]) -> Vector2Like:
    line.direction = line.direction.normalize()

    distance = 0 # Moves by one TILESIZE/2
    current = line.start + line.direction * step
    tile = None
    while distance <= length:
        key = (current.x//game.TILESIZE, current.y//game.TILESIZE)
        if key in tileset:
            if tileset[key].interactable:
                tile = tileset[key]
                break
        current = current + line.direction * step
        distance += step
    if tile is None:
        return [0,0] #line.start + line.direction*length
    else: 
        game.debug['highlight'] = tile
        found = False
        t = length
        for edge in tile.edges:
            b = line.get_intersection_parameter(edge) # Parameter from casting line
            c = edge.get_intersection_parameter(line) # Parameter for tile edge

            if b >= 0 and b <= t and c >= 0 and c<=game.TILESIZE:
                found = True
                t = b

        if found:
            return line.r(t)
        else:
            return edge.r(length*1) # type: ignore


