import pygame

from config import Config, screen


class Music:
    def __init__(self):
        pygame.mixer.init()

    def playTheme(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load('res/themeMusic.mp3')
        pygame.mixer.music.play(-1)

    def playInGameMusic(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load('res/inGameMusic.mp3')
        pygame.mixer.music.play(-1)

    def drawText(self):
        font = pygame.font.Font(None, 25)
        text = font.render("Music off", True. Config.GREEN)
        text_rect = text.get_rect(center=(Config.WINDOW_WIDTH/2, Config.WINDOW_HEIGHT/2 ))
        screen.blit(text, text_rect)
