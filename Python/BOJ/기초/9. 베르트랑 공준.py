# 여러 개의 테스트 케이스는 한 줄로 n을 포함한다. 입력의 마지막에 0이 오면 테스트 케이스 입력은 끝난다.
# 자연수 n이 주어졌을 때, n보다 크고 2n보다 작거나 같은 소수의 개수를 출력
# 에라토스테네스의 체 알고리즘을 사용하여 문제를 풀 수 있다.

# 풀이 1 : 숫자를 입력할 때마다 에라토스테네스의 체로 소수를 구하는 과정을 반복하므로 속도가 느림

while True:                                 # 여러 개의 테스트 케이스를 입력받기 위한 while 반복문
  n = int(input())  
  if n == 0:                                # 0이 입력되면 while 반복문이 종료되도록 함
    break
  m = n*2                                   # 소수의 개수를 출력하기 위한 범위의 최댓값인 2n을 변수 m에 선언

  numbers = [True] * (m+1)                  # numbers의 길이를 m+1로 설정하고 True로 초기화
  numbers[0] = numbers[1] = False           # 0과 1인 소수가 아니므로 False

  def prime():                              # 에라토스테네스의 체 구현부분 prime 함수
    for i in range(2, int(m ** 0.5)+1):    
      if numbers[i] == True:
        for j in range(i+i, m+1, i):        
          numbers[j] = False

  prime() 
  cnt = 0                                   # 소수의 개수를 세는 cnt변수를 0으로 초기화
  for i in range(n+1, m+1):                 # n보다 크고 2n보다 작거나 같을 때를 범위로 하므로 for문의 범위를 n-1부터 m+1까지로 함 
    if numbers[i] == True:                  # numbers[i]가 True 일 경우
      cnt += 1                              # cnt 변수에 +1 하여 소수의 개수를 구함
  print(cnt)
  
  
  
  
# 풀이 2: n의 최댓값 123,456까지 에라토스테네스의 체로 거른 뒤 범위 안의 소수의 갯수를 출력(속도 개선)
   
import sys                                      # sys 모듈
input = sys.stdin.readline

m = 123456 * 2                                  # 소수를 구하는 범위의 최댓값 2n (123,456 * 2)을 변수 m에 선언
numbers = [True] * (m + 1)
numbers[0] = numbers[1] = False

def prime():                            
  for i in range(2, int(m ** 0.5) + 1):
    if numbers[i] == True:
      for j in range(i ** 2, m + 1, i):
        numbers[j] = False

prime()                                  
while True:                                     # while 반복문
  n = int(input())                      
  if n == 0:                                    # n이 0이면 종료
    break

  print(numbers[n + 1 : n * 2 + 1].count(True)) # numbers 배열에서 슬라이싱을 이용해 n+1부터 2n까지의 범위에서 소수를 의미하는 True의 갯수를 세어 출력
