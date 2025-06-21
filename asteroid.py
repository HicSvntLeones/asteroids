from circleshape import CircleShape
import pygame

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

