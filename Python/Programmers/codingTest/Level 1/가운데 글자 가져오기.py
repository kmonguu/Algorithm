# 단어 s가 매개변수로 주어질 때, s의 가운데 글자를 반환
# 단어 길이가 짝수라면 가운데 두글자를 반환


# 내가 푼 코드
# 단어의 길이가 짝수인 경우 가운데 두글자를 출력하기 위해 인덱스 슬라이싱을 하였고, 아닌 경우 단어 길이의 가운데 값을 반환하도록 했음

def solution(s):
    idx = len(s) // 2
    return s[idx-1:idx+1] if len(s)%2 == 0 else s[idx]



# 다른 사람 코드
# if 조건문 없이 짝수, 홀수인 경우 처리

def solution(s):
    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]
