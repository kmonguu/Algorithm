# 비어있는 공집합 s가 주어졌을 때, 아래 연산을 수행하는 프로그램
# 1. add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# 2. remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# 3. check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# 4. toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# 5. all: S를 {1, 2, ..., 20} 으로 바꾼다.
# 6. empty: S를 공집합으로 바꾼다.


# 코드
import sys
input = sys.stdin.readline

s = []
m = int(input())
for _ in range(m):
  order = input().split()

  if order[0] == "add":
    if int(order[1]) not in s:
      s.append(int(order[1]))

  elif order[0] == "remove":
    if int(order[1]) in s:
      s.remove(int(order[1]))

  elif order[0] == "check":
    print(1) if int(order[1]) in s else print(0)

  elif order[0] == "toggle":
    s.remove(int(order[1])) if int(order[1]) in s else s.append(int(order[1]))

  elif order[0] == "all":
    s = [i for i in range(1,21)]

  elif order[0] == "empty":
    s = []
    
    
    
# 다른 풀이
# command 딕셔너리를 만들고, key에 명령어 이름, value에 lambda 식 넣어 푸는 방법

import sys
input = sys.stdin.readline

s = set()
all_set = set(map(str, range(1, 21)))
command = {
  "add": lambda x: s.add(x),
  "remove": lambda x: s.discard(x),
  "check": lambda x: print(1 if x in s else 0),
  "toggle": lambda x: s.discard(x) if x in s else s.add(x),
  "all": lambda: all_set,
  "empty": lambda: set()
}

m = int(input())
for _ in range(m):
  c = input().strip().split()
  if len(c) == 1: s = command[c[0]]()                             # c의 길이가 1일때는 명령어에 해당하는 함수 호출하고 s 갱신
  else: command[c[0]](c[1])                                       # c의 길이가 2일때는 명령어에 해당하는 함수 호출
