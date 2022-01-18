# 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4... 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.
# 구간의 시작과 끝을 나타내는 정수 a, b가 주어질 때 수열에서 a번째 숫자부터 b번째 숫자까지 합을 출력

# 내가 푼 코드
# 풀이
# 변수 i를 0으로 두고 while 문으로 수열이 담기는 배열 arr의 길이가 구간의 끝인 b보다 커질 때까지 i를 i번 배열에 담는 식으로 수열을 구했다.

a, b = map(int, input().split())

arr = []
i = 0

while len(arr) < b:
  i += 1
  for _ in range(i):
    arr.append(i)

print(sum(arr[a-1:b]))



# 다른 사람 코드

a, b = map(int, input().split())

numbers = [1]
while len(numbers) < b:
  numbers.extend([numbers[-1] + 1] * (numbers[-1] + 1))

print(sum(numbers[a - 1: b]))


# 풀이
# 구간의 범위가 1 ≤ a ≤ b ≤ 1,000 이므로 리스트의 크기가 1000이 넘어가는 순간인 1~45까지 배열에 미리 수열을 만들어놓고 입력받은 구간만큼 합을 출력했다.

a, b = map(int, input().split())

arr = []
for i in range(46):
  arr += [i]*i
print(sum(arr[a-1:b]))
