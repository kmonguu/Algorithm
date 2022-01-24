# N부터 M까지의 수들을 종이에 적었을 때 종이에 적힌 0들을 세어 출력

# 내가 푼 코드
# n부터 m+1까지를 범위로 하는 i를 내부 for문에서 str형으로 바꾸고 문자열을 하나하나 순회하여 '0'이 있다면 cnt를 +1해준다.
# 만약 i가 1004일 때, 0이 2개이므로 이러한 경우를 대비하여 i를 str형으로 바꾸어 하나씩 살펴봐야한다.

import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n, m = list(map(int, input().split()))

  cnt = 0
  for i in range(n, m+1):
    for j in str(i):
      if '0' in j:
        cnt += 1
  print(cnt)

  
  

# 다른 사람 풀이
# n, m 사이의 수를 모두 str로 바꾸고 count를 이용하여 0의 개수를 셈

import sys
input = sys.stdin.readline

for _ in range(int(input()):
  n, m = map(int, input().split())
  
  print("".join(map(str, range(n, m + 1))).count("0"))    # n, m 사이에 있는 모든 숫자를 str로 변환 후 문자열로 변환하고 이후 "0"의 개수를 셈
