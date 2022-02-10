# 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 M개를 고른 수열은 같은 수를 여러 번 골라도 되며 고른 수열은 비내림차순이어야 한다.
# 중복되는 수열을 여러 번 출력하면 안된다.

# 내가 푼 코드

n,m = list(map(int,input().split()))
answer = []
 
def n_and_m(start, n, m):
  if len(answer) == m:
    print(' '.join(map(str,answer)))
    return
  
  for i in range(start ,n+1):             # 고른 수열은 비내림차순이라는 조건을 만족하기 위해 수열의 앞 요소가 뒷 요소보다 작은 경우가 없도록 범위를 설정  
    answer.append(i)
    n_and_m(i, n, m)                      # 같은 수를 여러 번 사용할 수 있다는 조건을 만족하기 위해 재귀함수 호출시 i+1이 아닌 i를 넘겨줌 
    answer.pop()
 
n_and_m(1, n, m)
