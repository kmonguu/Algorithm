# 1부터 N까지 사람이 원을 이루면서 앉아있고, 양의 정수 K가 주어진다. 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 N명의 사람이 모두 제거될 때까지 반복한다. 

# 예시
# N이 7이고, K가 3이라면
# [1, 2, 3, 4, 5, 6, 7]에서 3번째 사람이 제거되고 -> [3]
# [1, 2, 4, 5, 6, 7]에서 3이 제거된 자리에서 3번째 사람을 제거한다. -> [3, 6]
# [1, 2, 4, 5, 7]에서 6이 제거된 자리에서 3번째 사람을 제거하면 한바퀴를 돌아 2가 제거된다. -> [3, 6, 2]
# [1, 4, 5, 7]에서 2가 제거된 자리에서 3번째 사람은 7이다. -> [3, 6, 2, 7]
# [1, 4, 5]에서 7이 제거된 자리에서 3번째 사람은 한바퀴를 돌아 5가 된다. -> [3, 6, 2, 7, 5]
# [1, 4]에서 5가 제거된 자리에서 3번째 사람은 한바퀴를 돌아 1 -> 4 또 한바퀴를 돌아 1이 된다. -> [3, 6, 2, 7, 5, 1]
# [4]만 남았으므로 4에서 3번째 사람은 그대로 4이므로 4를 제거한다. -> [3, 6, 2, 7, 5, 1, 4]

# 풀이
# 큐에 1부터 N까지의 수를 넣은 상태에서 K번째 사람을 빼려면 큐의 양쪽 끝에 있거나 K가 끝에 올 때까지 양쪽 중 한 곳의 수를 빼야한다.
# 큐에서 K번째를 꺼내기 위해 K-1번째까지 앞에서 popleft를 이용하여 뺀 다음 바로 뒤쪽으로 append하여 원형큐형태로 만들어 주었다.
# K-1번째까지 제거가 되었으면 K는 큐의 끝에 위치하게 되어 pop한 다음 결과 리스트에 넣어주는 것을 큐가 비어있을 때까지 반복한다.

# 코드
from collections import deque

N, K = map(int, input().split())
result = []
queue = deque(i for i in range(1, N+1))

while queue:                                        # 큐가 비어 있지 않은 경우 반복
  for _ in range(K-1):                              # 큐의 K-1번째요소까지 
    queue.append(queue.popleft())                   # 큐의 앞에서 뺀 다음 큐의 뒷쪽으로 append해준다.    
  result.append(queue.popleft())                    # K번째 수를 빼어 result 배열에 넣어준다.
print('<' + ', '.join(map(str, result)) + '>')




# 큐를 사용하지 않고 푼 방법
N, K = map(int, input().split())

numbers = list(range(1, N + 1))
result = []
idx = 0
while numbers:
  idx = (idx + (K - 1)) % len(numbers)              # idx + (K-1)을 한 값에 numbers[] 배열의 길이를 나눈 나머지를 idx변수에 저장한다.
  result.append(numbers.pop(idx))                   # numbers[idx]값을 pop한 뒤 result 배열에 넣어준다.
                                                    # numbers배열에서 값이 하나 제거되므로 numbers의 길이도 -1만큼 줄어들어 (idx + (K-1))에서 나눈 나머지를 구하고
                                                    # result배열에 number[idx]를 넣는 것을 반복하면 답을 구할 수 있다.
print("<" + ", ".join(map(str, result)) + ">")
