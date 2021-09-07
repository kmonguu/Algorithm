# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수를 골드바흐 수라고 한다.
# 4 = 2+2, 6 = 3+3, 8 = 3+5 등을 예로 들 수 있다.
# 테스트 케이스의 수를 입력하고 각 테스트 케이스마다 더하여 입력받은 수 n이 되는 소수를 작은 수부터 출력

# 풀이 과정
# n의 최댓값은 10000으로, numbers에 최댓값의 크기만큼 True로 초기화하여 numbers 배열을 가지고 소수만 걸러냄
# 두 소수의 합이 n이 되야하므로 소수 중 하나를 a로 둔다면 나머지 하나는 n-a가 된다.
# n을 2로 나눈 몫을 n2에 저장하고 for문으로 n2부터 거꾸로 1까지 범위를 설정하면 a변수는 n2에서 1사이의 값이 된다.
# 자동적으로 n-a 값은 n2부터 n-1까지의 범위를 갖는다. 예를 들어, n이 10이라면 a는 5~1, n-a는 5~9의 범위를 갖게 됨
# 마지막으로 if문을 사용하여 이 두수가 소수인지 확인한 후 출력한다.


import sys
input = sys.stdin.readline

numbers = [True] * 10001                                    # n의 최댓값인 10000으로 크기를 설정하고 True로 초기화
numbers[0] = numbers[1] = False                             # 0과 1은 소수가 아니므로 False로 변환


def prime():
  for x in range (2, 101):                                  # 10000의 제곱근까지만 확인하면 되므로 2부터 100까지 변수 x에 선언
    if numbers[x] == True:
      for y in range(x ** 2, 10001, x):
        numbers[y] = False

prime()

T = int(input())
for _ in range(T):
   n = int(input())
   n2 = n//2                                                # 입력받은 n을 2로 나눈 몫을 구함

   for a in range(n2, 1, -1):                               # a의 범위를 1부터 n2까지로 해도 되지만 두 수의 크기 차이가 작아야하므로 n2에서부터 1까지 a에 선언
     if (numbers[n-a] == True) and (numbers[a] == True):    # n-a와 a가 소수인지를 확인하기 위해 numbers에서 True인지 확인
       print(a, n-a)
       break
      
      
      
 
# 소수 집합을 생성하는 다른 풀이
# 소수에는 2를 제외하고 짝수가 없으므로 2와 홀수로 이루어진 10000까지의 숫자 집합을 생성
# 이 집합에서 홀수의 배수들을 빼면 소수만 남게 된다.


numbers = {x for x in range(2, 10001) if x==2 or x%2 == 1}               # 2와 홀수로 이뤄진 집합 numbers
for y in range(3, 101, 2):
  numbers -= { i for i in range(2*y, 10001, y) if i in numbers}          # 홀수의 배수들로 이루어진 집합을 numbers에서 빼줌

   
