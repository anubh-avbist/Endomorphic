import sys

import pygame
from scripts.player import Player
from scripts.tilemap import Tilemap, Tile
from scripts.bezier import Bezier

'''.git/

git remote add origin https://github.com/anubh-avbist/ninja_game.git
git branch -M main
git push -u origin main

'''

class Game:
    def __init__(self):

        self.TILESIZE = 16
        self.UPSCALE = 6
        DISPLAY_SIZE = (320,240)
        SCREEN_SIZE = (320*self.UPSCALE, 240*self.UPSCALE)

        pygame.init()
        pygame.display.set_caption('Ball Test')
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.display = pygame.Surface(DISPLAY_SIZE)
        self.clock = pygame.time.Clock()



        self.assets = {
            'ball' : pygame.image.load('assets/images/Ball.png'),
            'default_tile' : pygame.image.load('assets/images/Tile.png')
        }

        self.tiles = {
            (8,8): Tile(self,[8,8],'default_tile', (self.TILESIZE,self.TILESIZE)),
        }





        self.movement = [[False,False],[False,False]]
        self.player = Player(self, 'player', (5*self.TILESIZE,5*self.TILESIZE), 'ball', (self.TILESIZE,self.TILESIZE))


        #self.bez = Bezier(self, [[50,50], [100,75]], (50,10,20))

        self.level = Tilemap(self, (0,1), 'assets/maps/map.txt')
            

    
    def get_close_tiles(self, pos, scaled = False):
        tiles = []
        x = int(pos[0]//self.TILESIZE)
        y = int(pos[1]//self.TILESIZE)
        permutations = [(-1,-1), (0,-1), (1,-1), (-1,0), (0,0), (1,0), (-1,1), (0,1), (1,1)]
        for permutation in permutations:
            key = (x+permutation[0], y+permutation[1])
            if key in game.tiles:
                tiles.append(game.tiles[(x+permutation[0], y+permutation[1])])

        return tiles
        
    def run(self):
        while True:
            self.display.fill((50,70,150))
            self.player.update([self.movement[0][1] - self.movement[0][0], self.movement[1][0] - self.movement[1][1]])

            # INPUT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[0][1] = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0][0] = True
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[1][1] = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1][0] = True
                    if event.key == pygame.K_SPACE:
                        #self.player.jump()
                        pass

                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[0][1] = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0][0] = False
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[1][1] = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1][0] = False


            for key in self.tiles:
                tile = self.tiles[key]
                tile.render(self.display)


            self.screen.blit(pygame.transform.scale((self.display),self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)


game = Game()

game.run()