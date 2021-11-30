# 농부가 묘목 하나를 심는데 걸리는 시간은 1일이고, 묘목의 수만큼 입력받은 날짜가 묘목이 완전히 자라는데 걸리는 시간이라고 할 때
# 마지막 나무가 다 자란 다음날 이장님을 초대해야 한다. 이장님을 최대한 빨리 초대할 수 있는 날짜를 출력

# 풀이
# 이장님을 최대한 빨리 초대를 해야하므로 자라는데 시간이 가장 오래 걸리는 묘목을 가장 먼저 심어야 한다.
# 자라는 시간이 오래걸리는 순으로 정렬하고, 구매하는 날 하루를 포함하여 각각의 나무를 심는데 딜레이되는 날짜를 더해준다.

# 예를 들어, 묘목 4개가 다 자라는데 각각 2 3 4 3 일이 소요된다고 할 때, 4 3 3 2 순으로 내림차순 정렬한다.
# o o o o
#   o o o 
#     o o o
#       o o
# 위와 같이 나무가 자란다고 할 때 

# x o o o o
# x x o o o
# x x x o o o
# x x x x o o
# 나무를 구매하고 심고 자라는 데 (x + o) 일이 소요되게 된다. 그럼 총 6일이 소요되는데 이장님은 마지막 나무가 다 자란 다음날 초대해야하므로 마지막에 +1을 해준다.


# 코드
import sys
input = sys.stdin.readline

n = int(input())
day = sorted(map(int, input().split()), reverse = True)

buy = 1                                                     # 모묙을 구매하고 심길 때 까지 소요되는 일 수
result = []                     

for i in day:
  result.append(i + buy)                                    # 나무가 완전히 자라는 데 걸리는 시간 + buy 를 result 배열에 담아준다.
  buy += 1

print(max(result)+1)                                        # result에 담긴 값 중 가장 큰 값에 +1을 하면 원하는 값을 얻을 수 있다.






# 다른 코드 : 람다식을 활용
# enumerate를 사용하면 (인덱스, 요소)순으로 반환해준다.

import sys
input = sys.stdin.readline

n = int(input())
day = sorted(map(int, input().split()), reverse=True)

result = max(map(lambda x: x[0] + x[1] + 1, enumerate(day)))    # (묘목이 심길 때까지 걸리는 일 수 + 나무로 완전히 자랄 때까지 걸리는 일 수 + 묘목을 구매하는 하루)의 최댓값을 result에 저장
print(result + 1)
