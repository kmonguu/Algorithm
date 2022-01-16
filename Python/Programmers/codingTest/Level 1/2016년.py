# 2016년 1월 1일이 금요일일 때, 2016년 a월 b일은 무슨 요일인지 반환
# 2016년은 윤년이다.

# 내가 푼 코드
# 1월 1일이 금요일이라고 되어있으므로 week[1]이 금요일이 되도록 저장한다.
# 윤년의 2월은 29일까지로 배열에 담아준다.

def solution(a, b):
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    return week[(sum(month[0:a]) + b) % 7]


# 모듈을 사용한 방법

import datetime

def solution(a, b):
    days = [ "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return days[datetime.date(2016, a, b).weekday()]
