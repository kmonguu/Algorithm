# N을 입력받고 1부터 N까지의 수의 중요도를 입력받아, 중요도를 기준으로 수를 출력한다.

# 예제
# N이 6이고, 중요도가 1 1 9 1 1 1 이라면,
# 중요도에 따라 3 4 5 6 1 2 로 출력이 된다.

# 풀이
# 중요도와 그 인덱스(0부터 N-1까지)가 담긴 numbers를 큐에 담고 중요도가 높은 게 큰 수를 가지고 있다.
# priority의 첫번째 자리에 max값이 있다면, index+1하고 priority.popleft()를 한다.
# 만약 이때 numbers.popleft()한 값이 M과 같다면 이때의 index 값을 print한다.

# 만약 priority[0]이 max가 아니라면 priority[0]이 최댓값이 될 때까지 popleft한 값을 다시 append하는 것을 반복한다.
# 이때 numbers도 같이 popleft후 append한다.

# 마침내 priority[0]이 최댓값이 되었다면 위의 과정을 반복한다.

# 고려할 점
# prority의 요소가 popleft할 때마다 index 변수를 +1하여 queue에 담긴 요소를 뺄 때
# 1씩 증가하는 index뿐 아니라 초기의 queue 인덱스를 고려해주어야 한다.

# 틀린 코드
# 테스트 케이스 하나마다 index 변수가 0으로 초기화되어야 하는데 for문 밖에 선언되어 index의 값이 계속 쌓여서 문제가 생김
# 문제 이해를 잘못해서 numbers 배열에 들어가야하는 수가 왜 인덱스인지 인지하지 못함

import sys
input = sys.stdin.readline

from collections import deque
index = 0

Testcase = int(input())
for _ in range(Testcase):
  N, M = map(int, input().split())   

  priority = deque(list(map(int, input().split())))
  numbers = deque([number for number in range(N)])   

  while priority:
    if priority[0] == max(priority):
      index += 1
      priority.popleft()
      if numbers.popleft() == M:
        print(index)

    else:
      priority.append(priority.popleft())
      numbers.append(numbers.popleft())

      
# 맞은 코드 
# index변수가 popleft 될 때마다 +1하니까 그 의미에 맞춰 cnt로 변수명을 바꿔주고, 테스트케이스 for문 안에 넣음으로 테스트케이스마다 초기화되도록 수정
# 또한, 인덱스가 들어가는 배열의 변수명을 index로 바꿈

import sys
input = sys.stdin.readline

from collections import deque

Testcase = int(input())
for _ in range(Testcase):
  cnt = 0
  N, M = map(int, input().split())   

  priority = deque(list(map(int, input().split())))
  index = deque(list(range(N)))   

  while priority: 
    if priority[0] == max(priority):                    # 중요도가 담긴 배열 priority의 첫 번째 요소의 값이 최댓값인 경우
      cnt += 1                                          # cnt에 +1해주고
      priority.popleft()                                # popleft를 통해 그 첫 번째요소를 빼낸다.
      if index.popleft() == M:                          # 동시에 index요소의 첫 번째 요소를 popleft를 이용하여 빼내고 이 값이 입력받은 값 M과 같으면
        print(cnt)                                      # 몇 번째 순서로 출력이 되었는지 cnt를 출력하여 나타낸다.
        break

    else:                                               # 만약 priority에 첫 번째 요소가 최댓값이 아니면
      priority.append(priority.popleft())               # 최댓값이 첫 번째 자리에 위치하여 if문의 조건에 맞을 때까지 앞의 요소를 popleft하고 큐 뒤로 append한다. 
      index.append(index.popleft())                     # index 큐도 priority와 같이 움직인다.
