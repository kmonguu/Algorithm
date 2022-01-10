# 방향없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램

# 풀이
# 방향없는 양방향 그래프가 주어졌을 때, 연결 요소를 구하는 것은 즉, 몇 개의 구역으로 나누어져 있는지 구하면 된다.


# 코드
import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

cnt = 0
for i in range(1,n+1):                    # 노드 수만큼 반복
  if not visited[i]:                      # 노드 i를 방문하지 않았다면 다른 구역이 존재한다는 의미이므로
    bfs(graph, i, visited)                # 노드 i를 시작점으로 하여 bfs 함수 실행
    cnt += 1                              # 연결 요소의 개수 + 1
print(cnt)
