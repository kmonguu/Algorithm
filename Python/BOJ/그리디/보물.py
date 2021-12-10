# S = A[0] X B[0] + ... + A[N-1] X B[N-1] 이라는 길이가 N인 정수 배열 A와 B가 있다.
# S의 최솟값을 출력한다.
# 단 B에 있는 수는 재배열하면 안된다.


# 풀이
# S가 최솟값이 되려면 B배열의 가장 작은 값과 A의 가장 큰 값이 곱해지고, B배열의 가장 큰 값이 A배열의 가장 큰 값고 곱해져야 한다.
# 예제에서 A = [1, 1, 1, 6, 0], B = [2, 7, 8, 3, 1]일 때
# A = [0, 1, 1, 1, 6], B = [8, 7, 3, 2, 1] 로 정렬되어야 S의 최솟값을 구할 수 있다.


# 코드
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()), reverse=True)     # a 배열은 내림차순으로 정렬되도록 한다.
b = sorted(map(int, input().split()))                   # b 배열은 오른차순으로 정렬되도록 한다.

result = 0
for idx in range(n):
  result += a[idx]*b[idx]
print(result)




# 다른 풀이
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))                   # a 오름차순 정렬
b = sorted(map(int, input().split()), reverse=True)     # b 내림차순 정렬

print(sum([x * y for x, y in zip(a, b)]))               # zip 함수를 이용하여 a, b 리스트를 묶고 곱을 구한 후 sum 함수를 이용하여 전체 합을 구함





# 다른 풀이
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)

print(sum(map(lambda x, y: x * y, a, b)))               # map 함수와 lambda식을 이용하여 a, b 모든 요소의 곱을 구하고 sum 함수를 이용하여 전체 합을 구함
