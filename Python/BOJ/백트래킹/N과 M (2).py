# 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복없이 M개를 고른 오름차순으로 정렬 된 수열을 반환

# 내가 푼 코드
# 재귀함수를 이용하고, 출력하려는 리스트의 길이가 m과 같아진다면 리스트를 출력
# 재귀함수에서는 start부터 n까지 숫자를 이용하여 탐색
# [1, 2]와 [2, 1]은 같은 수열로 판단하여 앞의 수가 뒤의 수보다 큰 경우를 제외한다.

def solution(start, n, m):
  if len(answer) == m:
    print(' '.join(map(str, answer)))

  for i in range(start, n+1):
    if i not in answer:
      answer.append(i)
      solution(i+1, n, m)
      answer.pop()

n, m = map(int, input().split())
answer = []

solution(1, n, m)
