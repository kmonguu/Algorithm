# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 
# 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 
# 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력

# 예제
# N = 5  M = 5  R =  1
# graph = [[1 4], [1 2], [2 3], [2 4], [3 4]]

# 출력
# 정점 1번에서 정점 2번을 방문한다. 정점 2번에서 정점 3번을 방문한다. 정점 3번에서 정점 4번을 방문한다. 정점 5번은 정점 1번에서 방문할 수 없다.
# 1
# 2
# 3
# 4
# 0


# 메모리 초과 코드
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())

edge_info = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for _ in range(m):
  u, v = map(int, input().split())
  edge_info[u].append(v)
  edge_info[v].append(u)

def dfs(n):
  global count 
  visited[n] = count
  edge_info[n].sort()
  for i in edge_info[n]:
    if not visited[i]:
      count += 1
      dfs(i)
      
dfs(r)
for cnt in range(1, n+1):
  print(visited[cnt])
