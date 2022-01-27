# 1xN 크기의 미로의 각 칸에는 정수가 하나 쓰여있다.
# i번째 칸에 쓰인 수를 Ai라고 했을 때, 오른쪽으로 떨어진 칸으로 1~i 만큼 한 번에 점프할 수 있다.
# 현재 미로의 가장 왼쪽 끝에 있고, 가장 오른쪽 끝으로 가려고 할 때, 최소 몇 번 점프를 해야 갈 수 있는지 출력

# 스스로 못 푼 문제의 정답 코드

import sys
input = sys.stdin.readline

from collections import deque

def bfs(x):
  queue = deque([x])
  visited[x] = True

  while queue:
    x = queue.popleft()

    for d in range(1, maps[x] + 1):
      nx = x + d
      
      if nx < n and not visited[nx]:
        visited[nx] = visited[x] + 1
        queue.append(nx)

n = int(input())
maps = list(map(int, input().split()))
visited = [False] * n
bfs(0)
print(visited[n - 1] - 1 if visited[n - 1] else -1)
