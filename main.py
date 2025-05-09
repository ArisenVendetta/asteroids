import sys
import pygame
from constants import * 
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

player: Player = None

def main():
    print('Starting Asteroids!')
    pygame.init()

    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    bg_color = (0, 0, 0)

    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids: pygame.sprite.Group[Asteroid] = pygame.sprite.Group()
    shots: pygame.sprite.Group[Shot] = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            
        display.fill(color=bg_color)

        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_for_collision(player):
                print('Game over!')
                sys.exit(1)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_for_collision(shot):
                    shot.kill()
                    asteroid.split()

        for item in drawable:
            item.draw(display)
        
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time / 1000

if __name__ == '__main__':
    main()