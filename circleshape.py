import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int):
        if hasattr(self, 'containers'):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: int = radius

    def draw(self, screen: pygame.Surface):
        pass

    def update(self, dt: int):
        pass
    
    def check_for_collision(self, other: 'CircleShape') -> bool:
        threshold = self.radius + other.radius
        distance = self.position.distance_to(other.position)
        return distance <= threshold