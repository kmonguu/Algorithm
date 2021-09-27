# 정수를 저장하는 스택을 구현하여 5개의 명령을 처리하는 프로그램
# 1. push x : 정수 x를 스택에 넣는 연산
# 2. pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우, -1 출력
# 3. size : 스택에 들어있는 정수의 개수를 출력
# 4. empty : 스택이 비어있으면 1 아니면 0 출력
# 5. top : 스택의 가장 위에 있는 정수를 출력, 만약 스택에 들어있는 정수가 없는 경우 -1 출력


# 풀이
# list 형태로 정수를 입력받고 stack 이라는 빈 리스트를 생성
# input으로 정수를 입력받으면 시간 초과가 나므로 sys 모듈을 사용하여 입력받는다.
# 명령에 따라 수행할 수 있도록 if else 문을 사용하여 경우를 나누어 줌

# 코드
import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
  x = list(input().split())

  if x[0] == 'push':                        # 입력받은 첫 번째 인자가 push인 경우
    stack.append(x[1])                      # 두 번째 인자를 stack 리스트에 넣어줌

  elif x[0] == 'pop':                       # 입력받은 첫 번째 인자가 pop인 경우
    if stack:                               # stack 리스트가 비어 있는지를 확인
      print(stack.pop())                    # 비어있지 않으면 내장함수 pop을 이용하여 stack에 들어있는 가장 위에 위치한 정수를 반환 후 제거
    else:
      print(-1)

  elif x[0] == 'size':                      # 입력받은 첫 번째 인자가 size인 경우
    print(len(stack))

  elif x[0] == 'empty':                     # 입력받은 첫 번째 인자가 empty인 경우
    if stack:
      print(0)
    else:
      print(1)

  elif x[0] == 'top':                       # 입력받은 첫 번째 인자가 top인 경우
    if stack:
      print(stack[-1])
    else:
      print(-1)
