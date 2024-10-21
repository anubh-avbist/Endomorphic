import pygame

from common import Game_t as Game
from common import MapCoordinates, Vector2Like
from scripts.utils import Line, load_sprite


class Tile:
    def __init__(self, game: Game, pos: MapCoordinates, tile_type: str, size: Vector2Like, interactable = True):
        self.game = game
        self.pos = [pos[0]*game.TILESIZE,pos[1]*game.TILESIZE]
        self.interactable = interactable
        self.type = tile_type
        self.name = str(pos[0]) + ','+ str(pos[1])
        self.size = size
        self.sprite = load_sprite(game, tile_type, size)
        self.edges: list[Line] = []
        if interactable:
            self.edges.append(Line(pygame.Vector2(self.pos),pygame.Vector2(1,0)))
            self.edges.append(Line(pygame.Vector2(self.pos),pygame.Vector2(0,1)))
            self.edges.append(Line(pygame.Vector2(self.pos) + pygame.Vector2(self.size),pygame.Vector2(-1,0)))
            self.edges.append(Line(pygame.Vector2(self.pos) + pygame.Vector2(self.size),pygame.Vector2(0,-1)))


    def rect(self):
        return pygame.Rect(*self.pos, *self.size)


    def render(self, surf: pygame.Surface):
        surf.blit(self.sprite, self.pos)


class Tilemap:
    def __init__(self, game: Game, initial_pos: MapCoordinates, file_path: str):
        self.game = game
        self.initial_pos = list(initial_pos)
        self.file = open(file_path,'r')
        # print(self.file.readlines())

        j = 0
        for line in self.file.readlines():
            i = 0
            for char in line:
                x = i + initial_pos[0]
                y = j + initial_pos[1]
                if char == '1':
                    game.tiles[(x,y)] = Tile(game, (x,y), 'default_tile', (game.TILESIZE,game.TILESIZE))
                i+=1
            j+=1
    


    