# 12시간 표기법으로 적힌 시간을 24시간 표기법으로 변환하여 반환

# 예제
# s = '12:01:00PM' 이 주어졌다면 '12:01:00'을 반환
# s = '12:01:00AM' 이 주어졌다면 '00:01:00'을 반환
# s = '07:05:45PM' 이 주어졌다면 '19:05:45'를 반환

# 내가 푼 코드
# 매개변수로 주어지는 s의 가장 뒤에 적힌 'AM', 'PM'에 따라 조건을 나누었다.
# 만약 'AM'일 때, 예외의 경우인 12시라면 시를 '00'으로 바꿔준다. 12시가 아니라면 문자열 가장 뒤의 'AM'을 제외하고 반환
# 만약 'PM'일 때, 예외의 경우인 12시라면 문자열 가장 뒤 'PM'을 제외하고 그대로 반환
# 'PM'인데 '12'시가 아니라면 24시간 표기법으로 바꾸기 위해 시를 정수형으로 변환하고 12를 더해준다.

def timeConversion(s):
    # Write your code here
    if s[-2:] == 'AM':
        return '00' + s[2:-2] if s[:2] == '12' else s[:-2]

    elif s[-2:] == 'PM':
        return s[:-2] if s[:2] == '12' else str(int(s[:2]) + 12) + s[2:-2]
