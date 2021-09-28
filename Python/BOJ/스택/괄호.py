# 입력으로 괄호를 입력받는데, 이때 입력받은 괄호 문자열이 '('과 ')'으로 이루어진 올바른 괄호 문자열인지 확인한다.
# 괄호 문자열이 올바른 괄호 문자열이면 'YES'를, 아니라면 'NO'를 출력한다.

# 풀이
# 빈 스택리스트를 생성하고 만약 괄호 문자열의 요소가 '(' 괄호라면 스택 리스트에 추가합니다.
# 만약 괄호 문자열의 요소가 ')' 괄호인 경우 if문을 통해 한쌍의 괄호를 만들어 pop 합니다.

# 오류
# 처음 ')' 일 때 무조건 pop 하도록 if문을 만들었지만 만약 스택이 비어있을 경우 pop을 못함
# 이 경우 올바른 괄호 문자열인지 출력하는 부분에서 빈 스택리스트를 올바른 괄호 문자열로 인식하여 'YES'를 출력했음

# 수정
# i가 ')' 괄호인 경우 pop을 하기 위해 스택 리스트가 비어있지 않은지를 확인
# 만약 스택 리스트가 비어있다면 그대로 스택 리스트에 추가해줌


# 코드
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  stack = []                                # 스택 리스트 생성
  for i in (input()):                       # 입력받은 문자열 요소를 반복적으로 i에 선언
    if i == '(':                            # i가 '('라면
      stack.append(i)                       # 스택 리스트에 추가

    elif i == ')':                          # i가 ')' 인 경우
      if stack and stack[-1] == "(":        # 스택 리스트가 비어있지 않고 스택 리스트의 마지막 요소가 '(' 괄호인 경우
        stack.pop()                         # 괄호는 한쌍이 되므로 pop해줌
      else:                                 # 위의 조건에 안맞을 경우
        stack.append(i)                     # ')' 괄호는 짝이 없어 pop되지 않았으므로 스택 리스트에 추가해줌

  if stack:                                 # 만약 스택에 요소가 있다면
    print('NO')                             # 입력받은 괄호 문자열이 모두 pop되지 못하고 남았다는 의미이므로 올바른 괄호 문자열이 아님
  else:
    print('YES')                            # 리스트가 비었다면 괄호들이 모두 pop되었다는 의미이므로 올바른 괄호 문자열이 됨
    

    
    
    
# 다른 풀이    
# 괄호가 i에 선언될 때 마다 매번 스택 리스트를 확인하여 효율성이 떨어지는 것을 보완

import sys
input = sys.stdin.readline

for _ in range(int(input())):
  stack = []
  for i in (input().rstrip()):
    if i == ')':                              # i가 ')'인 경우
      if stack and stack[-1] == "(":          # if문의 조건을 확인하고
        stack.pop()                           # 조건에 맞다면 pop
        continue                      
      else:                                   
        stack.append(i)                       # 조건에 맞지 않다면 스택 리스트에 추가 
        break
    
    stack.append(i)                           # i가 ')' 괄호가 아닌 경우 스택 리스트에 추가

  if stack:
    print('NO')
  else:
    print('YES')
