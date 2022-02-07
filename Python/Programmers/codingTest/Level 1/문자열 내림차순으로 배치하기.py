# 매개변수로 주어지는 문자열 s에 나타나는 문자를 큰 것부터 작은 순으로 정렬하여 반환
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작다.

# 내가 푼 코드

def solution(s):
    return "".join(sorted(s, reverse = True))
