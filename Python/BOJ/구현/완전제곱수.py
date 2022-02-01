# M과 N을 입력받아, M이상 N이하 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 합과 최솟값을 출력

# 내가 푼 코드

m = int(input())
n = int(input())

answer = []
for i in range(m, n+1):
  if i**0.5 == int(i**0.5):
    answer.append(i)

print(f'{sum(answer)}\n{min(answer)}' if answer else -1)



# 다른 사람 풀이
# m과 n 사이의 수를 모두 확인하지 않고 m과 n의 제곱근 값들만 확인

import math
m, n = math.ceil(int(input()) ** 0.5), int(int(input()) ** 0.5) + 1

result = range(m, n)
if result:
  print(sum(map(lambda x: x ** 2, result)))
  print(result[0] ** 2)
else:
  print(-1)
  

  
  
  
# fuctools 모듈을 사용한 방법

import math
from functools import reduce

m, n = math.ceil(int(input()) ** 0.5), int(int(input()) ** 0.5) + 1

result = range(m, n)
if result:
  print(reduce(lambda total, cur: total + cur ** 2, result, 0))
  print(result[0] ** 2)
else:
  print(-1)
