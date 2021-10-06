# 1에서 n까지의 임의로 입력받은 수로 만들어진 수열이 있다.
# 1부터 n까지 자연수를 스택에 push, pop하면서 주어진 수열을 만들어 push라면 '+'를, pop이라면 '-'를 출력


# 예시 1을 살펴보면 입력으로 [4, 3, 6, 8, 7, 5, 2, 1]을 입력하면 출력으로 [+, +, +, +, -, -, +, +, -, +, +, -, -, -, -, -]가 나온다.
# 이 예시를 설명해보면
# 출력이 +, +, +, + 이므로 스택에는 [1, 2, 3, 4]가 push된다.
# 그 다음으로 -, - 는 스택의 특성을 이용하여 스택의 제일 마지막부터 4, 3을 pop하여 [1, 2]가 남는다.
# 다음으로 +, + 는 스택에 5, 6이 push 되어 [1, 2, 5, 6]가 된다.
# -는 스택의 top에 있는 6을 pop하여 스택은 [1, 2, 5]가 되고
# 이어지는 +, + 는 7과 8을 push하여 [1, 2, 5, 7, 8]이 된다.
# 마지막으로 -, -, -, -, - 라는 5번의 pop은 스택의 top의 위치한 요소를 8, 7, 5, 2, 1 순으로 pop하게 된다.
# 따라서 pop이 된 요소를 보면 처음 입력했던 수열과 같은 [4, 3, 6, 8, 7, 5, 2, 1]이 만들어진다.


# 코드
import sys
input = sys.stdin.readline

count = 1                               # 1부터 n까지의 자연수를 나타내는 count 변수를 1로 초기화
stack = []                              # 스택이 저장될 리스트 stack 생성
result = []                             # push, pop을 나타내는 '+', '-'를 저장할 result 리스트 생성

for _ in range(int(input())):
  number = int(input())

  while count <= number:                # count가 수열을 입력받은 number보다 작거나 같을 때까지 while문 반복
    stack.append(count)                 # count 변수에 저장된 수를 stack 리스트에 넣고
    result.append('+')                  # result 리스트에는 push라는 의미로 '+'를 저장
    count += 1                          

  if stack[-1] == number:               # 스택에 제일 위에 위치한 수가 number와 같다면
    stack.pop()                         # stack 리스트에서 pop
    result.append('-')                  # result 리스트에는 pop이라는 의미로 '-'를 저장

if stack:                               # 만약 임의의 수열과 같은 수열을 만들었다면 stack 리스트에는 아무것도 남아있지 않아야하지만 stack이 비어있지 않다면
  print('NO')                           # 'NO'를 출력

else:
  for i in result:
    print(i)
