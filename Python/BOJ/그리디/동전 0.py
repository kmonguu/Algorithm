# n 종류의 동전을 적절히 사용해서 그 가치의 합을 k로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 내가 푼 코드
# k원에서 동전을 빼는 방식으로 풀었다.
# k에 값이 있는 동안, a배열에 저장된 동전의 종류를 내림차순으로 for문에서 순회한다.
# 동전의 종류가 k원보다 작거나 같은 경우에 필요한 동전의 개수를 저장하는 answer 변수에는 k원과 동전 i를 나눈 몫을 저장한다.
# k에는 나눈 해당 동전만큼의 액수를 빼주기 위해 동전 i와 나눈 나머지를 다시 k에 저장한다.
# 이 과정을 k가 0이 될 때까지 반복하면 answer에 필요한 동전의 개수가 저장되어 있다.

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

answer = 0
while k:
  for i in a[::-1]:
    if k >= i:
      answer += k // i
      k %= i
print(answer)
