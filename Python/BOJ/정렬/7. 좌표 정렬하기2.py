# (x, y) 좌표를 N개 입력했을 때, 좌표를 y가 증가하는 순으로 정렬할 때 y좌표가 같으면 x좌표가 증가하는 순서로 출력
# lambda 식을 사용하여 정렬 기준을 y좌표 -> x좌표 순서로 한다.

import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x: (x[1], x[0]))                                      # 1 번 인덱스인 y좌표를 오름차순 정렬 후 x좌표를 정렬하는 lambda 식

for i in arr:
  print(i[0], i[1])                                                       # 0 번 인덱스인 x좌표, 1번 인덱스 y좌표 순으로 출력
