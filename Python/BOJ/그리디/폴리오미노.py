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
