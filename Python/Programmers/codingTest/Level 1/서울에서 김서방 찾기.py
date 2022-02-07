# 문자열 배열 seoul이 매개변수로 주어졌을 때, 'Kim'의 위치를 찾아 반환

# 내가 푼 코드
# 문자열 포매팅을 이용하여 '김서방은 ~에 있다'라는 문자열 사이에 'Kim'의 인덱스 번호를 넣어주었다.

def solution(seoul):
    return ('김서방은 %s에 있다') %seoul.index('Kim')
