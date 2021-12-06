# 줄을 서 있는 사람의 수와 각 사람이 돈을 인출하는데 걸리는 시간이 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 문제


# 풀이
# 각 사람이 돈을 인출하는데 걸리는 시간을 리스트로 입력받고 오름차순으로 정렬한 뒤, 리스트 누적합의 합을 구하면 된다.
# 예를 들어, 5명의 사람이 돈을 인출하는데 걸리는 시간이 [3, 1, 4, 3, 2]라고 할 때, 이 배열을 정렬하여 [1, 2, 3, 3, 4]로 만든다.
# 정렬된 배열의 누적합을 구하면 [1, 3, 6, 9, 13]이 되는데, 이의 합을 구하면 돈을 인출하는 데 걸리는 시간 32분이 나오게 된다.


# 코드 (accumulate 모듈사용하기)

from itertools import accumulate
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
sum = list(accumulate(arr))

result = 0
for idx in sum:
  result += idx
print(result)



# 코드
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
result = 0

for idx in range(n):
  result += sum(arr[0:idx+1])
print(result)
