# 정수 N이 주어졌을 때, N을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램

# 예를 들어 N이 4일 때 1,2,3의 합으로 나타내는 방법은 총 7가지이다.
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1

# 합을 나타낼 때는 수를 1개 이상 사용해야 한다.


# 풀이
# 이 문제에서 규칙을
# N = 1, 1 (1가지)
# N = 2, 1+1, 2 (2가지)
# N = 3, 1+1+1, 1+2, 2+1, 3 (4가지)
# N = 4, 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1 (7가지)
# N = 5, 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1, 1+1+3, 1+3+1, 3+1+1, 2+3, 3+2 (13개)

# 위의 규칙을 통해 N이 4일 때 경우의 수는 N이 1, 2, 3일 때의 경우의 수를 합한 것과 같고, 
# N이 5인 경우의 수는 N이 2, 3, 4일 때의 경우의 수를 합한 것과 같다는 것을 알 수 있습니다.

# 이러한 규칙을 통해 N이 3보다 클 때의 N의 경우의 수는 f(N) = f(N-1) + f(N-2) + f(N-3)이라는 점화식을 구할 수 있습니다.
# 이 점화식을 이용하여 재귀함수를 사용하여 풀 수 있었습니다.


# 코드

import sys 
input = sys.stdin.readline

def sum(num):                                     # 재귀함수 구현
  if num == 1:                                    # num이 1인 경우
    return(1)                                     # 1을 반환 
  elif num == 2:                                  # num이 2인 경우
    return(2)                                     # 2를 반환
  elif num == 3:                                  # num이 3인 경우
    return(4)                                     # 4를 반환
        
  else:                                           # num이 4이상인 경우
    return sum(num-1) + sum(num-2) + sum(num-3)   # 규칙이 적용되어 num의 (num-1), (num-2), (num-3)의 경우의 수를 더한 값이 num의 경우의 수가 된다.

for _ in range(int(input())):
  num = int(input())
  print(sum(num))
  

  
# 다른 코드
t = int(input())
result = [1, 2, 4]
for i in range(3, 10):
  result.append(result[i - 3] + result[i - 2] + result[i - 1])
for i in range(t):
  n = int(input())
  print(result[n - 1])
  
  
  
# dp 테이블을 이용한 풀이

import sys
input = sys.stdin.readline

dp = [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 11):
  dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

t = int(input())
for _ in range(t):
  n = int(input())
  print(dp[n])
