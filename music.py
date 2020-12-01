import pygame


class Music:
    def __init__(self):
        pygame.mixer.init()

    def playTheme(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load('res/themeMusic.mp3')
        pygame.mixer.music.set_volume(0.02)
        pygame.mixer.music.play(-1)

    def playInGameMusic(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load('res/inGameMusic.mp3')
        pygame.mixer.music.set_volume(0.02)
        pygame.mixer.music.play(-1)

