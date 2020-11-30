import pygame
class Config():
  FPS = 9
  MENU_FPS = 60

  # 화면크기
  WINDOW_WIDTH = 1200
  WINDOW_HEIGHT = 700
  CELLSIZE = 20 # 블록 크기
  assert WINDOW_WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
  assert WINDOW_HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
  CELLWIDTH = int(WINDOW_WIDTH / CELLSIZE) # 가로 블록 갯수
  CELLHEIGHT = int(WINDOW_HEIGHT / CELLSIZE) # 새로 블록 갯수

  # Colors
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  ORANGE = (255, 94, 19)
  PURPLE = (128, 0, 128)
  GOLD = (255, 215, 0)
  DARKRED = (139, 0, 0)
  DARKGREEN = (0, 155, 0)
  DARKGRAY = (40, 40, 40)
  DARKORANGE = (207, 83, 0)
  DARKPURPLE = (102, 0, 102)
  DARKGOLD = (204, 172, 0)
  BG_COLOR = BLACK


screen = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
