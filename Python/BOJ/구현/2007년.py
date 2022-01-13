# 현재 날짜가 2007년 1월 1일 월요일일 때, 2007년 x월 y일이 무슨 요일인지 출력


# 내 코드
# 풀이 : 12달의 일 수와 요일이 담긴 배열 month와 week를 만들어서 for문 반복으로 일 수 계산

x, y = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

day = 0
for i in range(x-1):
  day += month[i]
  
day = (day + y) % 7
print(week[day])



# 풀이 : 반복문을 사용하지 않고 sum 함수를 사용하여 일 수 계산

x, y = map(int, input().split())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

print(week[(sum(month[0:x]) + y) % 7])
