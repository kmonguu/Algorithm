# N개의 도시가 있고 몇km 떨어져있다. 각각에 도시들에는 하나의 주유소가 있고 도시 마다 주유소의 가격이 다를 수 있다.
# 각 도시에 있는 주유소의 기름 가격과, 각 도시를 연결하는 도로의 길이를 입력으로 받아 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소 비용을 출력

# 예제
# 4개의 도시의 기름 값은 각각 5, 2, 4, 1 원 이다. 
# 각 도시마다 거리는 2km, 3km, 1km 떨어져 있다.
# 이때, 제일 왼쪽 도시에서 제일 오른쪽 도시까지 한번에 가기 위해 기름은 6km 만큼을 넣으면 기름값은 30원이 든다.
# 가장 좋은 방법은 제일 왼쪽 도시에서 다음 도시로 2km 이동하기 위해 2리터 주유하고(5*2) 다음 도시는 기름 값이 3 번째 도시보다 싸기 때문에
# 기름 값이 2원 하는 도시에서 가장 오른쪽 도시로 한번에 가기 위해 4리터를 주유하면(2*4) 총 18원이 든다. 이 방법이 가장 최소의 비용이 든다.


# 풀이
# 가장 왼쪽의 도시는 다음 도시로 가기 위해 무조건 한 번은 주유를 해야 하기 때문에 oil이라는 변수를 하나 두어 첫 번째 도시의 기름 값을 저장했다.
# oil에 저장된 기름값과 다음 도시의 기름값을 비교하여 다음 도시의 기름값이 크거나 같다면 둘 중 더 싼 기름 값인 oil에 거리를 곱하여 총 기름값을 구한다.
# oil과 다음 도시의 기름값을 비교하여 다음 도시의 기름값이 더 작다면 다음 도시의 기름 값이 더 싼 것이 되므로 oil에 다음 도시의 기름 값을 저장한 뒤 
# 기름값을 계산해준다.


# 코드
import sys
input = sys.stdin.readline

city = int(input())
km = list(map(int, input().split()))
L = list(map(int, input().split()))

oil = L[0]
sum = 0
for i in range(city-1):
  if L[i] >= oil:
    sum += oil*km[i]

  elif L[i] < oil:
    oil = L[i]
    sum += oil*km[i]

  else:
    sum += km[i]

print(sum)




# 다른 풀이 : zip 함수를 이용한 방법
# 현재 문제에서 주어진 최대 가격이 10 ** 9이므로 min_price라는 변수의 초기값으로 1e9로 설정해준다.
# zip 함수를 이용하여 기름값과 가격을 묶는다. 이때 마지막 도시의 주유소 가격은 필요없으므로 price[:-1]로 자른다.

import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

result, min_price = 0, 1e9

for r, p in zip(road, price[:-1]):
  if p < min_price:                       # p가 min_price보다 작다면
    min_price = p                         # min_price 값 갱신

  result += (min_price * r) # 비용 계산

print(result)

