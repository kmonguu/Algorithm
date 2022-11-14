# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 반환

# 예제
# 2	10	2048
# 7	15	229,376

# 내가 푼 코드

def solution(n, t):
    for _ in range(t):
        n *= 2
    return n
  
# 다른 사람 풀이
# << 비트연산자 사용

def solution(n, t):
    return n << t
