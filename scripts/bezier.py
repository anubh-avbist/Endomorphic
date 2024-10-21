import pygame
import math
import random

class Bezier:
    def __init__(self, game, points: list, color = (0,0,0), pixel_size = 1, segments = 100):
        self.game = game
        self.points = points
        self.color = color
        self.pixel_size = pixel_size
        self.segments = segments

        self.degree = len(self.points)-1
        self.start = self.points[0]
        self.end = self.points[self.degree]

    def fun(self, t):
        output = [0,0]
        
        for i in range(0,len(self.points)):
            multiplier = math.comb(self.degree,i) * math.pow(t,i) *math.pow(1-t,self.degree-i)
            
            output[0] += multiplier * self.points[i][0]
            output[1] += multiplier * self.points[i][1] 
        return output
    