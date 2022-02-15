# N개의 자연수와 자연수 M이 주어졌을 때, N개의 자연수 중 M개를 고른 수열을 모두 반환

# 내가 푼 코드
# compare 변수로 중복된 수열을 출력하는 것을 방지
# 만약, [9, 7, 9, 1]이라는 배열이 입력으로 들어오면 중복된 수열 1, 9와 1, 9가 출력되는 경우를 방지함
# visited로 숫자의 방문여부를 판단한다.

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [False] * n
answer = []

def n_and_m():
  if len(answer) == m:
    print(*answer)
    return

  compare = 0
  for i in range(n):
    if not visited[i] and compare != arr[i]:
      visited[i] = True
      answer.append(arr[i])
      compare = arr[i]
      n_and_m()
      visited[i] = False
      answer.pop()

n_and_m()
