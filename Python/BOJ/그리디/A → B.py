# 정수 A를 B로 바꾸려고 할 때 할 수 있는 연산은 2가지이다.
# 1. 2를 곱한다.
# 2. 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

# 내가 푼 코드
# B에서 A로 만드는 것으로 문제를 풀었다.
# B가 짝수라면 2로 나누었고, B를 10으로 나누었을 때 나머지가 1이라면 수의 가장 오른쪽에 1이 있다는 의미이므로 1을 떼어준다.
# B가 짝수도 아니고 10으로 나누었을 때 나머지가 1도 아니라면 이 수는 A로 만들 수 없는 수이므로 반복을 멈추고 -1을 출력한다.

a, b = map(int, input().split())
cnt = 1

while a < b:
  if b % 2 == 0:
    b = b//2
    cnt += 1

  elif b % 10 == 1:
    b = b//10
    cnt += 1

  else:
    break
  
if a == b:
  print(cnt)
else:
  print(-1)

  
  
# 다른 사람 코드

a, b = map(int, input().split())

cnt = 1
while a < b:
  if b % 2 == 0: b = b//2
  elif b % 10 == 1: b = b // 10
  else: break
  
  cnt += 1

print(cnt if a == b else -1)
