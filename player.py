import pygame
from utils import load_sprite
from bezier import Bezier

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
        self.frame_movement = [0,0]
        self.legs = []


        self.jump_frame = False
        self.jump_height = 2

    def rect(self):
        return pygame.Rect(*self.pos, *self.size)


    def update(self, movement):



        self.collisions = {'down' : False, 'right': False, 'up': False, 'left': False}
        

        # Horizontal Movement
        close_tiles = self.game.get_close_tiles(self.pos)
        horizontal_movement = (self.velocity[0] + movement[0])*self.speed
        self.pos[0] += horizontal_movement
        self.frame_movement[0] = horizontal_movement
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

        if self.jump_frame is True:
            print("HI")
            self.jump_frame = False
            self.velocity[1] = -self.jump_height

        vertical_movement = (self.velocity[1] + movement[1])*self.speed
        self.pos[1] += vertical_movement

        self.frame_movement[1] = vertical_movement
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
        self.velocity[1] = min(2,self.velocity[1]+0.1)

        if self.collisions['up'] or self.collisions['down']:
            self.velocity[1] = 0

        self.render(self.game.display)

    def jump(self):
        self.jump_frame = True

    def render(self, display):
        frame_rotation = 0

        if self.collisions['down']:
            if self.frame_movement[0] > 0:
                frame_rotation -= 10
            if self.frame_movement[0] < 0:
                frame_rotation += 10
        self.rotation += frame_rotation

        
        #self.sprite = pygame.transform.rotate(self.sprite, frame_rotation)
        #self.sprite = pygame.transform.rotate(self.sprite, 10)
        #rotated_sprite = pygame.transform.rotate(self.sprite,self.rotation)
        
        display.blit(self.sprite, self.pos)



