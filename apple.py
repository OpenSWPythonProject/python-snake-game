import random
from config import Config


class Apple():
  def __init__(self):
    # self.setNewLocation()
    self.x = random.randint(0, Config.CELLWIDTH - 1)
    self.y = random.randint(0, Config.CELLHEIGHT - 1)
    self.color = Config.RED
    self.doubleNum = 0
    self.deleteNum = 0

  # 사과 생성 메소드
  def setNewLocation(self, snake):
    self.x = random.randint(0, Config.CELLWIDTH - 1) # 0부터 31사이에 난수생성 및 x에 저장
    self.y = random.randint(0, Config.CELLHEIGHT - 1) # 0부터 23사이에 난수생성 및 y에 저장
    
    #사과의 생성의 뱀과 겹칠시 사과 위치를 재설정하여 사과 생성
    for i in range(len(snake.wormCoords)):
      if(self.x == snake.wormCoords[i]['x'] and self.y == snake.wormCoords[i]['y']):
        self.setNewLocation(snake)

  def setAppleColor(self, color):
    self.color = color

  def getAppleColor(self):
    return self.color

  def setAppleNum(self): #2/5 확률 0~4중 1,3이랑 같을시
    self.doubleNum = random.randint(0, 5)

  def getAppleNum(self):
    return self.doubleNum

  def setAppleDNum(self): #1/3 확률 0~2중 1이랑 같을시
    self.deleteNum = random.randint(0, 3)

  def getAppleDNum(self):
    return self.deleteNum