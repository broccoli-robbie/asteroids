import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatables, drawables)
Asteroid.containers = (updatables, drawables, asteroids)
AsteroidField.containers = updatables
Shot.containers = (updatables, drawables, shots)

asteroid_field = AsteroidField()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        for drawable in drawables:
            drawable.draw(screen)
        updatables.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
            if asteroid.collision(player):
                sys.exit("Game Over!")
        pygame.display.flip()
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()
