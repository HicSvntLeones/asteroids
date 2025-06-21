# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
import sys
import pygame
import random
from asteroid import Asteroid
from constants import *
from shot import Shot


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    clock = pygame.time.Clock()
    dt = 0
    cooldown = 0.3
    
    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        cooldown -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if cooldown <= 0:
                player.shoot(player.position[0], player.position[1], player.rotation, shots)
                cooldown = 0.3

        for item in asteroids:
            if item.collide_check(player):
                print("Game over!")
                sys.exit()
            for item2 in shots:
                if item.collide_check(item2):
                    # print("hit")
                    item.split()

        screen.fill('black', rect=None, special_flags=0) 
        for item in drawable:
            item.draw(screen)
            
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
