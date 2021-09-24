# 수를 리스트 형태로 입력받고 수가 작은 순으로 번호를 매겨 출력한다.
# 수에 번호를 매기는 과정에서 딕셔너리를 사용하여 0부터 N까지 번호를 매긴다.


import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
x_set = sorted(set(x))

dic = {x_set[i]:i for i in range(len(x_set))}

for i in x:
  print(dic[i], end=' ')
