import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0
        self.color = (255, 255, 255)
        self.draw_width = 2
        self.cooldown_timer = 0.0
    # in the player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, self.color, self.triangle(), self.draw_width)

    def rotate(self, dt: int) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: int) -> None:
        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt * -1)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(dt * -1)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt: int) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

    def shoot(self) -> None:
        if self.cooldown_timer <= 0:
            velocity = pygame.Vector2(0, 1)
            velocity = velocity.rotate(self.rotation)
            velocity *= PLAYER_SHOOT_SPEED
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = velocity
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN