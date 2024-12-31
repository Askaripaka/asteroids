import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    running = True

    pos_x = SCREEN_WIDTH
    pos_y = SCREEN_HEIGHT

    player_pos_x = SCREEN_WIDTH/2
    player_pos_y = SCREEN_HEIGHT/2

    p1 = Player(player_pos_x,player_pos_y)

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((pos_x,pos_y))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        p1.draw(screen=screen)    
        
        pygame.display.flip()

        delta_time = clock.tick(60)
        dt = delta_time/1000


         


if __name__ == "__main__":
    main()