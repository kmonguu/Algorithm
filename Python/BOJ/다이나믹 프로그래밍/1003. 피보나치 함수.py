# 0 1 1 2 3 5 8 13 .. 과 같은 피보나치 수열은

def fibo(n):
  if (n == 0):
     return 0
    
  elif (n == 1):
      return 1
  else:
      return fibo(n - 1) + fibo(n - 2)
    
# 위와 같은 재귀함수를 통해 구할 수 있다.

# fibo(3)을 오출하면 다음과 같은 일이 일어난다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
# 1은 2번 출력되고, 0은 1번 출력된다.

# fibo(n)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하시오.
# (제한 조건 : n은 40보다 작거나 같은 자연수 또는 0이다.)

# 시간초과(실패) 코드
# 재귀함수를 이용하여 피보나치 함수를 호출하는 방식으로 구했지만, 제한 조건을 고려하지 못하여 시간초과 발생

global cnt
cnt = [0, 0]

def fibo(n):
  if (n == 0):
      cnt[0] += 1
  elif (n == 1):
      cnt[1] += 1
  else:
      fibo(n - 1) + fibo(n - 2)
    
  return ' '.join(map(str, cnt))

for _ in range(int(input())):
  cnt = [0, 0]
  n = int(input())
  print(fibo(n))


# 맞춘 코드
# 재귀를 사용하지 않고 미리 배열에 피보나치 수열을 구하여 저장한 뒤 찾아쓰는 방법

fibo = [[0, 0] for _ in range(41)]
fibo[0] = [1, 0]
fibo[1] = [0, 1]

nArr=[]  # 테스트 케이스에 맞게 입력받은 n을 저장하는 배열
maxOfN = 0

for _ in range(int(input())):
  n = int(input())   
  nArr.append(n)  # 입력받은 n을 nArr에 저장
  maxOfN = max(maxOfN, n) # 입력받은 n 중 가장 큰 값을 maxOfN에 저장한다.

for idx in range(2, maxOfN+1):  # 2부터 n의 최댓값까지 피보나치 규칙을 활용하여 0이 나오는 횟수, 1이 나오는 횟수를 구하여 fibo배열에 저장
  fibo[idx][0] = fibo[idx-1][0] + fibo[idx-2][0]
  fibo[idx][1] = fibo[idx-1][1] + fibo[idx-2][1]

for n in nArr:  # 미리 fibo 함수에 구해둔 값을 n에 맞게 찾아서 출력
  print(' '.join(map(str,fibo[n])))
  
  
# 위 방법의 문제점 : n의 값에 상관없이 fibo배열을 무조건 40개를 미리 만들어둠으로 자원의 낭비가 발생

# 해결방법
# fibo 배열을 n만큼만 생성하여 낭비되는 부분이 없도록 함

# 최종 코드
t = int(input())
for _ in range(t):
    n = int(input())

    if n == 0:
        print('1 0')
    else:
        fibo = [[0, 0] for _ in range(n + 1)]
        fibo[0] = [1, 0]
        fibo[1] = [0, 1]

        for idx in range(2, n + 1):
            fibo[idx][0] = fibo[idx - 1][0] + fibo[idx - 2][0]
            fibo[idx][1] = fibo[idx - 1][1] + fibo[idx - 2][1]

        print(' '.join(map(str, fibo[n])))

