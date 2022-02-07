# 대문자와 소문자가 섞여있는 문자열 s가 매개변수로 주어질 때, 
# s에 'p'의 개수와 'y'의 개수를 비교하여 같으면 True, 다르면 False를 반환

# 내가 푼 코드
# 대소문자가 섞여있기 때문에 s를 모두 소문자로 바꿔준다.
# s안의 'p'와 'y'의 개수를 카운트하여 같다면 True, 다르다면 False를 반환하도록 한다.

def solution(s):
    s = s.lower()
    return True if s.count('p') == s.count('y') else False
