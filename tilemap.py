import pygame
from utils import load_sprite

class Tile:
    def __init__(self, game, pos, tile_type, size, interactable = True):
        self.game = game
        self.pos = [pos[0]*game.TILESIZE,pos[1]*game.TILESIZE]
        self.interactable = interactable
        self.type = tile_type
        self.name = str(pos[0]) + ','+ str(pos[1])

        self.sprite = load_sprite(game, tile_type, size)

    def render(self, surf):
        surf.blit(self.sprite, self.pos)


class Tilemap:
    def __init__(self, game, initial_pos, file_path):
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
                    print('hi')
                    game.tiles[(x,y)] = Tile(game, [x,y], 'default_tile', (game.TILESIZE,game.TILESIZE))
                i+=1
            j+=1
    


    