# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 * 으로 가린 문자열을 반환

# 내가 푼 코드
# phone_number의 전체 길이에서 4개를 빼고 나머지 요소를 '*'로 만들고 phone_number의 마지막 요소 4개를 더하여 반환한다.

def solution(phone_number):
    return '*' * (len(phone_number)-4) + phone_number[-4:]
