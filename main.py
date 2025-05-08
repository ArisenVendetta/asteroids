import sys
import pygame
from constants import * 
from circleshape import CircleShape
from player import Player

def main():
    print('Starting Asteroids!')
    pygame.init()

    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    bg_color = (0, 0, 0)

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            
        display.fill(color=bg_color)
        player.update(dt)
        player.draw(display)
        
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time / 1000

if __name__ == '__main__':
    main()