import pygame
import math
import random

class Bezier:
    def __init__(self, game, points, color, thickness = 1, pixel_size = 1, segments = 100):
        self.game = game
        self.points = points
        self.color = color
        self.thickness = thickness
        self.degree = len(self.points)-1
        self.start = self.points[0]
        self.end = self.points[self.degree]
        self.pixel_size = 2
        self.segments = segments

    def fun(self, t):
        output = [0,0]
        
        for i in range(0,len(self.points)):
            multiplier = math.comb(self.degree,i) * math.pow(t,i) *math.pow(1-t,self.degree-i)
            
            output[0] += multiplier * self.points[i][0]
            output[1] += multiplier * self.points[i][1]
        return output
    
    def grid_snap(self, point):
        return [int(point[0]), int(point[1])]

    def draw(self, surf):
        division = 1/self.segments
        t = 0
        for i in range(0,self.segments):
            pygame.draw.rect(surf,self.color, (*self.grid_snap(self.fun(t)), self.pixel_size,self.pixel_size))
            t += division

    def dummy_update(self):
        self.points[0] = [pygame.mouse.get_pos()[0]/self.game.UPSCALE,pygame.mouse.get_pos()[1]/self.game.UPSCALE]
        self.points[self.degree] = self.game.player.rect().center