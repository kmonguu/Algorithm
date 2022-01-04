# 사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매기려고 할 때, 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수를 k+1 이 된다.
# 이렇게 등수를 결정하면 같은 등수를 가진 사람은 여러 명도 가능하다.


# 예제
# [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]] 라는 5명의 집단이 있을 때
# 세 번째 사람 [88, 186] 보다 더 큰 덩치의 사람은 없으므로 1등이 된다.
# 그리고 첫 번째, 두 번째, 네 번째 각각의 덩치보다 큰 사람은 세 번째 사람뿐이므로 이들은 모두 2등이 된다.
# 마지막으로 다섯 번째 사람 [46, 155]보다 큰 덩치는 4명이므로 이 사람의 덩치 등수는 5등이 된다.


# 풀이
# 덩치 등수는 정렬하여 등수를 매기는 방식이 아닌, 자신보다 큰 덩치의 사람이 몇 명있는지에 따라 매겨진다.
# 각각의 사람들의 키와 몸무게를 비교하여 자신보다 큰 덩치의 사람 수를 센다.


# 코드
import sys
input = sys.stdin.readline

n = int(input())
people = []
for _ in range(n):
  people.append(list(map(int, input().split())))


for i in people:
  rank = 1                                          # rank를 1로 초기화
  for j in people:
    if i[0] < j[0] and i[1] < j[1]:                 # 자신보다 큰 덩치의 사람이 있다면
      rank += 1                                     # rank + 1
  print(rank, end=" ")


  
  
# 다른 풀이
import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in range(n):
  rank = 1
  for j in range(n):
    if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
      rank += 1
  
  result.append(rank)

print(*result)
