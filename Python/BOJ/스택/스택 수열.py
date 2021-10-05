# 1에서 n까지의 임의로 입력받은 수로 만들어진 수열이 있다.
# 1부터 n까지 자연수를 스택에 push, pop하면서 주어진 수열을 만들어 push라면 '+'를, pop이라면 '-'를 출력

# 풀이



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
