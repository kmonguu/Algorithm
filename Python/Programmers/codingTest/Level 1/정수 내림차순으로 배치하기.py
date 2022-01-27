# 정수 n을 매개변수로 받아, n의 각 자릿수를 큰 것부터 작은 순으로 정렬한 새로운 정수를 반환

# 내가 푼 풀이

def solution(n):
    n = sorted(list(str(n)))
    return int(''.join(n[::-1]))
