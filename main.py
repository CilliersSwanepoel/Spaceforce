import pygame
from game import Game

def main():
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("Algorithm.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Spaceforce")
    clock = pygame.time.Clock()
    game = Game(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(event.pos)

        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
