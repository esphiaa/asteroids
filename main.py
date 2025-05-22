import pygame
from constants import *
from player import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
dt = 0 # delta time

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(x, y)

    # Game loop
    while True:
        # Check if game is closed, end loop if so
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Set bg to black
        pygame.Surface.fill(screen, (0, 0, 0))  # Fill the screen with black
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000 # Set the frame rate to 60 FPS (pause for 1/60 seconds)

if __name__ == "__main__":
    main()