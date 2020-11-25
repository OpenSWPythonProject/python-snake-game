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
        x = self.x + 20
        y = self.y + 45
        self.window.blit(text, (x, y))


class Menu:
    def __init__(self):
        self.title_size = 100
        self.title_color = [255, 255,255]
        self.title_pos = (Config.WINDOW_WIDTH - self.title_size * 7.8, 200)
        self.timer = 0
        self.running = True
        self.btn_width = 250
        self.btn_height = 125
        self.play_button = Button(screen, Config.WINDOW_WIDTH / 2 - self.btn_width / 2, Config.WINDOW_HEIGHT / 2,
                                  self.btn_width, self.btn_height, text='Single Player', text_size=47)
        self.controls_button = Button(screen, Config.WINDOW_WIDTH / 2 - self.btn_width / 2,
                                      Config.WINDOW_HEIGHT / 2 + 150, self.btn_width, self.btn_height, text="Controls",
                                      text_size=70)
        self.play_button.color = Config.GREEN
        self.show_controls = False

    def message(self, text, text_size, color, position):
        font = pygame.font.SysFont('Comic Sans MS', text_size)
        screen_text = font.render(text, True, color)
        screen.blit(screen_text, position)

    def logic(self):
        self.timer += 1

        if self.timer % 10 == 0:
            self.title_color[0] = randint(0, 255)
            self.title_color[1] = randint(0, 255)
            self.title_color[2] = randint(0, 255)

        if self.play_button.clicked():
            self.running = False

        if self.controls_button.clicked():
            if self.show_controls:
                self.show_controls = False
            if self.show_controls == False:
                self.show_controls = True

    def render(self):
        self.message("Welcome to", 40, (0, 0, 0), (Config.WINDOW_WIDTH / 2 - 40 * 2.1, self.title_pos[1] - 50))
        self.message("Python.io", self.title_size, self.title_color, self.title_pos)

        self.play_button.render()
        self.controls_button.render()

        if self.show_controls:
            self.message("Single Player: Arrow keys", 30, (255, 255, 255),
                         (Config.WINDOW_WIDTH / 2 - 500, Config.WINDOW_HEIGHT / 2))
