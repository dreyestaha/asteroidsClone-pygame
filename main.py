import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_one = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player_one.draw(screen)
        delta_time = clock.tick(60) /1000
        player_one.update(delta_time)
        pygame.display.flip()

if __name__ == "__main__":
    main()
