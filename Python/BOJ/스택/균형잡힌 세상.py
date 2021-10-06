# 괄호를 포함한 문자열을 입력받았을 때, 입력받은 문자열 '(' 과 ')'이 짝을 이루었는지 '[' 와 ']' 가 짝을 이루었는지 판단
# 입력의 조건으로 '.' 가 들어오고 영문, 소괄호, 대괄호가 입력된다.
# 문자열이 완전한 괄호들로 균형을 이루고 있다면 'YES'를 아니라면 'NO'를 출력한다.


# 첫번째 코드 : 런타임 에러
# 24번 째 줄의 elif문의 조건으로 stack이 비어있지 않으면서 i == ')' 또는 i == '['이어야 한다라는 의미
# 만약 입력으로 ')))'이 들어온다면 stack에 append 될 것이 없기 때문에 stack은 빈 리스트가 되고 'yes'가 출력되므로 오류

import sys
input = sys.stdin.readline

while True:
  string = input().rstrip()

  if string == '.':
    break
  
  stack = []

  for i in string:

    if i == '(' or i == '[':
      stack.append(i)

    elif stack and i == ')' or i == ']':  
      if i == ')' and stack[-1] == '(':
        stack.pop()
      elif i == ']' and stack[-1] == '[':
        stack.pop()
      else:
        stack.append(i)
          
  if stack:
    print('NO')
  
  else:
    print('YES')
    
    
    
# 정답 코드
import sys
input = sys.stdin.readline

while True:
  string = input().rstrip()

  if string == '.':
    break
  
  stack = []

  for i in string:
    if i == '(' or i == '[':
      stack.append(i)

    elif i == ')' or i == ']':
      if stack and i == ')' and stack[-1] == '(':
        stack.pop()
      elif stack and i == ']' and stack[-1] == '[':
        stack.pop()
      else:
        stack.append(i)
  
  if stack:
    print('no')
  else:
    print('yes')
