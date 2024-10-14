import sys

import pygame
from entity import Entity
from tilemap import Tilemap, Tile

'''.git/

git remote add origin https://github.com/anubh-avbist/ninja_game.git
git branch -M main
git push -u origin main

'''

class Game:
    def __init__(self):

        self.TILESIZE = 16
        UPSCALE = 6
        DISPLAY_SIZE = (320,240)
        SCREEN_SIZE = (320*UPSCALE, 240*UPSCALE)
        pygame.init()
        pygame.display.set_caption('Ball Test')
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.display = pygame.Surface(DISPLAY_SIZE)
        self.clock = pygame.time.Clock()



        self.movement = [False,False]
        self.assets = {
            'ball' : pygame.image.load('assets/images/Ball.png'),
            'default_tile' : pygame.image.load('assets/images/Tile.png')
        }
        self.tiles = {
            (8,8): Tile(self,[8,8],'default_tile', (self.TILESIZE,self.TILESIZE)),
            (9,8): Tile(self,[9,8],'default_tile', (self.TILESIZE,self.TILESIZE)),
            (10,8): Tile(self,[10,8],'default_tile', (self.TILESIZE,self.TILESIZE))
        
        }

        self.player = Entity(self, 'player', (5*self.TILESIZE,5*self.TILESIZE), 'ball', (self.TILESIZE,self.TILESIZE))
        
    def run(self):
        while True:

            self.display.fill((50,70,150))
            self.player.update([self.movement[1] - self.movement[0],0])
            self.player.render(self.display)


            for key in self.tiles:
                tile = self.tiles[key]
                tile.render(self.display)


            level = Tilemap(game, (0,1), 'assets/maps/map.txt')

            # INPUT

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False



            self.screen.blit(pygame.transform.scale((self.display),self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)





game = Game()

game.run()