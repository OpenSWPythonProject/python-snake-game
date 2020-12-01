# 공개SW실무 : 프로젝트 스네이크 

### Tech-Stack (Dependencies)

- Python
- pygame
- pygame_button



플레이어(snake)
- 시작 길이는 3, 시작 방향은 Right
- 플레이어가 방향키를 사용해 상, 하, 좌, 우로 움직일 수 있음
- 사과를 먹을 때마다 몸의길이(cell)가 1씩(1칸씩) 늘어남
- 뱀의 HEAD가 자신의 몸통, 독사과, 혹은 프레임에 닿을시 게임오버

### 아이템 추가

DoubleApple 아이템 (파란색 사과)
- 1, 2, 3라운드에서 33.3%의 확률로 등장, 습득 시 몸길이 2 증가

DeleteApple 아이템 (보라색 사과)
- 2, 3라운드에서 22.2%의 확률로 등장, 습득 시 몸길이 1 감소

DoubleDeleteApple 아이템 (금색 사과)
- 3라운드 이후부터 14.8%의 확률로 등장, 습득 시 몸길이 2 감소

wallapple (갈색 = 썩은 사과)
- 플레이어(snake)의 머리(HEAD)가 wallapple에 닿으면 게임오버로 판단 됨
- apple을 먹으면 1~3개에 랜덤한 개수의 wallapple이 랜덤한 위치에 생성



### Screenshot

<img src="https://media.giphy.com/media/Xy771jkY0ngo1Nxfvj/giphy.gif" />
