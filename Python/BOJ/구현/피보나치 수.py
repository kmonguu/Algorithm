# 피보나치 수는 0과 1로 시작한다. 0 번째 피보나치 수는 0이고, 1 번째 피보나치 수는 1이다.
# 그 다음 2 번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

# 틀린 코드
# 풀이 : 재귀함수를 구현하여 푼 방법 - 시간 초과 발생

def fib(n):
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else:
    return fib(n-2) + fib(n-1)

n = int(input())
print(fib(n))



# 정답 코드
# 배열에 미리 0과 1에 해당하는 값 0, 1을 넣어두고 2부터 n까지 앞 배열 2개의 합을 구해 배열에 넣어서 n의 값을 구함

# 재귀는 특정 문제가 아니면 잘 사용하지 않음. 해당 풀이는 다이나믹 프로그래밍이라는 알고리즘을 사용한 방법

n = int(input())
answer = [0, 1]

for _ in range(2, n+1):
  answer.append(answer[-1]+answer[-2])
  
print(answer[n])




# 정리 코드
# 문제에서 요구하는 바를 점화식으로 뽑아낸 후 그대로 코드로 옮기는 방법, 피보나치의 수가 다이나믹 프로그래밍 알고리즘을 적용할 수 잇는 대표적인 문제 중 하나이다.

n = int(input())
dp = [0] * (n+1)                    # dp 리스트 선언
dp[0], dp[1] = 0, 1                 # 초기값 설정

for i in range(2, n+1):
  dp[i] = dp[i - 1] + dp[i - 2]     # 점화식 적용
  
print(dp[n])
