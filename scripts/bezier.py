import math
import random

import pygame

from common import ColorValue
from common import Game_t as Game
from common import Vector2Like


class Bezier:
    def __init__(self, game: Game, points: list[Vector2Like], color: ColorValue = (0,0,0), pixel_size = 1, segments = 100):
        self.game = game
        self.points = points
        self.color = color
        self.pixel_size = pixel_size
        self.segments = segments

        self.degree = len(self.points)-1
        self.start = self.points[0]
        self.end = self.points[self.degree]

    def fun(self, t: int | float) -> list[float]:
        output = [0.,0.]
        
        for i, point in enumerate(self.points):
            multiplier = math.comb(self.degree,i) * math.pow(t,i) *math.pow(1-t,self.degree-i)
            
            output[0] += multiplier * point[0]
            output[1] += multiplier * point[1] 
        return output
    