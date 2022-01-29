# 자연수 N이 주어질 때, N의 각 자릿수의 합을 구해서 반환

# 내가 푼 코드

def solution(n):
    return sum(map(int,str(n)))
