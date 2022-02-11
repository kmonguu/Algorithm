# N개의 자연수와 자연수 M이 주어졌을 때, N개의 자연수 중에서 M개를 고른 수열을 반환
# 같은 수를 여러 번 골라도 되며, 고른 수열은 비내림차순이어야 한다.

# 내가 푼 코드
# 수열을 비내림차순으로 출력하기 위해 start를 매개변수로 주었다.
# 재귀함수 호출 시 매개변수로 answer에 담긴 요소의 인덱스를 주어 해당 인덱스보다 작은 인덱스는 탐색하지 않도록하여 비내림차순으로 수열을 만들었다.

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
answer = []

def n_and_m (start):
  if len(answer) == m:
    print(' '.join(map(str, answer)))
    return 
  
  for idx in range(start, n):
    answer.append(arr[idx])
    n_and_m(idx)
    answer.pop()

n_and_m(0)
