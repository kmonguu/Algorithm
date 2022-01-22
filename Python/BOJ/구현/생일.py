# 어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 출력

# 내가 푼 코드
# 이름, 일, 월, 년도를 입력받고, birth라는 배열에 각각의 자료형으로 추가한다.
# 람다식을 사용하여 나이가 적은 순으로 나열하고 나이가 가장 적은 사람의 이름과 가장 많은 사람의 이름을 출력

import sys
input = sys.stdin.readline

birth = []
for _ in range(int(input())):
  name, day, month, year = input().split()
  birth.append([str(name), int(day), int(month), int(year)])

birth.sort(key = lambda x : (x[3], x[2], x[1]), reverse =True)
print(birth[0][0]+'\n'+birth[-1][0])
