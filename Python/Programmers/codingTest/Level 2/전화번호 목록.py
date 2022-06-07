# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 반환

# 예시
# phone_num = ["119", "97674223", "1195524421"]일 때, '119'는 '1195524421'의 접두어이므로 False를 반환한다.

# 시간초과 코드 : 리스트를 사용하여 풀었더니 효율성 테스트에서 시간초과

def solution(phone_book):
    answer = True
    
    for call_num in phone_book:
        check = ''
        
        for num in call_num:
            check += num
             
            if check in phone_book and check != call_num:
                answer = False
    return answer
    

 # 맞은 코드 : 파이썬 내장함수 startswith을 사용 (해당 문자열이 특정 문자열로 시작하는지 확인시켜주는 함수)

def solution(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book)-1):
        if phone_book[idx+1].startswith(phone_book[idx]):  # 다음 인덱스의 값이 현재 인덱스 값으로 시작한다면 False를 반환
            return False
        
    return True
