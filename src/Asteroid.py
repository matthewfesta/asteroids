import pygame
import random
from CircleShape import CircleShape
import constants


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x,y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        radius = self.radius - constants.ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, radius).velocity = velocity1 * 1.2
        Asteroid(self.position.x, self.position.y, radius).velocity = velocity2 * 1.2



