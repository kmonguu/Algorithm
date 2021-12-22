# AAAA와 BB 라는 폴리오미노를 2개 가지고 있고, '.'와 'X'로 이루어진 보드판이 입력으로 주어진다.
# 겹침없이 'X'를 모두 폴리오미노로 덮으면서 동시에 '.'은 덮으면 안된다.
# 폴이오미노로 모두 덮은 보드판을 출력하는 프로그램


# 풀이
# 주어진 보드판의 'X'를 폴리오미노로 replace하여 풀었다.
# 예제에서 보드판이 XXXXXX 이라면, replace를 사용하여 먼저 왼쪽부터 4개 XXXX를 'AAAA'로 치환
# 바뀐 보드판에서 다시 replace를 사용하여 남은 XX를 모두 'BB'로 바꿔준다.



# 코드

import sys
input = sys.stdin.readline

s = input() 
s = s.replace('XXXX', 'AAAA')       # 문자열 s에서 보드판 XXXX는 폴리오미노 'AAAA'로 replace
s = s.replace('XX', 'BB')           # 문자열 s에서 보드판 XX는 폴리오미노 'BB'로 replace

if 'X' in s:                        # 보드판을 주어진 폴리오미노로 replace가 끝난 후에도 보드판에 여전히 X가 남아있다면
  print(-1)                         # -1 출력       
else: 
  print(s)

  
  
  
# 다른 풀이
board = input().replace("XXXX", "AAAA").replace("XX", "BB")
print(-1 if "X" in board else board)



# 다른 풀이
# A로 먼저 덮고, B를 덮는 함수
# 예를 들어 XXXXXX 이면 l은 6이고, "A" * 4 * (6 // 4) + "B" * (l % 4)으로 A 먼저 덮고 B를 덮을 수 있음

board = input()

def convert(l):
  return ("A" * 4 * (l // 4) + "B" * (l % 4)) if not l % 2 else -1          # l 만큼 모두 덮을 수 있으면 덮은 결과, 덮을 수 없으면 -1 return

result = ""
l = 0
for b in board:
  if b == "X":
    l += 1                                                                  # X의 길이 구함
  else:
    tmp = convert(l)                                                        # 덮은 문자열로 변환
    result += ("" if tmp == -1 else (tmp + b))                              # l 만큼 덮지 못하였으면 "", 덮었으면 tmp + "."을 result에 더함
    l = 0                                                                   # l 초기화

tmp = convert(l)                                                            # 남은 문자열에 대한 길이에 대해 덮은 문자열로 변환
result += ("" if tmp == -1 else tmp)                                        # l 만큼 덮지 못하였으면 "", 덮었으면 tmp을 result에 더함
print(result if len(result) == len(board) else -1)                          # result와 board의 길이가 같으면 result, 다르면 -1 출력
