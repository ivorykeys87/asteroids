# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys
import time
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect = None, special_flags = 0)
        for thing in updatable:
            thing.update(delta_time)
        for thing in asteroids:
            if thing.collisions(player):
                print("Game Over!")
                time.sleep(5)
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.kill()
                    shot.kill()

        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

if __name__ == "__main__":
    main()