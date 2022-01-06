# 두 정수 a, b가 주어졌을 때, a와 b 사이에 속한 모든 정수의 합을 반환

# 코드
# a > b, a < b 로 경우를 나누어서 풀었다.

def solution(a, b):
    answer = 0
    
    if (a <= b):
        for i in range(a, b+1):
            answer += i
    else:
        for i in range(b, a+1):
            answer += i
            
    return answer
  
  
# 다른 풀이
# a와 b의 크기 비교를 하지 않고 max, min을 활용하여 푸는 방법도 있다.

# 코드
def solution(a, b):
    return sum(range(min(a,b), max(a,b) + 1))
