import random

from config import Config


# wallapple :: 방해물 사과
class WallApple():
    def __init__(self):

        # 방해물 갯수
        self.walCnt = 3
        self.x = []
        self.y = []

        for i in range(0, self.walCnt):
            self.x.append(random.randint(0, Config.CELLHEIGHT - 1))
            self.y.append(random.randint(0, Config.CELLHEIGHT - 1))
        self.color = Config.DARKPURPLE

    # 방해물 사과 생성 메소드
    def setNewLocation(self, snake):
        # 방해물 갯수 랜덤
        self.walCnt = random.randint(1, 3)
        # 방해물 위치 설정.
        for i in range(self.walCnt):
            self.x[i] = random.randint(0, Config.CELLWIDTH - 1)  # 0부터 31사이에 난수생성 및 x에 저장
            self.y[i] = random.randint(0, Config.CELLHEIGHT - 1)  # 0부터 23사이에 난수생성 및 y에 저장

        # 방해물 사과의 생성의 뱀과 겹칠시 사과 위치를 재설정하여 사과 생성
        for i in range(len(snake.wormCoords)):
            for j in range(self.walCnt):
                if (self.x[j] == snake.wormCoords[i]['x'] and self.y[j] == snake.wormCoords[i]['y']):
                    self.setNewLocation(snake)
