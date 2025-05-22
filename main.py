import pygame
from constants import *
from player import *
from asteroidfield import *
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0 # delta time

    # Game loop
    while True:
        # Check if game is closed, end loop if so
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if player.collide(asteroid):
                player.death()

        # Check for collisions with shots
        for asteroid in asteroids:
            for shot in shots:
                # print(shot.position, asteroid.position, shot.radius, asteroid.radius)
                if shot.collide(asteroid):
                    player.updatepoints()
                    shot.kill()
                    asteroid.split()

        # yay progression
        if player.score % 150 == 0 and not player.upgrade_triggered and player.score != 0:
            player.upgrade_weapon()

        if player.score % 150 != 0:
            player.upgrade_triggered = False

        # Set bg to black
        screen.fill("black")

        # Draw
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000 # Set the frame rate to 60 FPS (pause for 1/60 seconds)

if __name__ == "__main__":
    main()