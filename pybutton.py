import os

import pygame as pg
from pygame_button import Button

os.environ["SDL_VIDEO_CENTERED"] = "1"
pg.init()

RED = (255, 0, 0)
BLUE = (204, 210, 240)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 180, 0)

# The button can be styled in a manner similar to CSS.
BUTTON_STYLE = {
    "hover_color": BLUE,
    "clicked_color": GREEN,
    "clicked_font_color": WHITE,
    "hover_font_color": BLACK,

}


class Control(object):
    def __init__(self, game, screen, rect, title, color, action=None):
        self.game = game
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.done = False
        self.fps = 60.0
        self.color = WHITE

        self.button = Button(rect, color, action, text=title, **BUTTON_STYLE)

    # def change_color(self):
    #     self.color = [random.randint(0, 255) for _ in range(3)]

    def event_loop(self):
        for event in self.game.event.get():
            self.button.check_event(event)

    def update(self):
        # self.event_loop()
        self.button.update(self.screen)
        self.clock.tick(self.fps)
