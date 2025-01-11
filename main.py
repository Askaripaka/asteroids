import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    running = True

    pos_x = SCREEN_WIDTH
    pos_y = SCREEN_HEIGHT

    player_pos_x = SCREEN_WIDTH/2
    player_pos_y = SCREEN_HEIGHT/2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable,drawable)
    Shot.containers = (updatable,drawable)
    

    p1 = Player(player_pos_x,player_pos_y)
    asteroid_field = AsteroidField()
    
    

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((pos_x,pos_y))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.has_collided_with(p1):
                print("GAME OVER!")
                sys.exit()
            
            for bullet in shots:
                if asteroid.has_collided_with(bullet):
                    asteroid.split()
                    bullet.kill()
        
         
        pygame.display.flip()


        dt= clock.tick(60)/1000
        
       


         


if __name__ == "__main__":
    main()