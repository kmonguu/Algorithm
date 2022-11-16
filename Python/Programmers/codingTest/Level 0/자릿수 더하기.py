# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 반환

# 예제
# n       result
# 1234      10
# 930211    16


# 내가 푼 코드

def solution(n):
    return sum(list(map(int, str(n))))
