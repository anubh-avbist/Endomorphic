import pygame
import math
from scripts.bezier import Bezier
import random
from scripts.utils import raycast, Line

class Leg(Bezier):
    def __init__(self, game, points, length, color = (0,0,0), pixel_size = 2, segments = 100):
        self.game = game
        self.points = points
        self.color = color
        self.length = length
        self.pixel_size = pixel_size
        self.segments = segments

        self.degree = len(self.points)-1 # SHOULD ALWAYS BE 2
        self.start = self.points[0]
        self.end = self.points[self.degree]

        self.orientation = -1 

        self.destination = [0,0]
        self.ray = [0,self.length]
        self.transitioning = False
        self.transition_time = 0.25
        self.timer = 0
        self.foot_path = Bezier(self.game, [[0,0], [0,0], [0,0]])

    def update(self):
        # Root
        self.points[0] = (self.game.player.center()[0],self.game.player.center()[1] + self.game.player.vertical_offset())

        # Foot
        start = pygame.Vector2(self.points[0])
        end = pygame.Vector2(self.points[self.degree])
        direction = end - start
        distance = pygame.Vector2.magnitude(direction)

        # If maxlength
        if distance > self.length:
            # Start moving Leg
            if not self.transitioning:

                # Random orientation
                self.orientation = 1
                if random.random()>0.5:
                    self.orientation = -1
            
                self.transitioning = True
                self.timer = 0
                self.foot_path.points[0] = end

                # Destination
            self.pick_destination(start)


            # Snap leg to circle
            direction = self.length*pygame.Vector2.normalize(direction)
            distance = self.length
            new_end = start + direction
            self.points[self.degree] = [new_end.x, new_end.y]

        


        # If transitioning
        if self.transitioning:
            self.transition()



        # Joint
        h = distance/2
        b = 1.2* math.sqrt((self.length/2)**2 - h**2)
        perpendicular = pygame.Vector2(direction.y, -direction.x)
        perpendicular = self.orientation*b * pygame.Vector2.normalize(perpendicular)
        self.points[1] = self.points[0] + (direction/2) + perpendicular

    def pick_destination(self, start):
        self.foot_path.points[0] = self.points[self.degree]
        self.timer = 0

        direction = [0,1]
        if self.game.player.frame_movement[0] > 0 :
            direction[0] = 1
        elif self.game.player.frame_movement[0] < 0:
            direction[0] = -1
        # self.ray = pygame.Vector2.normalize(pygame.Vector2(*direction))*self.length*0.9

        cast = Line(self.game.player.center(), pygame.Vector2(direction[0], direction[1]))
        self.destination = raycast(self.game, cast, self.length, self.game.TILESIZE, self.game.tiles)

        #self.destination = start + self.ray

    def transition(self):
            self.timer += self.game.delta_time/1000
            t = self.timer/self.transition_time

            # Create Foot Path:
            self.foot_path.points = [self.foot_path.points[0], self.game.player.center(), self.destination]

            self.points[self.degree] = self.foot_path.fun(t)

            if pygame.Vector2.magnitude(pygame.Vector2(self.points[self.degree])-pygame.Vector2(self.points[0])) > self.length:
                self.pick_destination(self.points[self.degree])
                self.timer = 0

            
            if t>=1: 
                self.transitioning = False
    
    def debug(self, surf):
        pygame.draw.rect(surf, (50,255,50), (*self.destination, self.pixel_size,self.pixel_size))
        pygame.draw.rect(surf, (255,50,50), (*self.foot_path.points[0], self.pixel_size,self.pixel_size))

    def draw(self, surf):
        division = 1/self.segments
        t = 0
        for i in range(0,self.segments):
            pygame.draw.rect(surf,self.color, (*self.fun(t), self.pixel_size,self.pixel_size))
            t += division

        self.debug(surf)
        