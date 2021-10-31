# N을 입력받고 1부터 N까지의 수의 중요도를 입력받아, 중요도를 기준으로 수를 출력한다.

# 예제
# N이 6이고, 중요도가 1 1 9 1 1 1 이라면,
# 중요도에 따라 3 4 5 6 1 2 로 출력이 된다.

# 풀이
# 중요도와 1부터 N까지 담긴 numbers를 큐에 담고 중요도가 높은 게 큰 수를 가지고 있다.
# priority의 첫번째 자리에 max값이 있다면, index+1하고 priority.popleft()를 한다.
# 만약 이때 numbers.popleft()한 값이 M과 같다면 이때의 index 값을 print한다.

# 만약 priority[0]이 max가 아니라면 priority[0]이 최댓값이 될 때까지 popleft한 값을 다시 append하는 것을 반복한다.
# 이때 numbers도 같이 popleft후 append한다.

# 마침내 priority[0]이 최댓값이 되었다면 위의 과정을 반복한다.

# 고려할 점
# prority의 요소가 popleft할 때마다 index 변수를 +1하여 queue에 담긴 요소를 뺄 때
# 1씩 증가하는 index뿐 아니라 초기의 queue 인덱스를 고려해주어야 한다.

# 틀린 코드
# 아직 미완성..
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
