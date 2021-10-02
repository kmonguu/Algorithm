# 괄호를 포함한 문자열을 입력받았을 때, 입력받은 문자열 '(' 과 ')'이 짝을 이루었는지 '[' 와 ']' 가 짝을 이루었는지 판단
# 입력의 조건으로 '.' 가 들어오고 영문, 소괄호, 대괄호가 입력된다.
# 문자열이 완전한 괄호들로 균형을 이루고 있다면 'YES'를 아니라면 'NO'를 출력한다.


# 첫번째 코드 : 런타임 에러
import sys
input = sys.stdin.readline

while True:
  string = input().rstrip()

  if string == '.':
    print('YES')
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
