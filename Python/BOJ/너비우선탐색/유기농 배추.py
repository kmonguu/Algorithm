# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력
# 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.


# 코드
import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  board[x][y] == 0                                    # 한 번 방문했던 땅은 다시 방문하지 않도록 0으로 초기화해준다.

  while queue:
    x, y = queue.popleft()

    for i in range(4):                                # 4방향으로 확인하여
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if board[nx][ny] == 0:
        continue
      if board[nx][ny] == 1:                           # 배추가 있다면
        board[nx][ny] = 0                              # 0으로 초기화해주고
        queue.append((nx, ny))                         # queue에 추가해준다.

testcase = int(input())
for _ in range(testcase):
  n, m, k = map(int, input().split())
  board = [[0]*m for _ in range(n)]                     # NxM 크기의 밭을 0으로 초기화

  for _ in range(k):                                    # 배추가 심어져있는 위치를 입력받고
    x, y = map(int, input().split())
    board[x][y] = 1                                     # 배추가 있는 곳은 1로 바꿔준다.

  cnt = 0
  for x in range(n):
    for y in range(m):
      if board[x][y] == 1:                              # NxM 크기의 밭에서 배추가 있다면 (1이 있다면)
        bfs(x, y)                                       # bfs 함수 실행
        cnt += 1                                        # 필요한 지렁이 수 +1

  print(cnt)
