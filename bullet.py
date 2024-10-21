import pygame

class Bullet:
    last_fired_time = 0  
    fire_delay = 300  

    def __init__(self, screen, x, y):
        self.screen = screen
        self.rect = pygame.Rect(x, y, 2, 10)  
        self.speed = 10

    @classmethod
    def can_fire(cls):
        current_time = pygame.time.get_ticks()
        if current_time - cls.last_fired_time >= cls.fire_delay:
            cls.last_fired_time = current_time
            return True
        return False

    def update(self):
        self.rect.y -= self.speed

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)  


def handle_bullets(bullets, screen, player_pos):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and Bullet.can_fire():
        bullets.append(Bullet(screen, player_pos[0], player_pos[1]))

    for bullet in bullets[:]:
        bullet.update()
        bullet.draw()
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
