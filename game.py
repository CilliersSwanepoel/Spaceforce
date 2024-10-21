import pygame
from space_background import SpaceBackground  
from player import Player
from enemy import Enemy
from bullet import Bullet

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.bullets = []
        self.player = Player(screen, self.bullets)
        self.enemies = []
        self.score = 0
        self.lives = 3  
        self.font = pygame.font.Font(None, 36)
        self.last_spawn_time = pygame.time.get_ticks()
        self.enemy_speed = 2  
        self.spawn_delay = 2000  
        self.game_over = False

        
        self.space_background = SpaceBackground(screen, num_stars=200)

        
        self.restart_button_rect = pygame.Rect(0, 0, 100, 40)

    def update(self):
        if self.game_over:
            return
        
        
        self.space_background.update()

        
        self.player.update()
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)
            for enemy in self.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    self.score += 10
                    break

        
        for enemy in self.enemies[:]:
            enemy.update()
            
            if enemy.rect.top > self.screen.get_rect().bottom:
                self.enemies.remove(enemy)
                self.lose_life()
            elif enemy.rect.colliderect(self.player.rect):
                self.enemies.remove(enemy)
                self.lose_life()

        
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time >= self.spawn_delay:
            self.spawn_enemy()
            self.last_spawn_time = current_time

        
        self.increase_enemy_speed()

    def draw(self):
        
        self.space_background.draw()

        
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        for bullet in self.bullets:
            bullet.draw()

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 40))

        
        if self.game_over:
            game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(game_over_text, game_over_rect.topleft)
            
            
            self.restart_button_rect.centerx = self.screen.get_width() // 2
            self.restart_button_rect.y = game_over_rect.bottom + 20
            
            pygame.draw.rect(self.screen, (255, 255, 255), self.restart_button_rect)
            restart_text = self.font.render("Restart", True, (0, 0, 0))
            restart_text_rect = restart_text.get_rect(center=self.restart_button_rect.center)
            self.screen.blit(restart_text, restart_text_rect.topleft)

    def spawn_enemy(self):
        enemy = Enemy(self.screen, self.enemy_speed)
        self.enemies.append(enemy)

    def increase_enemy_speed(self):
        
        time_passed = pygame.time.get_ticks() / 1000  
        self.enemy_speed = 2 + (time_passed / 30)  

    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_over = True

    def handle_click(self, pos):
        
        if self.game_over and self.restart_button_rect.collidepoint(pos):
            self.reset_game()

    def reset_game(self):
        
        self.bullets.clear()
        self.enemies.clear()
        self.score = 0
        self.lives = 3
        self.enemy_speed = 2
        self.last_spawn_time = pygame.time.get_ticks()
        self.game_over = False
