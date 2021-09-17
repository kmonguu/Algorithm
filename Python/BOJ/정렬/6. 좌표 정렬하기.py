# (x, y) 좌표를 입력받은 N만큼 입력받고 오름차순으로 정렬할 때, x 좌표가 같으면 y좌표가 증가하는 순서로 정렬
# arr 이라는 변수에 리스트 형태로 수를 입력받음
# lambda를 이용하여 정렬 기준을 정해주고 정렬
# for문을 이용하여 배열 안의 요소를 정렬 기준에 따라 출력


import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x: (x[0], x[1]))                                          # 첫 번째 인자 x[0]에 해당하는 x좌표를 먼저 정렬하고
                                                                              # 그 다음 두 번째 인자 x[1]에 해당하는 y좌표를 정렬 

for i in arr:
  print(i[0], i[1])
