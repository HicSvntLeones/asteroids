from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        self.width = 2
        pygame.draw.circle(screen, 'white', self.position,SHOT_RADIUS, self.width)
    
    def update(self, dt):
        self.position += self.velocity * dt