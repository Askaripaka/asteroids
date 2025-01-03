from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        

        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            surface=screen,
            color="white",
            points=self.triangle(),
            width=2
        )

    def rotate(self,dt):
        self.rotation = self.rotation + dt*PLAYER_TURN_SPEED

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)



   
   
   
