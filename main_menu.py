import pygame

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.logo_font = pygame.font.Font(None, 100)
        self.start_button_rect = pygame.Rect(0, 0, 200, 50)
        self.exit_button_rect = pygame.Rect(0, 0, 200, 50)
        self.start_button_rect.center = (screen.get_width() // 2, screen.get_height() // 2 - 50)
        self.exit_button_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 50)
        pygame.mixer.music.load("Azimuth.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def draw(self):
        self.screen.fill((0, 0, 0))

        
        logo_text = self.logo_font.render("Spaceforce", True, (255, 255, 0))  
        logo_outline = self.logo_font.render("Spaceforce", True, (0, 100, 0))  
        logo_rect = logo_text.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(logo_outline, logo_rect.move(2, 2))  
        self.screen.blit(logo_outline, logo_rect.move(-2, -2))
        self.screen.blit(logo_outline, logo_rect.move(2, -2))
        self.screen.blit(logo_outline, logo_rect.move(-2, 2))
        self.screen.blit(logo_text, logo_rect)

        
        start_text = self.font.render("Start", True, (255, 255, 0)) 
        exit_text = self.font.render("Exit", True, (255, 255, 0))   
        pygame.draw.rect(self.screen, (0, 100, 0), self.start_button_rect)  
        pygame.draw.rect(self.screen, (0, 100, 0), self.exit_button_rect)   
        self.screen.blit(start_text, start_text.get_rect(center=self.start_button_rect.center))
        self.screen.blit(exit_text, exit_text.get_rect(center=self.exit_button_rect.center))

    def handle_click(self, pos):
        if self.start_button_rect.collidepoint(pos):
            pygame.mixer.music.stop()
            return "start"
        elif self.exit_button_rect.collidepoint(pos):
            return "exit"
        return None