import pygame
from constants import *
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Check if game is closed, end loop if so
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Set bg to black
        pygame.Surface.fill(screen, (0, 0, 0))  # Fill the screen with black
        pygame.display.flip()

if __name__ == "__main__":
    main()