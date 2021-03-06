# 지구를 나타내는 수 e, 태양을 나타내는 수 s, 달을 나타내는 수 m이 있을 때, 이 수는 각각  (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)의 범위를 가진다.
# e, s, m이 주어졌고, 1년이 준규가 사는 나라에서 1 1 1 일 때, 준규가 사는 나라에서 e, s, m이 우리가 알고 있는 연도로 몇 년인지 출력


# 예제
# 15년은 15 15 15로 나타낼 수 있다.
# 1년이 지나 16년은 16 16 16 이 아니라 1 16 16으로 나타낼 수 있다. e의 범위 15를 넘어가기 때문이다.


# 풀이
# 년도를 나타내는 year 변수를 1로 초기화 한다.
# (year-e)%15, (year-s)%28, (year-m)%19 가 모두 0으로 떨어지는 year이 나올 때까지 year에 +1을 한다.
# year의 최댓값은 e, s, m이 15, 28, 19가 될 때의 년도 7980년이다.
# 경우의 수를 모두 찾는 완전탐색 문제이다.


# 코드
import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

year = 1
while True:
  if (year-e) % 15 == 0 and (year-s) % 28 == 0 and (year-m) % 19 == 0:
    print(year)
    break
  year += 1
  

  
# 다른 풀이 : e, s, m 에서 1씩 감소시켜서 연도를 구하고, e, s, m은 0 이하가 될 수 없으므로 0 이하가 될 때, 각 값의 최대값을 더하면서 구함
e, s, m = map(int, input().split())

year = 1
while e != 1 or s != 1 or m != 1:
  if e <= 0: e += 15; continue
  if s <= 0: s += 28; continue
  if m <= 0: m += 19; continue

  e, s, m = e - 1, s - 1, m - 1
  year += 1

print(year)
