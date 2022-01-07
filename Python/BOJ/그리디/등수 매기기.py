# N명의 학생들에게 자신이 N명 중에서 몇 등을 할 것인지 예상 등수를 적어서 제출하도록 하였다.
# 하지만 실수로 모든 학생들의 프로그램을 날려버려 임의로 등수를 매겼다. 
# 학생들이 제출한 예상 등수와 임의 등수가 차이가 있을 때 이 불만도는 |(학생들의 예상 등수) - (임의 등수)|로 수치화할 수 있다.
# 이 불만도의 합을 최소화하는 프로그램


# 풀이 
# 1등부터 N등까지 동석차가 없다는 점을 이용하여 5명의 학생의 예상 등수로 1 5 3 1 2 가 주어졌다면 이를 1 1 2 3 5로 정렬한다.
# 각 학생이 받아야 하는 실제 등수는 1 2 3 4 5이므로 정렬된 예상 등수와 같은 자릿수의 차의 절댓값의 합을 구하면 된다.


# 처음 시간초과 코드
# 배열을 예상 등수를 담은 rank와 실제 등수를 담은 index 두개를 만들어 풀었음
# repl에서는 예제대로 답이 나왔지만 백준에 제출했을 땐 시간 초과 발생

import sys
input = sys.stdin.readline

rank = []
n = int(input())
for _ in range(n):
  rank.append(int(input()))
  rank.sort()

result = 0
index = []
for i in range(n):
  index.append(i+1)

  if rank[i] != index[i]:
    result += abs(rank[i] - index[i])

print(result)




# 정답 코드
import sys
input = sys.stdin.readline

rank = []
n = int(input())
rank = sorted([int(input()) for _ in range(n)])

print(sum(abs(rank[i] - (i+1)) for i in range(n)))
