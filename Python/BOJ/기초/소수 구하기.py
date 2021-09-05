# M과 N을 숫자로 입력받아 M이상 N이하의 수 중 소수를 모두 출력하는 문제
# 에라토스테네스의 체 알고리즘을 사용하여 풀지 않으면 시간초과가 발생



# 에라토스테네스의 체를 사용한 코드 풀이

M, N = map(int, input().split())

numbers = [True] * (N+1)                  # numbers 배열의 길이를 N+1 만큼 설정하고 True로 초기화
numbers[0] = numbers[1] = False           # 0과 1은 소수가 아니므로 False로 설정

def prime_number():                       # 에라토스테네스의 체 구현부분
  for i in range(2, int(N ** 0.5) + 1):   # 입력받은 수 N이 소수인지 알기 위해 N의 제곱근까지만 확인하면 되므로 2부터 N의 제곱근까지 for문 변수 i에 선언
    if numbers[i] == True:                # numbers[i]가 True일 경우
      for j in range(i ** 2, N + 1, i):   # i를 제외한 i의 제곱부터 N까지 i의 배수들을 for문 변수 j에 선언
        numbers[j] = False                # i의 배수는 소수가 아니므로 numbers[j]에 False로 변환

prime_number()                            # 에라토스테네스의 체 실행부분
for i in range(M, N + 1):                 # 소수들 중 출력할 부분은 M부터 N까지 이므로 범위를 설정
  if numbers[i] == True:                  # numbers[i]가 True인 것만 
    print(i)                              # 출력
    
 


# 풀이 2 : M부터 N까지 매번 소수인지 처음부터 확인하기 때문에 방법 1보다 속도가 느림

import sys                                        # sys 모듈

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N + 1):                         # M부터 N까지를 범위로 하는 for문 변수 i 선언
    if i == 0 or i == 1: continue                 # 0과 1은 소수가 아니므로 continue
    x = int(i ** 0.5)                             # 변수 x에 i의 제곱근을 정수형으로 저장
    for j in range(2, x + 1):                     # 2부터 제곱근이 담긴 변수 x까지 for문 변수 j 선언
        if i % j == 0:                            # i에 j를 나눈 나머지가 0이라면 나누어 떨어지는 것이므로 소수가 아니므로 break
            break                                 
    else:                                          
        print(i)
        
        
        
# 에라토스테네스의 체를 사용하지 않은 시간초과 코드

M, N = map(int, input().split())

for i in range (M, N+1):
  if 1 < i:
    check = True
    for j in range (2, int(i ** 0.5) + 1):
      if i % j == 0:
        check = False

    if check:
      print(i)
