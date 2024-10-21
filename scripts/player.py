import math

import pygame

from common import Game_t as Game
from common import MapCoordinates
from scripts.bezier import Bezier
from scripts.leg import Leg
from scripts.tilemap import Tile
from scripts.utils import load_sprite


class Player:
    def __init__(self, game: Game, name: str, pos: MapCoordinates, sprite, size):
        self.game = game
        self.name = name
        self.sprite = load_sprite(game,sprite,size)
        self.size = size
        self.pos = list(pos)
        self.velocity = [0.,0.]

        self.speed = 2
        self.rotation = 0
        self.collisions = {'down' : False, 'right': False, 'up': False, 'left': False}
        self.frame_movement = [0,0]
        self.legs: list[Leg] = []


        self.jump_frame = False
        self.jump_height = 2
        self.allowed_jumps = 1

        self.time = 0

    def vertical_offset(self) -> int:
        return 0 #2*math.sin(self.time)

    def center(self) -> list[int]:
        return [self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2]



    def rect(self) -> pygame.Rect:
        return pygame.Rect(*self.pos, *self.size)


    def get_close_tiles(self) -> list[Tile]:
        tiles = []
        x = self.pos[0]//self.game.TILESIZE
        y = self.pos[1]//self.game.TILESIZE

        permutations = [(-2,-2),(-1,-1), (0,-1), (1,-1), (-1,0), (0,0), (1,0), (-1,1), (0,1), (1,1)]
        for permutation in permutations:
            key = ((x+permutation[0], y+permutation[1]))
            if key in self.game.tiles:
                tiles.append(self.game.tiles.get((x+permutation[0], y+permutation[1])))

        return tiles

    def update(self, movement):
        self.collisions = {'down' : False, 'right': False, 'up': False, 'left': False}
        
        self.frame_movement = (self.speed*(movement[0] + self.velocity[0]), self.speed*(movement[1] + self.velocity[1]))
        
        # Horizontal Movement
        self.pos[0] += self.frame_movement[0]
        current_rect = self.rect()
        for tile in self.get_close_tiles():
            if tile.interactable is True:
                if self.rect().colliderect(tile.rect()):
                    if self.frame_movement[0] > 0:
                        current_rect.right = tile.rect().left
                        self.collisions['right'] = True
                    elif self.frame_movement[0] < 0:
                        current_rect.left = tile.rect().right
                        self.collisions['left'] = True
                    self.pos[0] = current_rect.x

        if self.collisions['right'] or self.collisions['left']:
            self.velocity[0] = 0

        # Vertical Movement       
        self.pos[1] += self.frame_movement[1]
        current_rect = self.rect()
        for tile in self.get_close_tiles():
            if tile.interactable is True:
                if self.rect().colliderect(tile.rect()):
                    if self.frame_movement[1] > 0:
                        current_rect.bottom = tile.rect().top
                        self.collisions['down'] = True
                        self.allowed_jumps = 1
                    elif self.frame_movement[1] < 0:
                        current_rect.top = tile.rect().bottom
                        self.collisions['up'] = True

                    self.pos[1] = current_rect.y



        # Gravity
        self.velocity[1] = min(3,self.velocity[1]+0.1)

        if self.collisions['up'] or self.collisions['down']:
            self.velocity[1] = 0

        # Time
        self.time += 0.05
        if self.time > math.pi*2:
            self.time -= math.pi*2


    def jump(self):
        if self.allowed_jumps:
            self.allowed_jumps -= 1
            self.velocity[1] = -2

    def render(self, display: pygame.Surface):
        frame_rotation = 0

        if self.collisions['down']:
            if self.frame_movement[0] > 0:
                frame_rotation -= 10
            if self.frame_movement[0] < 0:
                frame_rotation += 10
        self.rotation += frame_rotation

        
        # self.sprite = pygame.transform.rotate(self.sprite, frame_rotation)
        # self.sprite = pygame.transform.rotate(self.sprite, 10)
        # rotated_sprite = pygame.transform.rotate(self.sprite,self.rotation)
        
        display.blit(self.sprite, (self.pos[0], self.pos[1] + self.vertical_offset()))



