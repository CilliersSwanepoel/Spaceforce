import pygame
import random

class HealthPellet:
    def __init__(self, screen, speed):
        self.screen = screen
        self.image = pygame.image.load("heart.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_rect().width - self.rect.width)
        self.rect.y = -self.rect.height  
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
