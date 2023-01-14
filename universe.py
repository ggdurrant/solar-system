import pygame
import math
import random
from planet import Planet
from settings import *


# universe class to hold all objects in system and calculate gravitational forces
class Universe:

    planets = []
    sun = None

    # create random planets from argument and a stationary sun
    def __init__(self, num_planets):
        for i in range(num_planets):
            self.planets.append(Planet(random.randint(10, WIDTH-10), random.randint(10, HEIGHT-10), 10))
        # self.sun = Planet(WIDTH/2, HEIGHT/2, 30, m=50*DENSITY, c=YELLOW)
        self.sun = Planet(WIDTH/2, HEIGHT/2, 30, m=200, c=YELLOW)
        self.sun.init_vel(0,0)
        self.sun.surface.set_colorkey((0,255,0))
        self.sun.surface.set_alpha(200)
        pygame.draw.circle(self.sun.surface, YELLOW, (WIDTH/2-15, HEIGHT/2-15), 30)

    # draw sun 
    def draw_sun(self, window):
        window.blit(self.sun.surface, (0,0))
        
    # calculate gravity and assign forces to each planet in system
    # just calculate gravity via the sun's mass for now
    def update_gravity(self):
        for planet in self.planets:
            bodies = [p for p in self.planets if p!=planet]

            for body in bodies:

                vector = body.pos - planet.pos
                mag = math.sqrt(vector[0]**2+vector[1]**2)
                norm = vector/mag

                local_dist = math.sqrt((body.pos[0] - planet.pos[0])**2 + (body.pos[1] - planet.pos[1])**2)
                local_gravity = norm*G*body.mass/(local_dist**2)
                if abs(local_gravity[0]) > .01:
                    local_gravity[0] = local_gravity[0]*.01
                if abs(local_gravity[1]) > .01:
                    local_gravity[1] = local_gravity[1]*.01
                planet.vel += local_gravity

            # get the normalized vector of gravitational pull
            vector = self.sun.pos - planet.pos
            mag = math.sqrt(vector[0]**2+vector[1]**2)
            norm = vector/mag

            # calculate gravitational force using F = G*m1*m2/r^2
            local_dist = math.sqrt((self.sun.pos[0] - planet.pos[0])**2 + (self.sun.pos[1] - planet.pos[1])**2)
            local_gravity = norm*G*self.sun.mass/(local_dist**2)
            planet.vel += local_gravity

        # # just do gravity wrt the sun
        # for planet in self.planets:
        #     # get the normalized vector of gravitational pull
        #     vector = self.sun.pos - planet.pos
        #     mag = math.sqrt(vector[0]**2+vector[1]**2)
        #     norm = vector/mag

        #     # calculate gravitational force using F = G*m1*m2/r^2
        #     local_dist = math.sqrt((self.sun.pos[0] - planet.pos[0])**2 + (self.sun.pos[1] - planet.pos[1])**2)
        #     local_gravity = norm*G*self.sun.mass/(local_dist**2)
        #     planet.vel += local_gravity

        #     # remove planet if it has escaped solar system
        #     if local_dist > 3000:
        #         self.planets.remove(planet)

    # print planet information
    def print_planets(self):
        for planet in self.planets:
            print(planet.pos[0], planet.pos[1], planet.mass, planet.radius, planet.vel[0], planet.vel[1])
