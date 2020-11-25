from config import Config
import random


class Snake():
  UP = 'up'
  DOWN = 'down'
  LEFT = 'left'
  RIGHT = 'right'
  HEAD = 0
  TAIL = -1

  #snake 객체 생성자
  def __init__(self):
    #snake의 위치 랜덤 생성    가로 32픽셀 세로 24픽셀
    self.x = random.randint(5, Config.CELLWIDTH - 6)  # 5부터 28까지 난수생성 후 x좌표에 저장
    self.y = random.randint(5, Config.CELLHEIGHT - 6) # 5부터 18까지 난수생성 후 y좌표에 저장
    self.direction = self.RIGHT # 시작시 무조건 오른쪽으로 가도록 설정
    self.wormCoords = [ # 처음 뱀의 몸통
        {'x': self.x, 'y': self.y}, # 머리
        {'x': self.x - 1, 'y': self.y}, # 몸통
        {'x': self.x - 2, 'y': self.y} # 꼬리
    ]
    self.TAIL = len(self.wormCoords)-1

  def update(self, apple):
    # check if snake has eaten an apply 뱀의 위치 업데이트 메소드
    if self.wormCoords[self.HEAD]['x'] == apple.x and self.wormCoords[self.HEAD]['y'] == apple.y:   #뱀의 머리의 x좌표와 y좌표와 사과의 x좌표와 y좌표가 같을 경우, 즉 머리가 사과를 먹었을 경우
      if apple.getAppleColor().__eq__(Config.RED):
        apple.setNewLocation(self)    # 사과를 새로운 장소에 생성
        apple.setAppleNum()
        apple.setAppleDNum()
      elif apple.getAppleColor().__eq__(Config.ORANGE):
        apple.setNewLocation(self)    # 사과를 새로운 장소에 생성
        apple.setAppleNum()
        apple.setAppleDNum()
        self.doubleUpdate(apple)
        del self.wormCoords[-1]
      else:
        apple.setNewLocation(self)    # 사과를 새로운 장소에 생성
        apple.setAppleNum()
        apple.setAppleDNum()
        self.deleteUpdate()
        del self.wormCoords[-1]
    else:
      del self.wormCoords[-1]  # remove worms tail segment # 뱀의 꼬리부분을 삭제

    # move the worm by adding a segment in the direction it is moving
    #뱀의 움직임을 구현
    if self.direction == self.UP: # 키보드 위쪽을 눌렀을 시 원래머리 위쪽에 새로운 머리를 생성
      newHead = {'x': self.wormCoords[self.HEAD]['x'],
                'y': self.wormCoords[self.HEAD]['y'] - 1}
    elif self.direction == self.DOWN: # 키보드 아래쪽을 눌렀을 시 원래머리 아래에 새로운 머리를 생성
      newHead = {'x': self.wormCoords[self.HEAD]['x'],
                'y': self.wormCoords[self.HEAD]['y'] + 1}
    elif self.direction == self.LEFT: # 키보드 왼쪽을 눌렀을 시 원래머리 왼쪽에 새로운 머리를 생성
      newHead = {'x': self.wormCoords[self.HEAD]['x'] - 1,
                'y': self.wormCoords[self.HEAD]['y']}
    elif self.direction == self.RIGHT: # 키보드 오른쪽을 눌렀을 시 원래머리 오른쪽에 새로운 머리를 생성
      newHead = {'x': self.wormCoords[self.HEAD]['x'] + 1,
                'y': self.wormCoords[self.HEAD]['y']}
    self.wormCoords.insert(0, newHead) # 뱀의 몸통 리스트 첫번째에 새로운 머리를 insert

  def doubleUpdate(self, apple):
    if self.direction == self.UP:
      newNext = {'x': self.wormCoords[self.HEAD]['x'],
                 'y': self.wormCoords[self.HEAD]['y'] - 1}
      newHead = {'x': self.wormCoords[self.HEAD]['x'],
                 'y': self.wormCoords[self.HEAD]['y'] - 2}

    elif self.direction == self.DOWN:
      newNext = {'x': self.wormCoords[self.HEAD]['x'],
                 'y': self.wormCoords[self.HEAD]['y'] + 1}
      newHead = {'x': self.wormCoords[self.HEAD]['x'],
                 'y': self.wormCoords[self.HEAD]['y'] + 2}

    elif self.direction == self.LEFT:
      newNext = {'x': self.wormCoords[self.HEAD]['x'] - 1,
                 'y': self.wormCoords[self.HEAD]['y']}
      newHead = {'x': self.wormCoords[self.HEAD]['x'] - 2,
                 'y': self.wormCoords[self.HEAD]['y']}

    elif self.direction == self.RIGHT:
      newNext = {'x': self.wormCoords[self.HEAD]['x'] + 1,
                 'y': self.wormCoords[self.HEAD]['y']}
      newHead = {'x': self.wormCoords[self.HEAD]['x'] + 2,
                 'y': self.wormCoords[self.HEAD]['y']}


    self.wormCoords.insert(0, newNext)
    self.wormCoords.insert(0, newHead)

  def deleteUpdate(self):
    del self.wormCoords[-1]