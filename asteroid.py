from circleshape import CircleShape
from constants import *
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        first_velocity = self.velocity.rotate(split_angle) * 1.2
        second_velocity = self.velocity.rotate(-split_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_ass = Asteroid(self.position.x, self.position.y, new_radius)
        second_ass = Asteroid(self.position.x, self.position.y, new_radius)

        first_ass.velocity = first_velocity
        second_ass.velocity = second_velocity

