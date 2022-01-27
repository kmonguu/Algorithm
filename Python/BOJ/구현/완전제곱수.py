# M과 N을 입력받아, M이상 N이하 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 합과 최솟값을 출력

# 내가 푼 코드

m = int(input())
n = int(input())

answer = []
for i in range(m, n+1):
  if i**0.5 == int(i**0.5):
    answer.append(i)

print(f'{sum(answer)}\n{min(answer)}' if answer else -1)
