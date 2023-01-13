import pygame
import numpy as np
import random
from settings import *


# planet class for celestial bodies orbiting a sun
class Planet:

    pos = None
    radius = None
    mass = None
    vel = None
    color = None
    start_pos = None
    path = None
    path_counter = 0
    surface = None

    # assign random starting position and velocity
    def __init__(self, x, y, r, m=None, c=None):
        self.pos = np.array([x,y], dtype='float64')
        self.start_pos = self.pos.copy()
        self.path = []
        self.radius = r
        if m is None:
            self.mass = r*r + random.random()*r
        else:
            self.mass = m
        if c is None:
            self.color = list(np.random.choice(range(256), size=3))
        else:
            self.color = c
        self.vel = np.array([random.uniform(-1,1)*SPEED, random.uniform(-1,1)*SPEED])

        self.surface = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        self.surface.set_alpha(100)

        print(self.pos, self.vel, self.radius, self.mass)

    # draw circle for planet at current position
    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)

    # draw the planet at starting position and a line for the orbit in real-time
    def draw_orbit(self, window):
        pygame.draw.circle(window, self.color, (int(self.start_pos[0]), int(self.start_pos[1])), self.radius)
        if len(self.path)>2:
            pygame.draw.aaline(self.surface, self.color, self.path[len(self.path)-2], self.path[len(self.path)-1])
        elif len(self.path)==1:
            pygame.draw.aaline(self.surface, self.color, self.start_pos, self.path[0])
        window.blit(self.surface,[0,0])

    # set the initial velocity
    def init_vel(self, dx=None, dy=None):
        self.vel[0] = dx if dx is not None else random.random()
        self.vel[1] = dy if dy is not None else random.random()

    # update the planet's position based on gravitational pull
    def move(self):
        self.pos += self.vel

        # add planet's position to previous known path for orbit plotting 
        int_pos = (int(self.pos[0]), int(self.pos[1]))
        if self.path_counter == 1:
            self.path.append(int_pos)
            self.path_counter = 0
        self.path_counter += 1
        if len(self.path)>20:
            self.path.pop(0)