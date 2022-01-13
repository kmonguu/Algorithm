# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어지낟. 섬의 개수를 세는 프로그램을 작성
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형으로 하나의 섬으로 간주한다.

# 풀이
# 가로, 세로, 대각선 총 8개의 방향을 고려하여 섬을 의미하는 1이 있는 위치부터 탐색을 시작하여 탐색한 섬은 재탐색을 방지하기 위해 0으로 바꿔준다.

# 코드
import sys
input = sys.stdin.readline

from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def bfs (x, y):
  queue = deque()
  queue.append((x,y))
  board[x][y] = 0

  while queue:
    x, y = queue.popleft()

    for i in range(8):
      nx, ny = x + dx[i], y + dy[i]

      if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
        board[nx][ny] = 0 
        queue.append((nx, ny))

while True:
  w, h = map(int, input().split())

  if w == 0 and h == 0:
    break

  board = [list(map(int, input().split())) for _ in range(h)]

  cnt = 0
  for x in range(h):
    for y in range(w):
      if board[x][y] == 1:
        bfs(x, y)
        cnt += 1
  print(cnt)
