# NxN 크기의 정사각형 모양의 지도에서 1은 집이 있는 곳을, 0은 집이 없는 곳을 의미한다.
# 이 지도를 가지고 연결된 집들에게 단지를 정의하고, 단지에 번호를 붙이려고 할 때 지도를 입력받아 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬 후 출력

# 풀이
# 탐색을 시작할 시작점이 각각 단지별로 다르기 때문에 NxN 크기의 지도를 모두 돌면서 1일 때 탐색을 시작
# 탐색 중 1인 부분은 0으로 바꿔서 다시 탐색하지 않도록하고 1인 부분을 탐색할 때마다 카운트하여 단지의 집의 수를 세어 오름차순으로 정렬 후 출력한다.

# 코드
import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  cnt = 1                                         # 단지 별 집의 수를 카운트하는 변수

  queue = deque()
  queue.append((x, y))
  board[x][y] = 0                                 # 탐색했던 집은 0으로 초기화

  while queue:
    x, y = queue.popleft()

    for i in range(4):                            # 4방향으로 확인
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if board[nx][ny] == 0:
        continue 
      if board[nx][ny] == 1:                      # 1이 있다면
        board[nx][ny] = 0                         # 0으로 바꿔주고
        queue.append((nx, ny))                    # 큐에 추가 후
        cnt += 1                                  # 카운트한다.

  return cnt

n = int(input())
board = []
for _ in range(n):
  board.append(list(map(int, input().strip())))

result = []
for x in range(n):
  for y in range(n):
    if board[x][y] == 1:                          # NxN 크기의 지도를 모두 돌아보고 1이 있다면 
      result.append(bfs(x, y))                    # 함수 실행하고 반환값을 result에 저장

result.sort()                                     # result에 저장된 각 단지에 속하는 집의 수를 오름차순으로 정렬
print(len(result))
for r in result:
  print(r)
