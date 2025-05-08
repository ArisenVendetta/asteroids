import sys
import pygame
from constants import * 

def main():
    print('Starting Asteroids!')
    pygame.init()

    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    bg_color = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            
            display.fill(color=bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    main()