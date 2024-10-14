import pygame
from utils import load_sprite

class Entity:
    def __init__(self, game, name, pos, sprite, size):
        self.game = game
        self.name = name
        self.sprite = load_sprite(game,sprite,size)

        self.pos = list(pos)
        self.velocity = [0,0]
        self.speed = 5
        self.rotation = 0


    def update(self, movement):
        self.pos[0] += (self.velocity[0] + movement[0])*self.speed
        self.pos[1] += (self.velocity[1] + movement[1])*self.speed

    def render(self, display):
        display.blit(self.sprite, self.pos)
