# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
# str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)" 형태의 문자열을 반환

# 내가 푼 코드

def solution(s):
    answer = sorted(map(int, s.split(' ')))
    return str(answer[0])+' '+str(answer[-1])


# 다른 사람 풀이
# 람다식을 이용한 방법

def solution(s):
    answer = sorted(s.split(" "), key=lambda x: int(x))
    return " ".join([answer[0], answer[-1]])
