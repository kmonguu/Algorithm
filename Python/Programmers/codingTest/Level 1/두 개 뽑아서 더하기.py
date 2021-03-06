# 정수 배열 numbers가 주어질 때 numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 반환

# 풀이
# itertools의 combinations 함수룰 이용하여 중복없이 원하는 배열에서 원하는 갯수만큼 뽑아 조합을 만들 수 있다.

# 코드
from itertools import combinations

def solution(numbers):
    answer = []
    for i in combinations(numbers, 2):
        answer.append(sum(i))             # 주어진 numbers 배열에서 2개씩 뽑아 그 합을 answer에 담는다.

    return sorted(list(set(answer)))      # 같은 중복된 수를 set으로 제거 후 오름차순으로 정렬하여 반환



# 다른 풀이
from itertools import combinations

def solution(numbers):
    return sorted(set(map(sum, combinations(numbers, 2))))



# 다른 풀이 : dfs 탐색을 이용한 백트래킹 알고리즘 사용
def solution(numbers):
    def dfs(case, pick, idx, depth):
        if depth == pick:
            answer.add(case)
            return
        
        for i in range(idx, len(numbers)):
            dfs(case + numbers[i], pick, i + 1, depth + 1)
    
    answer = set()
    dfs(0, 2, 0, 0)
    return sorted(answer)
