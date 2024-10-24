import pygame
from game import Game
from main_menu import MainMenu

def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Spaceforce")
    clock = pygame.time.Clock()

    main_menu = MainMenu(screen)
    game = Game(screen)

    running = True
    in_main_menu = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if in_main_menu:
                    action = main_menu.handle_click(event.pos)
                    if action == "start":
                        pygame.mixer.music.load("Algorithm.mp3")
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
                        in_main_menu = False
                    elif action == "exit":
                        running = False
                else:
                    game.handle_click(event.pos)

        if in_main_menu:
            main_menu.draw()
        else:
            game.update()
            game.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
