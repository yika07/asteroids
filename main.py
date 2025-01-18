import pygame 
from constants import *
from player import Player
from asteroids import *
from asteroidfield import *
import sys

def main(): 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroid_obect = AsteroidField()
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for p in drawable:
            p.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time/1000
        for p in updatable: 
            p.update(dt)
            if isinstance(p, Player):
                for ast in asteroids: 
                    if ast.collides_with(p): 
                        sys.exit("Game over!")
            if isinstance(p, Shot): 
                for ast in asteroids: 
                    if ast.collides_with(p): 
                        p.kill()
                        ast.split()



if __name__ == "__main__": 
    main()