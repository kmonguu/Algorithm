# 쩰리는 항상 NxN 정사각형의 가장 왼쪽, 가장 위에서 출발한다.
# 쩰리가 이동 가능한 방향은 오른쪽과 아래 뿐이다.
# 쩰리가 가장 오른쪽, 가장 아래 칸에 도달하는 순간 쩰리는 승리한다.
# 쩰리가 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다.


# 코드
import sys
input = sys.stdin.readline

from collections import deque

dx = [1, 0]
dy = [0, 1]

def bfs(x, y, visited):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  while queue:
    x, y = queue.popleft()
    if board[x][y] == -1:
      return 'HaruHaru'

    for i in range(2):
      nx = x + dx[i] * board[x][y]
      ny = y + dy[i] * board[x][y]

      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
        visited[nx][ny] = True
        queue.append((nx, ny))

  return 'Hing'
    
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

print(bfs(0, 0, visited))
