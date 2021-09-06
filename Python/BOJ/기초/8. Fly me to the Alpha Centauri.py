# 문제의 규칙을 알아내는 과정이 오래걸렸음
# 총 이동해야할 거리를 이동한 횟수를 count라고 했을 때 이 count가 반복되는 것을 count_repeat으로 뒀다.
# 이 count_repeat는 1, 1, 2, 2, 3, 3, 4, 4, ... 순으로 늘어났기 때문에 수가 2번씩 반복되고 커질 때의 이동해야할 거리는 2, 6, 12, 20, ... 으로 count_repeat*(count_repeat+1)의 식을 구할 수 있음
# 또한 count의 횟수가 바뀔 때를 보면 이동거리가 4, 9, 16, ... 으로 count_repeat의 제곱수인 것을 알 수 있음 이것을 이용하여 count를 구할 수 있다.

T = int(input())

for _ in range(T):
  x, y = map(int, input().split())
  distance = y-x                                  # 이동해야할 거리
  count_repeat = 0                                # 주어진 거리를 움직이는데 걸리는 횟수의 반복


  while True:
    if distance <= count_repeat*(count_repeat+1): # 이동해야할 거리가 count 반복횟수가 바뀔 때 경계에 있는 수보다 작거나 같을 경우
      break
    count_repeat += 1                             # distance가 경계에 있는 수보다 크다면 count_repeat을 +1 해준다.

  if distance <= count_repeat**2:                 # distance가 count_repeat의 제곱인 4, 9, 16, ..., 보다 작거나 같다면
    print(count_repeat*2-1)                       # 최소 이동거리 count를 출력한다.

  else:
    print(count_repeat*2)                         # distance가 count_repeat의 제곱보다 클 경우 최소 이동 거리 count를 출력한다.
    
    
