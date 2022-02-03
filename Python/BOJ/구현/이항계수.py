# 자연수 N과 정수 K가 주어졌을 때 이항 계수 (N/K)를 출력

# 내가 푼 코드
# 이항 계수를 다시 말해 조합이라고 한다.
# 이항 계수를 구하는 식 n!/r!(n-r)!을 이용하여 팩토리얼 재귀함수를 구현하여 문제를 풀었다.

n, k = map(int, input().split())

def fect(x):
  return x * fect(x-1) if x > 1 else 1

print(int(fect(n)/(fect(n-k)*fect(k))))



# 다른 사람 풀이
# 재귀를 사용하지 않고, 다이나믹 알고리즘을 사용

def c(n, k):
  dp = [0] * (n + 1)
  dp[0] = dp[1] = 1
  for i in range(2, n + 1):
    dp[i] = i * dp[i - 1]

  return dp[n] // (dp[k] * dp[n - k])

n, k = map(int, input().split())
print(c(n, k))
