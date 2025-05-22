from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        
        # check if smol
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        V1 = pygame.math.Vector2.rotate(self.velocity, angle)
        V2 = pygame.math.Vector2.rotate(self.velocity, -angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        A1 = Asteroid(self.position.x, self.position.y, new_radius)
        A1.velocity = V1 * 1.2

        A2 = Asteroid(self.position.x, self.position.y, new_radius)
        A2.velocity = V2 * 1.2