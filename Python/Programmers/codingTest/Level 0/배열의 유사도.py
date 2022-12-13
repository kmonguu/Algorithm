# 두 배열이 얼마나 유사한지 확인해보려고 할 때, 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 반환

# 내가 푼 코드
# s1, s2배열을 돌면서 서로 같은지 판별 후 answer에 +1

def solution(s1, s2):
    answer = 0
    
    for i in range(len(s1)): 
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                answer += 1
    return answer
  
  
# 다른 풀이
# set()을 이용하여 s1, s2에 같은 문자를 구하여 그 길이를 반환

def solution(s1, s2):
    return len(set(s1)&set(s2));
