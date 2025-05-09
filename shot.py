import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)
        self.color = (77, 77, 77)
        self.draw_width = 1

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.draw_width)
    
    def update(self, dt: int) -> None:
        self.move(dt)

    def move(self, dt: int) -> None:
        self.position += (self.velocity * dt)
    