# 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복을 포함한 M개를 고른 수열을 모두 반환

# 내가 푼 코드
# N과 M (1)문제에서 중복을 허용하기만 하면 되는 문제이다.
# 중복을 확인하는 if 조건문만 없앴다.

n,m = list(map(int,input().split()))
answer = []
 
def n_and_m(n, m):
  if len(answer) == m:
    print(' '.join(map(str,answer)))
    return
  
  for i in range(1,n+1):
    answer.append(i)
    n_and_m(n, m)
    answer.pop()
 
n_and_m(n, m)
