# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램
# 단, 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.


# 풀이
# DFS는 최상위 노드부터 시작하여 하위노드까지 하나의 방향으로 깊게 탐색한 뒤, 다시 올라가서 다른 노드를 동일한 방법으로 깊게 탐색하는 방법이다.
# 스택과 재귀를 이용하여 문제를 풀 수 있다.
# BFS의 경우 큐를 이용하여 풀 수 있다.

# 코드
from collections import deque

import sys
input = sys.stdin.readline

def dfs(n):                              # 깊이우선탐색
  print(n, end=' ')
  visited[n] = True
  for i in graph[n]:
    if not visited[i]:
      dfs(i)

def bfs(n):                              # 너비우선탐색
  queue = deque([n])
  visited[n] = True

  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

n,m,v = map(int, input().split())       # 정점의 개수 : n, 간선의 개수 : m, 탐색을 시작할 정점의 번호 : v 
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):                      # 간선의 개수 m 만큼 간선이 연결하는 두 정점의 번호가 주어진다.
  a, b = map(int, input().split())      
  graph[a].append(b)                    # 양방향 그래프이므로 두 정점 모두에 간선을 추가한다.
  graph[b].append(a)

for i in range(1, n+1):                 # 방문할 수 있는 정점이 여러 개인 경우, 정점 번호가 작은 것을 먼저 방문하기 위해 정렬해준다.
  graph[i].sort()                 


dfs(v)
visited = [False]*(n+1)                 # 노드의 방문 여부를 저장하는 visied는 dfs에서 사용하고 다시 bfs에서 사용하기 위해 초기화해준다.
print()
bfs(v)
