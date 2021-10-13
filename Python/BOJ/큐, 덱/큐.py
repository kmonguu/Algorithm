# 큐를 구현하고 총 여섯가지의 명령을 처리하는 프로그램

# push x : 정수 x를 큐에 넣는 연산
# pop : 큐에서 가장 앞에 있는 정수를 빼고 출력(먄약 큐가 비어있을 경우 -1 출력)
# size : 큐에 들어있는 정수의 개수를 출력
# empty : 큐가 비어있으면 1, 아니면 0출력
# front : 큐의 가장 앞에 있는 정수를 출력(만약 큐가 비어있을 경우 -1 출력)
# back : 큐의 가장 뒤에 있는 정수를 출력(만약 큐가 비어있을 경우 -1 출력)


# 풀이
# 처음 큐를 리스트로 구현하여 풀었지만 시간초과 발생
# collections 모듈을 이용하여 deque 자료형을 생성하였다.
# deque는 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형이다. 양방향이기 때문에 스택(Stack)처럼 써도 되고 큐(Queue)처럼 써도 된다.


#코드
from collections import deque
import sys
input = sys.stdin.readline

queue = deque([])
for _ in range(int(input())):
  order = input().split()

  if order[0] == 'push':              # push
    queue.append(order[1])

  elif order[0] == 'pop':             # pop
    if queue:    
      print(queue.popleft())          # deque에 존재하는 popleft() 메소드를 이용
    else:
      print(-1)
    
  elif order[0] == 'size':            # size
    print(len(queue))

  elif order[0] == 'empty':           # empty
    if queue:
      print(0)
    else:
      print(1)

  elif order[0] == 'front':           # front 
    if queue:
      print(queue[0])
    else:
      print(-1)

  elif order[0] == 'back':            # back
    if queue:
      print(queue[-1])
    else:
      print(-1)
      
      
      
      
# 다른 풀이 : if - else를 삼항연산자로 수정(가독성 증가)
import sys
input = sys.stdin.readline

from collections import deque

queue = deque()
for _ in range(int(input())):
  order = input().split()

  if order[0] == 'push':
    queue.append(order[1])

  elif order[0] == 'pop':
    print(queue.popleft() if queue else -1)             # 만약 queue가 비어있지 않다면 pop, 아닐 경우 -1출력

  elif order[0] == 'size':
    print(len(queue))

  elif order[0] == 'empty':
    print(0 if queue else 1)                            # queue가 비어있지 않다면 0을 출력, 아닐 경우 -1출력 

  elif order[0] == 'front':
    print(queue[0] if queue else -1)                    # queue가 비어있지 않다면 queue배열의 0번째 인덱스 요소 출력, 아닐 경우 -1 출력

  elif order[0] == 'back':
    print(queue[-1] if queue else -1)                   # queue가 비어있지 않다면 queue배열의 가장 뒤의 있는 요소 출력, 아닐 경우 -1 출력
    
    
    
    
    
    
# 다른 풀이 : lambda 식을 이용한 방법
import sys
input = sys.stdin.readline

from collections import deque

queue = deque()
command = {                                                       # 명령어 'push', 'pop', 'size', 'empty', 'front', 'back'을 딕셔너리의 key값으로 설정
  "push": lambda x: queue.append(x),                              # lmabda 식을 이용하여 해당 명령을 처리하여 나온 값을 value로 설정 
  "pop": lambda: print(queue.popleft() if queue else -1),
  "size": lambda: print(len(queue)),
  "empty": lambda: print(0 if queue else 1),
  "front": lambda: print(queue[0] if queue else -1),
  "back": lambda: print(queue[-1] if queue else -1)
}

for _ in range(int(input())):
  order = input().split()
  if len(order) == 2:                                             # 입력받은 order의 길이가 2인 경우(예를 들어, push 2)
    command[order[0]](order[1])                                   # order[0]은 'push'를 의미하므로 command에서 key가 'push'일 때 order[1] 값을 
  else:
    command[order[0]]()
