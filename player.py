import pygame
import os
from bullet import Bullet

class Player:
    def __init__(self, screen, bullets):
        self.screen = screen
        self.bullets = bullets
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen.get_rect().right:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        
        if Bullet.can_fire():
            bullet = Bullet(self.screen, self.rect.centerx, self.rect.top)
            self.bullets.append(bullet)

    def draw(self):
        self.screen.blit(self.image, self.rect)
