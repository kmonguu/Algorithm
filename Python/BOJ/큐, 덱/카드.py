# N장의 카드가 차례로 1부터 N까지 순서대로 놓여있다. 아래의 과정을 카드가 한 장 남을 때까지 반복한다.
# 우선 제일 위에 있는 카드를 바닥에 버린다. 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 마지막에 남게 되는 카드 번호를 출력한다.


# 예시
# N이 4일 때, 카드는 1234 순서로 놓이게 된다. 
# 반복 규칙에 따라 제일 위의 카드 1은 버리고 234가 남는다. 여기서 그다음 제일 위에 있는 카드 2를 가장 밑으로 옮기면 342가 된다.
# 342에서 다시 3을 버리면 42, 42에서 그다음 위에 있는 카드 4를 밑으로 옮기면 24가 된다. 
# 다시 24에서 제일 위의 카드 2를 버리면 4라는 카드가 한장이 남고 반복이 종료된다.


# 코드
from collections import deque

queue = deque()

N = int(input())
for card in range(1, N+1):
  queue.append(card)

while 1 < len(queue):                     # 카드가 한장이 남을 때까지 반복해야하므로 큐의 길이가 1보다 큰 경우를 조건으로 한다.
  queue.popleft()                         # 가장 위에 놓인 카드를 버리기 위한 popleft()
  queue.append(queue.popleft())           # 그다음 위에 놓은 카드를 꺼내고 바로 제일 아래로 append하면 제일 위에서 아래로 카드를 옮길 수 있다.
print(*queue)




# 다른 방법 : 리스트 컴프리헨션을 사용한 코드
from collections import deque

N = int(input())
queue = deque([card for card in range(1, N + 1)])

while len(queue) > 1:
  queue.popleft()
  queue.append(queue.popleft())

print(*queue)
