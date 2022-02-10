# 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열을 모두 반환

# 내가 푼 코드

def n_and_m(depth, n, m):

  if depth == m:
    print(' '.join(map(str, answer)))

  for i in range(1, n+1):
    if not visited[i]:                    # 중복을 방지하기 위해 해당 수를 방문했었는지를 확인한다.
      visited[i] = True                   # 방문하지 않았던 수라면 True로 바꿔주어 방문 여부를 변경한다.
      answer.append(i)                    # answer에 해당 수를 넣어준다.
      
      n_and_m(depth+1, n, m)              # answer배열의 길이를 나타내는 depth를 +1하고 다음 수열을 찾는다.
      
      visited[i] = False                  # 금방 방문했던 수는 다음 탐색을 위해 False로 변경해주고
      answer.pop()                        # answer에서 pop하여 다음 수열을 찾기 위해 원래자리로 돌아간다.

n, m = map(int, input().split())
visited = [False] * (n+1) 
answer = []
n_and_m(0, n, m)




# 다른 풀이

n,m = list(map(int,input().split()))
 
answer = []
 
def n_and_m():
    if len(answer) == m:                            # answer에 들어간 수열들이 m개가 되면 리스트에 들어있는 숫자들을 모두 출력하고 함수를 나온다.
        print(' '.join(map(str,answer)))
        return
    
    for i in range(1,n+1):                          # for문을 이용하여 1부터 n까지의 숫자들을 모두 확인
        if i not in answer:                         # answer 중복 확인
            answer.append(i)                        # answer에 중복된 수가 없다면 answer에 i를 추가해준다.
            n_and_m()                               # 재귀함수를 이용하여 다음 수를 answer에 넣어준다.
            answer.pop()                            # 금방 넣었던 수를 빼고 원래 자리로 돌아가서 다음 수열을 찾는다.
 
n_and_m()
