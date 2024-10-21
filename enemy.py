import pygame
import random

class Enemy:
    def __init__(self, screen, speed):
        self.screen = screen
        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_rect().width - self.rect.width)
        self.rect.y = -self.rect.height  
        self.speed = speed

        
        self.horizontal_speed = random.choice([-1, 1]) * random.uniform(0.5, 2.0)

    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.horizontal_speed

        
        if self.rect.left < 0 or self.rect.right > self.screen.get_rect().width:
            self.horizontal_speed = -self.horizontal_speed  

    def draw(self):
        self.screen.blit(self.image, self.rect)
