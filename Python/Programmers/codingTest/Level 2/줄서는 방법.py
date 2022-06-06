# 사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 반환

# 예시
# n = 3, k = 5 결과값 = [3,1,2]
# 예를 들어, 3명의 사람이 있다면 아래와 같이 6가지의 줄서는 방법이 있고, 이 중 5번째 방법을 반환하면 됨

# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]


# 시간초과 코드(1) : itertools 라이브러리 사용한 방법

from itertools import permutations

def solution(n, k):
    arr = []
    answer = [num for num in range(1, n+1)]
    
    
    for i in permutations(answer, len(answer)): 
        arr.append(list(i))
        
        if len(arr) >= k:
            break
        
    return arr[-1]
        
# 시간초과 코드(2) : 재귀를 활용한 dfs로 접근한 방법

def dfs(n, k, cases, visited):
    global count, answer
    if count == k: return
    
    if len(cases) == n:
        count += 1
        if count == k: answer = cases[:]
        return

    for num in range(1, n+1):
        if not visited[num]:
            visited[num] = True
            dfs(n, k, cases + [num], visited)
            visited[num] = False
    
    return answer

def solution(n, k):
    global count, answer
    count = 0
    answer = []
    visited = [False] * (n + 1)
    return dfs(n, k, [], visited)
