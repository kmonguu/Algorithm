# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 비내림차순이다.

# 내가 푼 코드
# 중복되는 수열을 여러 번 출력하면 안되므로 compare변수에 arr[idx]를 담고 다음 요소와 비교한다.
# 비내림차순으로 수열을 출력하기 위해 start를 매개변수로 주어 range범위를 idx+1로 조정한다.

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

answer = []
visited = [False]*n

def n_and_m(start):
  if len(answer) == m:
    print(' '.join(map(str, answer)))
    return 

  compare = 0
  for idx in range(start, n):
    if not visited[idx] and compare != arr[idx]:
      visited[idx] = True
      compare = arr[idx]
      answer.append(arr[idx])
      n_and_m(idx+1)
      visited[idx] = False
      answer.pop()

n_and_m(0)
