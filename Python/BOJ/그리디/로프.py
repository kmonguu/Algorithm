# N개의 로프가 있고 각각의 로프는 굵기나 길이가 다르게 때문에 들 수 있는 물체의 중량이 다를 수 있다.
# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k만큼의 중량이 걸리게 된다.
# 이 로프를 이용하여 들어올릴 수 있는 물체의 최대 중량을 구하는 프로그램


# 풀이
# 예제를 살펴봤을 때, 최대 중량이 10인 루프, 최대 중량이 15인 루프가 있을 때
# 두 로프는 모두 고르게 물체의 중량을 들어야하므로 한 루프가 들 수 있는 물체의 최대 중량은 15이지만, 들 수 있는 최대 중량이 10인 로프는 15를 들지 못한다.
# 결과적으로 두 로프는 같은 무게를 들면서 최대 중량을 들어야하므로 두 로프 모두 중량이 최대 10인 물체를 들 수 있다.
# 두 로프가 중량이 10인 물체를 들기 때문에 주어진 루프로 들 수 있는 물체의 최대 중량은 20이 된다.

# 결국 배열에 담긴 중량 중 작은 중량이 기준이 되므로
# 중량을 내림차순으로 정렬하여 N번째로 큰 수를 N번 곱하여 나온 값 중 가장 큰 수를 구하면 된다.

# 코드
import sys
input = sys.stdin.readline

w = [] 
n = int(input())
for _ in range(n):
  w.append(int(input()))
w.sort(reverse=True)                  # 로프가 들 수 있는 최대 중량이 담긴 배열을 내림차순으로 정렬한다.

result = []
for idx in range(n):
  result.append(w[idx]*(idx+1))       # w배열의 idx와 해당 요소의 자릿수를 곱하여 result 배열에 담는다.

print(max(result))




# 다른 풀이
import sys
input = sys.stdin.readline

n = int(input())
weights = sorted([int(input()) for _ in range(n)])    # 리스트 컴프리헨션으로 입력 받고 오름차순 정렬

result = 0
for i in range(n):
  weight = weights[i] * (n - i)                       # i번째 요소를 기준으로 최대 들 수 있는 중량 계산
  if result < weight:                                 # result의 최대값 구함
    result = weight

print(result)
