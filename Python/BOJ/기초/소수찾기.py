# 주어진 N개의 수 중에서 소수가 몇 개인지 찾아서 출력하는 문제
# 1은 소수가 아니므로 2부터 입력받은 숫자 i까지 나누어 떨어지는지 확인하므로 효율성에 문제가 있음

N = int(input())
sosu = 0                        # 소수가 몇 개인지 count                 

a = map(int, input().split())

for i in a:                     # a 안에 입력받은 요소를 for문 변수 i에 선언
  if 1 < i:                     # i가 1보다 클 경우 if문
    x = 0                       # 변수 x는 for문이 한번 돌 때 마다 0으로 초기화
    
    for j in range(2, i):       # 2부터 변수 i-1까지를 범위로 하는 for문 변수 j
      if i%j == 0:              # j와 i를 나누어 0으로 나누어 떨어질 경우를 확인
        x += 1                  # 나누어 떨어진다면 소수가 아니므로 변수 x에 +1

    if x == 0:                  # x==0 일 경우 1과 자기 자신을 제외한 숫자로는 나누어 떨어지지 않는 것을 의미
      sosu += 1                 # sosu 변수에 +1

print(sosu)


# 다른 방법) 입력받은 값이 소수인지 확인하기 위해 이 수의 제곱근이 소수인지 확인

N = int(input())
sosu = 0

a = map(int, input().split())

for i in a:
  if 1 < i:
    check = True
    for j in range(2, int(i ** 0.5) + 1):	  # 2부터 i의 제곱근까지를 범위로 하는 for문 변수 j
      if i % j == 0:			                  # i % j 의 값이 0일 경우 나누어 떨어지는 것이므로 소수가 아니다.
        check = False		                    # check에 False를 선언

    if check:			                          # check가 True일 경우
      sosu += 1			                        # sosu + 1

print(sosu)
