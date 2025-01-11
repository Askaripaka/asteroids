from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
           

    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position.x,self.position.y),self.radius,2)

    def update(self, dt):
        self.position += self.velocity*dt

    def kill(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)

            self.velocity.rotate(random_angle)
            self.velocity.rotate(-random_angle)

            n_radius = self.radius - ASTEROID_MIN_RADIUS

            n_obj_1 = Asteroid(self.position.x, self.position.y, n_radius)
            n_obj_2 = Asteroid(self.position.x, self.position.y, n_radius)

            n_obj_1.velocity += n_radius * 1.2
            n_obj_2.velocity = n_radius * 1.2



            
