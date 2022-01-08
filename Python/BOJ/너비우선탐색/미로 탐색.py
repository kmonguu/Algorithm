# NxM 크기의 배열로 표현되는 미로가 있을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.


# 코드
from collections import deque

import sys
input = sys.stdin.readline

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):                                # 현재 위치에서 4방향으로 위치 확인
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:      # 미로 찾기 공간을 벗어난 경우 continue
        continue
      if board[nx][ny] == 0:                          # 미로에서 0은 이동할 수 없는 칸을 나타내므로 continue
        continue
      if board[nx][ny] == 1:                          # 미로에서 1은 갈 수 있는 칸이며 한 번도 방문한 적없다는 의미가 된다.
        board[nx][ny] = board[x][y] + 1               # 방문했다는 의미에서 현재 위치에서 +1값을 저장
        queue.append((nx, ny))

  return board[n-1][m-1]

n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int,input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
