# 첫째 줄에 수의 개수가 주어지고 둘째 줄부터 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
# 수를 입력받고 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력


import sys                                  # 입력받는 시간을 줄이기 위해 sys 모듈 사용
input = sys.stdin.readline

num = [0]*10001                             # 입력받을 수의 최대 크기만큼 배열을 생성한 뒤 0으로 초기화
for _ in range(int(input())):
  num[int(input())] += 1                    # 0으로 초기화된 배열에서 입력받은 수의 인덱스에 1을 더해줌

for i in range(len(num)):                   # 배열의 길이만큼 다시 for문 범위 안에서 변수 i를 반복하고
    for j in range(num[i]):                 # 중첩 for문으로 num[i]에 입력된 수만큼 변수 j에 선언
      print(i)                              # j만큼 그 수를 출력하면 오름차순으로 정렬된 수를 확인할 수 있다.
