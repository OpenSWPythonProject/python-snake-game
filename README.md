# 공개SW실무 : 프로젝트 스네이크 

### Tech-Stack (Dependencies)

- Python
- pygame
- pygame_button

### 아이템 추가

DoubleApple 아이템 (파란색 사과)
- 1, 2, 3라운드에서 33.3%의 확률로 등장, 습득 시 몸길이 2 증가

DeleteApple 아이템 (보라색 사과)
- 2, 3라운드에서 22.2%의 확률로 등장, 습득 시 몸길이 1 감소

DoubleDeleteApple 아이템 (금색 사과)
- 3라운드 이후부터 14.8%의 확률로 등장, 습득 시 몸길이 2 감소

wallapple (갈색 = 썩은 사과)
- 플레이어(snake)의 머리(HEAD)가 wallapple에 닿으면 게임오버로 판단 됨
   (isGameOver() 함수가 이를 판단)
- apple을 먹으면 1~3개에 랜덤한 개수의 wallapple이 랜덤한 위치에 생성



### Screenshot

<img src="https://media.giphy.com/media/Xy771jkY0ngo1Nxfvj/giphy.gif" />
