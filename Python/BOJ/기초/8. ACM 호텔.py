# 각 층에 W 개의 방이 있는 H 층 건물에서 정문으로부터 걷는 거리가 가장 짧은 방을 출력
# 방 번호는 YXX나 YYXX 형태로 Y는 층수, X는 왼쪽에서부터 센 호수가 된다.
# 예를 들어, H는 6이고 W는 12인 건물일 때 10번 째 방은 4층에서 왼쪽에서 2번 째 방인 402호가 된다.
# 손님 번호는 10번이고 층수는 6층 건물이라면 1호에 배정되지 못하고 2호로 넘어가는 것을 이용하여 N-H로 층수를 구하고 N/H로 호수를 구하는 식을 세웠다.


import math                           # math 모듈

Test_case = int(input())

for _ in range (Test_case):
  H, W, N = map(int, input().split()) # H 층수, w 각 층의 방 수, N 몇 번째 손님인지 입력

  Y = N                               # Y에 몇 번째 손님인지 입력받은 N을 저장

  while Y > H:                        # Y가 H보다 클 경우 while문 반복
    Y -= H                            # Y에 H층수를 빼 손님 방의 층수를 구함
      
  ho = math.ceil(N/H)                 # 호수를 구하기 위해 N에서 층수를 나눈 몫을 ceil함수를 이용하여 올림

  if ho < 10:                         # 호수가 10보다 작으면 방번호 가운데 0을 넣고 간격없이 출력
    print(Y, '0', ho, sep='')

  else:
    print(Y, ho, sep='')              # 호수가 10보다 크다면 층수와 호수를 붙여서 출력
    
    
# while문을 사용하지 않고 층과 호를 구해 속도를 개선할 수 있다.
# 층수 구하기 식 = N % H
# 호수 구하기 식 = math.ceil(N/H)

import math

Test_case = int(input())

for _ in range (Test_case):
  H, W, N = map(int, input().split())

  Y = (N%H)   
  ho = math.ceil(N/H)

  if ho < 10:
    print(Y, '0', ho, sep='')

  else:
    print(Y, ho, sep='')

