# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# N개의 자연수 중 M개를 고른 수열 중 같은 수를 여러 번 골라도 된다.

# 내가 푼 코드
# N과 M (10)에서 비내림차순 조건에 사용했던 start 매개 변수를 빼고, 같은 수를 여러 번 골라도 되기 때문에 visited 방문 체크 기능을 뺌

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

answer = []

def n_and_m():
  if len(answer) == m:
    print(*answer)
    return

  compare = 0
  for idx in range(n):
    if compare != arr[idx]:
      answer.append(arr[idx])
      compare = arr[idx]
      n_and_m()
      answer.pop()

n_and_m()
