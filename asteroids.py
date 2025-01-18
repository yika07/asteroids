from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", 
                           center=self.position, radius=self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self): 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return 
        else: 
            random_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)
            small_radius = self.radius - ASTEROID_MIN_RADIUS
            small_ast_1 = Asteroid(self.position[0], self.position[1], small_radius)
            small_ast_2 = Asteroid(self.position[0], self.position[1], small_radius)
            small_ast_1.velocity = velocity1 * 1.2
            small_ast_2.velocity = velocity2 * 1.2





class Shot(CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", 
                           center=self.position, radius=SHOT_RADIUS,width=2)

    def update(self, dt):
        self.position += self.velocity * dt 
