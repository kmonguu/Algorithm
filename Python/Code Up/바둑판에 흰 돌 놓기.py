#가로와 세로 19*19 바둑판을 만들기 위해 이중 for문으로 2차원 리스트를 만듦
#2차원 리스트를 생성하는 부분이 어려웠지만 공부하면서 2차원 리스트를 만드는 리스트 컴프리헨션을 알게 됨
#d = [[0 for j in range(20)] for i in range(20)]으로도 2차원 리스트를 한 번에 생성할 수 있다.

d = []
for i in range (20):     #0부터 19까지 for문
  d.append([])           #리스트 안에 다른 리스트 추가
  for j in range (20):   #0부터 19까지 이중 for문 
    d[i].append(0)       #리스트 안에 추가한 리스트에 0을 추가

n = int(input())         #흰 돌의 갯수 입력받음
for i in range(n):
  x, y = input().split() #흰 돌의 위치 x, y를 입력받음
  d[int(x)][int(y)] = 1  #흰 돌이 놓은 곳을 1로 바꾸어 저장한다.

for i in range(1, 20):
  for j in range(1, 20):
    print(d[i][j], end=' ')
  print()
