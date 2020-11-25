import sys

import pygame
import random

from apple import Apple
from config import Config, screen
from menu import Menu
from snake import Snake


class Game():
  def __init__(self):
    pygame.init() #pygame에 포함된 모듈들을 한꺼번에 초기화, 초기화 실패시 성공 및 실패 모듈 횟수를 튜플로 리턴
    self.screen = screen
    self.clock = pygame.time.Clock() # 시간 트래킹 객체 생성
    self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18) # 폰트 (파일이름, 글자 크기)
    pygame.display.set_caption('Snake') #윈도우 창에 게임 이름 표시
    self.apple = Apple()  # 아이템 객체 할당
    self.snake = Snake()  # 뱀 객체 할당

  def drawGrid(self): # 격자 그리기 매소드
    # draw vertical lines
    for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE): # 720 한칸에 20
      pygame.draw.line(self.screen, Config.DARKGRAY,  # 파라미터:(윈도우객체, 색, 시작지점, 종료지점, 너비)
                       (x, 0), (x, Config.WINDOW_HEIGHT))
    # draw horizontal lines
    for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE): # 480 한칸에 20
      pygame.draw.line(self.screen, Config.DARKGRAY,  # 파라미터:(윈도우객체, 색, 시작지점, 종료지점, 너비)
                       (0, y), (Config.WINDOW_WIDTH, y))

  def drawWorm(self):
    for coord in self.snake.wormCoords: # 뱀 객체 리스
      x = coord['x'] * Config.CELLSIZE
      y = coord['y'] * Config.CELLSIZE
      wormSegmentReact = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE) # 사각형 객체를 생성하는 클래스 (x좌표,y좌표,너비,너비)
      pygame.draw.rect(self.screen, Config.DARKGREEN, wormSegmentReact) # 파라미터: (윈도우객체, 색상, 사각형객체)
      wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, Config.CELLSIZE - 8, Config.CELLSIZE - 8) # 안쪽 사각형 생성
      pygame.draw.rect(self.screen, Config.GREEN, wormInnerSegmentRect)

  def drawApple(self):
    # print("기본 사과 그리기")
    x = self.apple.x * Config.CELLSIZE
    y = self.apple.y * Config.CELLSIZE
    self.apple.setAppleColor(Config.RED)
    appleRect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE) # 사각형 객체를 생성하는 클래스 (x좌표,y좌표,너비,너비)
    pygame.draw.rect(self.screen, Config.DARKRED, appleRect) # 파라미터: (윈도우객체, 색상, 사각형객체)
    appleInnerRect = pygame.Rect(x + 4, y + 4, Config.CELLSIZE - 8, Config.CELLSIZE - 8) # 안쪽 사각형 생성
    pygame.draw.rect(self.screen, Config.RED, appleInnerRect)

  def drawDoubleApple(self):
    # print("두배 사과 그리기")
    x = self.apple.x * Config.CELLSIZE
    y = self.apple.y * Config.CELLSIZE
    self.apple.setAppleColor(Config.ORANGE)
    appleRect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE) # 사각형 객체를 생성하는 클래스 (x좌표,y좌표,너비,너비)
    pygame.draw.rect(self.screen, Config.DARKORANGE, appleRect) # 파라미터: (윈도우객체, 색상, 사각형객체)
    appleInnerRect = pygame.Rect(x + 4, y + 4, Config.CELLSIZE - 8, Config.CELLSIZE - 8) # 안쪽 사각형 생성
    pygame.draw.rect(self.screen, Config.ORANGE, appleInnerRect)

  def drawDeleteApple(self):
    # print("기본 사과 그리기")
    x = self.apple.x * Config.CELLSIZE
    y = self.apple.y * Config.CELLSIZE
    self.apple.setAppleColor(Config.PURPLE)
    appleRect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE) # 사각형 객체를 생성하는 클래스 (x좌표,y좌표,너비,너비)
    pygame.draw.rect(self.screen, Config.DARKPURPLE, appleRect) # 파라미터: (윈도우객체, 색상, 사각형객체)
    appleInnerRect = pygame.Rect(x + 4, y + 4, Config.CELLSIZE - 8, Config.CELLSIZE - 8) # 안쪽 사각형 생성
    pygame.draw.rect(self.screen, Config.PURPLE, appleInnerRect)

  def drawScore(self, score):
    scoreSurf = self.BASICFONT.render('Score: %s' % (score), True, Config.WHITE) # 윈도우 위에 새로운 표면에 텍스트 렌더 (텍스트, 안티얼라이싱, 색, 백그라운드)
    scoreRect = scoreSurf.get_rect() # 렌더된 텍스트의 사이즈와 오프셋 리턴
    scoreRect.topleft = (Config.WINDOW_WIDTH - 120, 10)
    self.screen.blit(scoreSurf, scoreRect)

  def draw(self): # 렌더링 메소드
    self.screen.fill(Config.BG_COLOR) #배경색
    # in here well draw snake, grid, apple, scroe
    self.drawGrid()
    self.drawWorm()
    if(len(self.snake.wormCoords) - 3) >= 3 and (len(self.snake.wormCoords) - 3) <= 5:
      if self.apple.getAppleNum() == 1:
        self.drawDoubleApple()
      else:
        self.drawApple()
    elif(len(self.snake.wormCoords) - 3) > 5 and (len(self.snake.wormCoords) - 3) <= 8:
      if self.apple.getAppleNum == 1:
        self.drawDoubleApple()
      elif self.apple.getAppleDNum() == 1:
        self.drawDeleteApple()
      else:
        self.drawApple()
    else:
      self.drawApple() 
    
    self.drawScore(len(self.snake.wormCoords) - 3) # 뱀 몸통 -3으로 점수계
    pygame.display.update() # 윈도우의 부분적인 업데이트를 가능하게 하는 메소
    self.clock.tick(Config.FPS) # 시간 업데이트 매개변수: (프레임레이트) 단위 ms

  def checkForKeyPress(self):
    if len(pygame.event.get(pygame.QUIT)) > 0: # 이벤트 리스트가 0보다 크면
      pygame.quit()

    keyUpEvents = pygame.event.get(pygame.KEYUP)

    if len(keyUpEvents) == 0:
      return None
    if keyUpEvents[0].key == pygame.K_ESCAPE:
      pygame.quit()
      quit()
    return keyUpEvents[0].key

  def handleKeyEvents(self, event):
    if(event.key == pygame.K_LEFT or event.key == pygame.K_a) and (self.snake.direction != self.snake.RIGHT):
      self.snake.direction = self.snake.LEFT
    elif(event.key == pygame.K_RIGHT or event.key == pygame.K_d) and (self.snake.direction != self.snake.LEFT):
      self.snake.direction = self.snake.RIGHT
    elif(event.key == pygame.K_UP or event.key == pygame.K_w) and (self.snake.direction != self.snake.DOWN):
      self.snake.direction = self.snake.UP
    elif(event.key == pygame.K_DOWN or event.key == pygame.K_s) and (self.snake.direction != self.snake.UP):
      self.snake.direction = self.snake.DOWN
    elif event.key == pygame.K_ESCAPE:
      pygame.quit()

  def resetGame(self):
    del self.snake
    del self.apple
    self.snake = Snake()
    self.apple = Apple()

    return True

  def drawPressKeyMgs(self):
    pressKeySurf = self.BASICFONT.render('Press a key UP to play again', True, Config.WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (Config.WINDOW_WIDTH - 250, Config.WINDOW_HEIGHT - 30)
    self.screen.blit(pressKeySurf, pressKeyRect)

  def isGameOver(self):
    if(self.snake.wormCoords[self.snake.HEAD]['x'] == -1 or
            self.snake.wormCoords[self.snake.HEAD]['x'] == Config.CELLWIDTH or
            self.snake.wormCoords[self.snake.HEAD]['y'] == -1 or
            self.snake.wormCoords[self.snake.HEAD]['y'] == Config.CELLHEIGHT):
      return self.resetGame()
    for wormBody in self.snake.wormCoords[1:]:
      if wormBody['x'] == self.snake.wormCoords[self.snake.HEAD]['x'] and wormBody['y'] == self.snake.wormCoords[self.snake.HEAD]['y']:
        return self.resetGame()

  def menu(self):
    main_menu = Menu()

    while main_menu.running:
      self.clock.tick(60)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          global running
          main_menu.running = False
          running = False

      main_menu.logic()
      # back = pygame.image.load("../back.png")
      screen.fill(Config.WHITE)
      # screen.blit(back, (0,0))
      main_menu.render()
      pygame.display.update()


  def showStartScreen(self):
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Snake!', True, Config.WHITE, Config.DARKGREEN)
    titleSurf2 = titleFont.render('Snake!', True, Config.GREEN)
    degrees1 = 0
    degrees2 = 0
    while True:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          return
      self.screen.fill(Config.BG_COLOR)

      rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
      rotatedRect1 = rotatedSurf1.get_rect()
      rotatedRect1.center = (Config.WINDOW_WIDTH / 2, Config.WINDOW_HEIGHT / 2)
      self.screen.blit(rotatedSurf1, rotatedRect1)

      rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
      rotatedRect2 = rotatedSurf2.get_rect()
      rotatedRect2.center = (Config.WINDOW_WIDTH / 2, Config.WINDOW_HEIGHT / 2)
      self.screen.blit(rotatedSurf2, rotatedRect2)

      self.drawPressKeyMgs()

      pygame.display.update()
      self.clock.tick(Config.MENU_FPS)
      degrees1 += 1  # rotate by 3degrees each frame
      degrees2 += 2  # rotate by 7degrees each frame

  def displayGameOver(self):
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, Config.WHITE)
    overSurf = gameOverFont.render('Over', True, Config.WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (Config.WINDOW_WIDTH / 2, 10)
    overRect.midtop = (Config.WINDOW_WIDTH / 2, gameRect.height + 10 + 25)
    self.screen.blit(gameSurf, gameRect)
    self.screen.blit(overSurf, overRect)

    self.drawPressKeyMgs()
    pygame.display.update()
    pygame.time.wait(500)

    self.checkForKeyPress()  # clear out any key presses in the event queue
    while True:
      if self.checkForKeyPress():
        pygame.event.get()  # clear event queue
        return

  def run(self):
    self.menu()
    self.showStartScreen()

    while True:
      self.gameLoop()
      self.displayGameOver()
      self.menu()
      self.showStartScreen()

  def gameLoop(self):
    while True:  # main game loop
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          self.handleKeyEvents(event)

      self.snake.update(self.apple)
      self.draw()
      if self.isGameOver():
        break
