import pygame

from game import Game


def main():
    game = Game()
    pygame.mixer.init()
    pygame.mixer.music.load("music2.mp3")
    pygame.mixer.music.play(2, 10)
    game.menu()
    pygame.mixer.music.unload()
    pygame.mixer.init()
    pygame.mixer.music.load("gameplaymusic.mp3")
    pygame.mixer.music.play(2, 10)
    game.run()
    quit()


if __name__ == '__main__':
    main()
