import pygame
from utils import load_sprite

class Player:
    def __init__(self, game, name, pos, sprite, size):
        self.game = game
        self.name = name
        self.sprite = load_sprite(game,sprite,size)
        self.size = size
        self.pos = list(pos)
        self.velocity = [0,0]
        self.speed = 2
        self.rotation = 0
        self.collisions = {'down' : False, 'right': False, 'up': False, 'left': False}

    def rect(self):
        return pygame.Rect(*self.pos, *self.size)


    def update(self, movement):



        self.collisions = {'down' : False, 'right': False, 'up': False, 'left': False}
        

        # Horizontal Movement
        close_tiles = self.game.get_close_tiles(self.pos)
        horizontal_movement = (self.velocity[0] + movement[0])*self.speed
        self.pos[0] += horizontal_movement
        current_rect = self.rect()
        for tile in close_tiles:
            if tile.interactable is True:

                if self.rect().colliderect(tile.rect()):
                    if horizontal_movement > 0:
                        current_rect.right = tile.rect().left
                        self.collisions['right'] = True
                    elif horizontal_movement < 0:
                        current_rect.left = tile.rect().right
                        self.collisions['left'] = True
                    self.pos[0] = current_rect.x

        if self.collisions['right'] or self.collisions['left']:
            self.velocity[0] = 0

        # Vertical Movement
        close_tiles = self.game.get_close_tiles(self.pos)
        self.pos[1] += (self.velocity[1] + movement[1])*self.speed
        current_rect = self.rect()
        for tile in close_tiles:
            if tile.interactable is True:
                if self.rect().colliderect(tile.rect()):
                    if self.velocity[1] > 0:
                        current_rect.bottom = tile.rect().top
                        self.collisions['down'] = True
                    elif self.velocity[1] < 0:
                        current_rect.top = tile.rect().bottom
                        self.collisions['up'] = True

                    self.pos[1] = current_rect.y


        # Gravity
        self.velocity[1] = max(2,self.velocity[1]+0.01)

        if self.collisions['up'] or self.collisions['down']:
            self.velocity[1] = 0



        

    def render(self, display):
        if self.collisions['down']:
            if self.velocity[0] > 0:
                self.rotation += 1
            if self.velocity[0] < 0:
                self.rotation -= 1
        self.sprite = pygame.transform.rotate(self.sprite, self.rotation)
        display.blit(self.sprite, self.pos)
