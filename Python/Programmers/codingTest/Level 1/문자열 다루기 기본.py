# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성되어 있다면 True, 아니면 False를 반환

# 내가 푼 코드
# 문자열 s가 숫자로만 구성되어있으면서 동시가 문자열의 길이가 4 또는 6이라면 True를 반환하도록 하였다.

def solution(s):
    return True if s.isdigit() and len(s) == 4 or len(s) == 6 else False
