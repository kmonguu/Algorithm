# N개의 자연수와 자연수 M이 주어졌을 때, N개의 자연수 중에서 M개를 고른 길이가 M인 수열을 반환
# 같은 수를 여러 번 골라도 된다.

# 내가 푼 코드

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
answer = []

def n_and_m (start):
  if len(answer) == m:
    print(' '.join(map(str, answer)))  
    return

  for idx in range(start, n):
    answer.append(arr[idx])
    n_and_m(start)
    answer.pop()

n_and_m(0)
