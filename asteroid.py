from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
            super().__init__(x, y, radius)
            self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            self.rect = self.image.get_rect(center=self.position)
    
    def draw(self, screen):
        self.width = 2
        pygame.draw.circle(screen, 'white', self.position,self.radius, self.width)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
             return
        else:
            angle = random.uniform(20,50)
            asteroid = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            asteroid.velocity = self.velocity.rotate(angle)
            asteroid.velocity *= 1.2
            asteroid = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            asteroid.velocity = self.velocity.rotate(-angle)
            asteroid.velocity *= 1.2
             

