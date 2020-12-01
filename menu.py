from random import randint

import pygame

from config import Config, screen

pygame.font.init()


class Button:
    def __init__(self, window, x, y, width, height, text='', text_size=10):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
        self.color = Config.WHITE
        self.text_color = Config.BLACK
        self.rect = (self.x, self.y, self.width, self.height)
        self.font = pygame.font.SysFont('Comic Sans MS', self.text_size)

    def clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()

        if mouse_press[0]:
            if mouse_x > self.x and mouse_x < self.x + self.width:
                if mouse_y > self.y and mouse_y < self.y + self.height:
                    return True

    def render(self):
        pygame.draw.rect(self.window, self.color, self.rect)
        text = self.font.render(self.text, True, self.text_color)
        x = self.x
        y = self.y + 25
        self.window.blit(text, (x, y))


class Menu:
    def __init__(self):
        self.title_size = 100
        self.title_color = [255, 255, 255]
        self.title_height = 250
        self.timer = 0
        self.running = True
        self.btn_width = 250
        self.btn_height = 125
        self.play_button = Button(screen, Config.WINDOW_WIDTH / 2 - self.btn_width / 2, Config.WINDOW_HEIGHT / 2,
                                  self.btn_width, self.btn_height, text='Single Player', text_size=41)
        self.play_button.color = Config.LIGHTGREEN
        self.show_music = False

    def message(self, text, text_size, color, height):
        font = pygame.font.SysFont('Comic Sans MS', text_size)
        screen_text = font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(Config.WINDOW_WIDTH / 2, height))
        screen.blit(screen_text, text_rect)

    def logic(self):
        self.timer += 1

        if self.timer % 10 == 0:
            self.title_color[0] = randint(0, 255)
            self.title_color[1] = randint(0, 255)
            self.title_color[2] = randint(0, 255)

        if self.play_button.clicked():
            self.running = False


    def render(self):
        self.message("Welcome to", self.title_size - 10, (0, 0, 0), self.title_height - 100)
        self.message("Snake Game", self.title_size, self.title_color, self.title_height)

        self.play_button.render()


