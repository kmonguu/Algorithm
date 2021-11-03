# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램

# push_front X : 정수 X를 덱의 앞에 추가
# push_back X : 정수 X의 덱의 뒤에 추가
# pop_front : 덱의 가장 앞에 있는 정수를 빼고 출력(먄약 큐가 비어있을 경우 -1 출력)
# pop_back : 덱의 가장 뒤에 있는 정수를 빼고 출력(먄약 큐가 비어있을 경우 -1 출력)
# size : 덱에 들어있는 정수의 개수를 출력
# empty : 덱이 비어있으면 1을, 아니면 0을 출력.
# front : 덱의 가장 앞에 있는 정수를 출력(만약 큐가 비어있을 경우 -1 출력)
# back : 덱의 가장 뒤에 있는 정수를 출력(만약 큐가 비어있을 경우 -1 출력)

# 코드

from collections import deque
import sys
input = sys.stdin.readline

queue = deque()
for _ in range(int(input())):
  order = input().split()

  if order[0] == 'push_front':
    queue.appendleft(order[1])

  elif order[0] == 'push_back':
    queue.append(order[1])

  elif order[0] == 'pop_front':
    if queue:
      print(queue.popleft())
    else:
      print(-1)

  elif order[0] == 'pop_back':
    if queue:
      print(queue.pop())
    else:
      print(-1)

  elif order[0] == 'size':
    print(len(queue))

  elif order[0] == 'empty':
    if queue:
      print(0)
    else:
      print(1)

  elif order[0] == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)

  elif order[0] == 'back':
    if queue:
      print(queue[-1])
    else:
      print(-1)
