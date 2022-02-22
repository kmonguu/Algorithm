# N개의 자연수와 자연수 M이 주어졌을 때, N개의 자연수 중에서 M개를 고른 수열을 반환
# 같은 수를 여러 번 골라도 되며, 고른 수열은 비내림차순이어야 한다.

# 내가 푼 코드
# N과 M (8)과 거의 비슷하지만, 입력받은 N개의 자연수 중 set으로 감싸서 중복을 제거해주었다.
# 같은 수를 여러 번 골라도 된다는 조건을 set을 통해 중복되는 수를 없애고, 중복을 제거하는 if조건문을 없애는 방법으로 만족시킴
# 수열을 비내림차순으로 출력하기 위해 start를 매개변수로 주었다.
# 재귀함수 호출 시 매개변수로 answer에 담긴 요소의 인덱스를 주어 해당 인덱스보다 작은 인덱스는 탐색하지 않도록하여 비내림차순으로 수열을 만들었다.

n, m = map(int, input().split())
arr = sorted(set(map(int, input().split())))
answer = []

def n_and_m(start):
  if len(answer) == m:
    print(*answer)
    return

  for idx in range(start, len(arr)):
    answer.append(arr[idx])
    n_and_m(idx)
    answer.pop()

n_and_m(0)



# 딕셔너리를 이용한 방법

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

def dfs(case, idx):
  if len(case) == m:
    result = tuple(case)
    if result not in check:
      check[result] = True
      print(*case)
    
    return

  for i in range(idx, n):
    dfs(case + [numbers[i]], i)

check = {}
dfs([], 0)
