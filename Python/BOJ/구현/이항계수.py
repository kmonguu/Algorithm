# 자연수 N과 정수 K가 주어졌을 때 이항 계수 (N/K)를 출력

# 내가 푼 코드
# 이항 계수를 다시 말해 조합이라고 한다.
# 이항 계수를 구하는 식 n!/r!(n-r)!을 이용하여 팩토리얼 재귀함수를 구현하여 문제를 풀었다.

n, k = map(int, input().split())

def fect(x):
  return x * fect(x-1) if x > 1 else 1

print(int(fect(n)/(fect(n-k)*fect(k))))
