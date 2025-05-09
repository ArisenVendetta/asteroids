import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius=radius)
        self.color = (30, 255, 30)
        self.draw_width: int = 2

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.draw_width)
    
    def update(self, dt: int) -> None:
        self.move(dt)

    def move(self, dt: int) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            new_angle = random.uniform(20, 50)
            new_velocity_a = self.velocity.rotate(new_angle)
            new_velocity_b = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child_a = Asteroid(self.position.x, self.position.y, new_radius)
            child_b = Asteroid(self.position.x, self.position.y, new_radius)
            child_a.velocity = new_velocity_a
            child_b.velocity = new_velocity_b