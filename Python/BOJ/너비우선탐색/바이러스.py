# 어느날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력

# 코드
import sys
input = sys.stdin.readline

from collections import deque

def bfs(graph, start, visted):
  global cnt                                # 1번 컴퓨터와 연결된 컴퓨터의 갯수를 count하기 위해 global로 선언 

  queue = deque([start])                    # 시작 컴퓨터를 queue에 담아준다.
  visited[start] = True                     # 시작 컴퓨터는 방문했다는 표시로 True로 초기화

  while queue:                              # 큐가 빌 때까지 반복
    v = queue.popleft()
    
    for i in graph[v]:
      if not visited[i]:                    # visited[i]가 없다는 것은 그 컴퓨터를 방문하지 않았다는 의미이므로
        queue.append(i)                     # 해당 컴퓨터를 queue에 추가해주고
        visited[i] = True                   # visited를 True로 만들어준다.
        cnt += 1                            # 1번 컴퓨터와 연결된 컴퓨터의 갯수 +1
        
computer = int(input())
connect = int(input())
graph = [[] for _ in range(computer+1)]
visited = [False]*(computer+1)

for i in range(connect):
  a, b = map(int, input().split())          # 서로 연결된 컴퓨터들을 a, b로 입력받고
  graph[a].append(b)                        # 바이러스는 양방향으로 전파될 수 있다고 했으므로 두 방향에 대해 저장한다.
  graph[b].append(a)

cnt = 0
bfs(graph, 1, visited)
print(cnt)
