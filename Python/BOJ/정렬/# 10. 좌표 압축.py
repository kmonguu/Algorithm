# 수를 리스트 형태로 입력받고 수가 작은 순으로 번호를 매겨 출력한다.
# 수에 번호를 매기는 과정에서 딕셔너리를 사용하여 0부터 N까지 번호를 매긴다.


import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
x_set = sorted(set(x))                            # s_set이라는 변수에 입력받은 배열 x를 set함수를 통해 중복을 제거하고 오름차순으로 정렬하여 저장

dic = {x_set[i]:i for i in range(len(x_set))}     # s_set 의 길이를 범위로 하여 딕셔너리를 for문을 통해 key값을 변수 i로 할당하여 변수 dic에 저장

for i in x:                                       # 입력받은 배열이 저장된 x에서 for문을 실행하고
  print(dic[i], end=' ')                          # 딕셔너리를 이용하여 배열에 저장된 수에 매겨진 번호를 출력
