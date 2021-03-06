# 두 문자열 s, t가 주어졌을 때, s를 t로 바꾸는 게임이다.
# 문자열을 바꿀 때는 1. 문자열의 뒤에 A를 추가한다. 2. 문자열을 뒤집고 뒤에 B를 추가한다. 이 2가지의 연산만 가능하다.
# 주어진 조건을 이용하여 s를 t로 만들 수 있다면 1을 출력 아니면 0을 출력


# 풀이 
# 처음엔 단순하게 문제에서 나온대로 s를 t로 만들기 위해 접근했지만, 반복문 안에 조건이 계속 추가됨 한 번 실패 후
# 접근을 t를 s로 만드는 방법으로 하여 문제 나온 2가지 연산을 다음과 같이 했음
# 1. 문자열 뒤에 A가 있다면 뺀다. 2. B를 빼고 문자열을 뒤집는다.


# 코드
import sys
input = sys.stdin.readline
  
s = list(map(str, input().strip()))     # pop을 해주기 위해 문자열을 배열로 입력받았다.
t = list(map(str, input().strip()))

while len(s) < len(t):                  # s의 길이가 t의 길이보다 작은 동안은 반복문 실행
  if t[-1] == 'A':                      # t의 마지막 요소가 'A'인 경우
    t.pop()                             # pop해준다.

  elif t[-1] == 'B':                    # t의 마지막 요소가 'B'인 경우
    t.pop()                             # pop해주고
    t.reverse()                         # 배열을 뒤집어준다.

if s == t:                              # s와 t가 같다면
  print(1)                              # 1 
else: 
  print(0)
  
  
  
  
# 다른 풀이
s, t = input(), input()

while len(t) != len(s):                 # t와 s의 길이가 같아질때까지 반복
  if t[-1] == "A":                      # t의 마지막 요소가 A라면 t에서 마지막 요소 잘라냄
    t = t[:-1]           
  else: t = t[:-1][::-1]                # t의 마지막 요소가 B라면 t에서 마지막 요소 잘라내고 뒤집음

print(1 if s == t else 0)               # 삼항연산자를 사용하여 print
