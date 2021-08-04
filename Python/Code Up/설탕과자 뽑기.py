# 생각해야 할 변수가 많아서 고민을 오래한 문제
# 막대의 길이만큼 좌표를 찍는 부분을 이해하는데 어려웠음

h, w = map(int, input().split())

pan = []                                    # 격자판을 입력받은 가로 h, 세로 w를 이용하여 이중 for문으로 생성한다.
for i in range(h+1):
  pan.append([])
  for j in range(w+1):
    pan[i].append(0)


n = int(input())                            # 막대의 갯수 n을 입력받는다.
for i in range(n):
  l, d, x, y = map(int, input().split())    # n만큼 l(막대의 길이), d(방향), x, y 좌표를 입력받는다.
  if d == 0:                                # d가 0(가로)일 경우 if문
    for j in range(l):                      # 막대 l의 길이 만큼 for문 반복
      pan[x][y+j] = 1                       # 판에서 y좌표에 막대 길이만큼 1로 변경하여 막대를 표시
  else:
    for j in range(l):
      pan[x+j][y] = 1                       # 판에서 x좌표에 막대 길이만큼 1로 변경하여 막대를 표시

for i in range(1, h+1):
  for j in range(1, w+1):
    print(pan[i][j], end=' ')
  print()
