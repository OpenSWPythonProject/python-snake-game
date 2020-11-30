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
    self.doubleDeleteNum = 0

  # 사과 생성 메소드
  def setNewLocation(self, snake):
    self.x = random.randint(0, Config.CELLWIDTH - 1) # 0부터 31사이에 난수생성 및 x에 저장
    self.y = random.randint(0, Config.CELLHEIGHT - 1) # 0부터 23사이에 난수생성 및 y에 저장
    
    #사과의 생성의 뱀과 겹칠시 사과 위치를 재설정하여 사과 생성
    for i in range(len(snake.wormCoords)):
      if(self.x == snake.wormCoords[i]['x'] and self.y == snake.wormCoords[i]['y']):
        self.setNewLocation(snake)

  # 사과 아이템의 종류에 따라 색상을 다르게 설정
  def setAppleColor(self, color):
    self.color = color
  # 현재 보이는 사과의 색상을 반환
  def getAppleColor(self):
    return self.color

  # DoubleApple 아이템이 생성될 확률을 지정
  def setAppleNum(self): #1/3 확률 0~2중 1이랑 같을시
    self.doubleNum = random.randint(0, 3)
  # DoubleApple 아이템의 확률 수를 반환
  def getAppleNum(self):
    return self.doubleNum

  # DeleteApple 아이템이 생성될 확률을 지정
  def setAppleDNum(self): #1/3 확률 0~2중 1이랑 같을시
    self.deleteNum = random.randint(0, 3)
  # DeleteApple 아이템의 확률 수를 반환
  def getAppleDNum(self):
    return self.deleteNum

 # DoubleDeleteApple 아이템이 생성될 확률을 지정
  def setAppleDoubleDNum(self): #1/3 확률 0~2중 1이랑 같을시
    self.doubleDeleteNum = random.randint(0, 3)
  # DoubleDeleteApple 아이템의 확률 수를 반환
  def getAppleDoubleDNum(self):
    return self.doubleDeleteNum

  #사과의 확률을 바꾸고 싶다면 여기서 각 랜덤 값의 마지막 값을 바꿔주면 됨