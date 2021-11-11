# N개의 원소를 가진 양방향 순환 큐가 있고, 입력받은 M개의 원소를 뽑아낸다.
# 둘째 줄에 뽑아내려고 하는 수의 위치를 순서대로 입력한다.

# 이 큐는 세 가지 연산을 할 수 있는데, 
# 1. 첫 번째 원소만 뽑아낼 수 있다.
# 2. 왼쪽으로 한 칸 이동시킬 수 있다.
# 3. 오른쪽으로 한 칸 이동시킬 수 있다.

# 원소를 주어진 순서로 뽑아내는데 드는 이동 횟수의 최솟값을 출력한다.


# 풀이
# 우선, 첫 번째 인덱스가 입력받은 뽑으려고 하는 수의 위치와 일치하는지 확인한다.
# 일치한다면 첫 번째 원소를 뽑아낸다.
# 일치하지 않는다면 왼쪽이나 오른쪽으로 큐의 원소들을 이동해야 하는데, 이때 최소 이동값을 구해야하므로 해당 수의 위치가 큐의 왼쪽에 가까운지, 오른쪽에 가까운지 확인한다.
# 해당 뽑아내려고 하는 수의 위치가 왼쪽, 큐의 앞쪽과 가깝다면 첫 번째 인덱스가 뽑아내려는 수의 위치와 같아질 때까지 왼쪽으로 한칸 이동시키는 것을 반복한다.
# 뽑아내려고 하는 수의 위치가 오른쪽인 큐의 뒷쪽과 가깝다면 첫 번째 인덱스가 뽑아내려는 수의 위치가 같아질 때까지 오른쪽으로 한칸 이동시키는 것을 반복한다.
# 왼쪽이든 오른쪽이든 한 칸 이동할 때 0으로 초기화 된 cnt 변수를 +1하여 이동 횟수를 구한다.


# 코드
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
index = list(map(int, input().split()))
cnt = 0                                               # 이동 횟수를 저장하는 변수

numbers = deque(list(range(1, N+1)))                  # numbers를 deque로 선언하며 동시에 1부터 N+1까지 리스트형태로 저장한다.
for i in index:
  while True:
    if numbers[0] == i:                               # numbers의 첫 번째 인덱스의 값이 i와 같다면
      numbers.popleft()                               # 첫 번째 원소를 뽑아낸다.     
      break

    else:                                             # numbers의 첫 번째 인덱스의 값이 i와 같지 않는다면
      if numbers.index(i) < len(numbers)/2:           # 뽑아내려는 수의 위치 인덱스가 numbers의 길이를 반으로 나는 것보다 작은 경우
        while numbers[0] != i:                        # numbers의 첫 번째 인덱스의 값이 i와 같지 않을 때를 참으로 while문 반복
          numbers.append(numbers.popleft())           # 이 경우, 왼쪽으로 원소들을 이동시키는 것이 이동 횟수가 최소가 되므로 popleft()한 원소를 큐의 뒤로 append해준다.
          cnt += 1                                    # 한번 이동할 때마다 cnt를 +1 한다.

      else:                                           # 뽑아내려는 수의 위치 인덱스가 numbers 길이를 반으로 나눈 것보다 큰 경우
        numbers.appendleft(numbers.pop())             # 오른쪽 방향으로 회전하는 것이 이동 횟수가 최소가 되므로 pop() 한 원소를 큐의 앞으로 appendleft()하여 회전시킨다.
        cnt += 1                                      # 마찬가지로 한번 이동할 때 마다 cnt에 +1 해준다.

print(cnt)


