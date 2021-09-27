# k개의 정수가 한줄에 하나씩 입력된다. 입력된 정수가 0일 경우 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
# 최종적으로 적어 낸 수의 합을 출력한다.


# 풀이
# stack 이라는 빈 리스트를 생성한다.
# 0일 경우 가장 최근에 쓴 수를 지운다는 말은 0일 경우 스택에서 'pop'하라는 의미이고
# 아닐 경우는 정수 k를 스택에 push하라는 의미가 된다.
# 최종적으로 스택에 담겨있는 수의 합을 sum을 이용하여 출력


# 코드
import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
  k = int(input())

  if k == 0:                        # k가 0인 경우
    stack.pop()                     # 내장 함수 pop을 이용하여 스택의 가장 위에 위치한 정수를 반환 후 삭제
  else:                             # 0이 아닐 경우
    stack.append(k)                 # 정수 k를 stack 리스트에 push 한다.

print(sum(stack))
