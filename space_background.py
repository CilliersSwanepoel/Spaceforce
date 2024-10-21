import pygame
import random

class Star:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(0, screen.get_width())
        self.y = random.randint(0, screen.get_height())
        self.speed = random.uniform(0.5, 3)
        self.size = random.choice([1, 2, 3])

    def update(self):
        self.y += self.speed
        if self.y > self.screen.get_height():
            self.y = 0
            self.x = random.randint(0, self.screen.get_width())

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), self.size)

class SpaceBackground:
    def __init__(self, screen, num_stars=100):
        self.screen = screen
        self.stars = [Star(screen) for _ in range(num_stars)]

    def update(self):
        for star in self.stars:
            star.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for star in self.stars:
            star.draw()
